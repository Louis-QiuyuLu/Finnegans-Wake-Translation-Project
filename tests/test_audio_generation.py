import hashlib
import importlib.util
import json
import multiprocessing
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/generate_audio.py'
spec = importlib.util.spec_from_file_location('generate_audio', SCRIPT)
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


def register_worker(folder, number, gate):
    gate.wait()
    for j in range(8):
        api.register_audio({'id': f'{number}-{j}', 'original': str(j)}, folder)


class AudioGenerationTests(unittest.TestCase):
    def test_registering_a_regenerated_track_preserves_other_tracks(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            api.register_audio({'id': 'a', 'original': 'first'}, root)
            api.register_audio({'id': 'b', 'original': 'second'}, root)
            api.register_audio({'id': 'a', 'original': 'revised'}, root)
            tracks = json.loads((root / 'index.json').read_text())['tracks']
            self.assertEqual([t['segment_id'] for t in tracks], ['a', 'b'])
            self.assertEqual(tracks[0]['original_sha256'], hashlib.sha256(b'revised').hexdigest())

    def test_only_nonempty_indexed_current_audio_can_be_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            segment = {'id': 'a', 'original': 'topples'}
            (root / 'a.mp3').write_bytes(b'audio')
            self.assertFalse(api.audio_is_current(segment, root))
            api.register_audio({'id': 'a', 'original': 'toples'}, root)
            self.assertFalse(api.audio_is_current(segment, root))
            api.register_audio(segment, root)
            self.assertTrue(api.audio_is_current(segment, root))
            (root / 'a.mp3').write_bytes(b'')
            self.assertFalse(api.audio_is_current(segment, root))

    def test_concurrent_registration_keeps_every_track(self):
        with tempfile.TemporaryDirectory() as folder:
            context = multiprocessing.get_context('fork')
            gate = context.Barrier(6)
            processes = [context.Process(target=register_worker, args=(folder, i, gate)) for i in range(6)]
            for process in processes:
                process.start()
            for process in processes:
                process.join(10)
            self.assertTrue(all(process.exitcode == 0 for process in processes))
            tracks = json.loads((Path(folder) / 'index.json').read_text())['tracks']
            self.assertEqual(len(tracks), 48)

    def test_publish_rejects_changed_original_and_preserves_previous_audio(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'a.mp3').write_bytes(b'old audio')
            candidate = root / 'candidate.mp3'
            candidate.write_bytes(b'new audio')
            with self.assertRaisesRegex(RuntimeError, '原文'):
                api.publish_audio({'id': 'a', 'original': 'old'}, candidate, root,
                                  current_segments=[{'id': 'a', 'original': 'new'}])
            self.assertEqual((root / 'a.mp3').read_bytes(), b'old audio')
            self.assertFalse((root / 'index.json').exists())

    def test_publish_atomically_replaces_file_and_registers_original(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            segment = {'id': 'a', 'original': 'text'}
            (root / 'a.mp3').write_bytes(b'old audio')
            candidate = root / 'candidate.mp3'
            candidate.write_bytes(b'new audio')
            api.publish_audio(segment, candidate, root, current_segments=[segment])
            self.assertEqual((root / 'a.mp3').read_bytes(), b'new audio')
            self.assertFalse(candidate.exists())
            self.assertTrue(api.audio_is_current(segment, root))

    def test_publish_rejects_empty_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            candidate = root / 'candidate.mp3'
            candidate.touch()
            with self.assertRaises(ValueError):
                api.publish_audio({'id': 'a', 'original': 'text'}, candidate, root,
                                  current_segments=[{'id': 'a', 'original': 'text'}])


class AudioBatchTests(unittest.TestCase):
    def batch(self):
        spec = importlib.util.spec_from_file_location('audio_batch', SCRIPT.with_name('audio_batch.py'))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_queue_prioritizes_three_expired_tracks_and_omits_current(self):
        batch = self.batch()
        segments = [{'id': sid, 'original': sid} for sid in ['fw-i1-a', 'fw-i3-069-30', 'fw-i3-067-28', 'fw-i3-072-17']]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'fw-i1-a.mp3').write_bytes(b'audio')
            api.register_audio(segments[0], root)
            self.assertEqual([s['id'] for s in batch.build_queue(segments, root)],
                             ['fw-i3-067-28', 'fw-i3-069-30', 'fw-i3-072-17'])

    def test_original_freeze_ignores_translation_changes_but_rejects_source_changes(self):
        batch = self.batch()
        before = [{'id': 'a', 'original': 'text', 'translation': '旧'}]
        same = [{'id': 'a', 'original': 'text', 'translation': '新'}]
        batch.check_originals(before, same)
        with self.assertRaisesRegex(RuntimeError, '原文'):
            batch.check_originals(before, [{'id': 'a', 'original': 'changed'}])

    def run_fake_batch(self, child_success):
        from unittest.mock import patch
        import contextlib
        import io
        import sys
        batch = self.batch()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'scripts').mkdir()
            code = '''import sys,json,pathlib
args=sys.argv[1:]
if '--audio-dir' not in args:
    raise SystemExit(8)
out=pathlib.Path(args[args.index('--audio-dir')+1]);out.mkdir(parents=True,exist_ok=True)
sid=args[args.index('--segment')+1]
hash_value=args[args.index('--expected-original-sha256')+1]
(out/(sid+'.mp3')).write_bytes(b'candidate')
(out/'index.json').write_text(json.dumps({'tracks':[{'segment_id':sid,'file':sid+'.mp3','original_sha256':hash_value}]}))
'''
            if not child_success:
                code = 'raise SystemExit(9)\n'
            (root / 'scripts/generate_audio.py').write_text(code)
            segments = [{'id': 'fw-i1-a', 'original': 'text', 'chapter': 'I.1'}]
            argv = ['audio_batch.py', '--run-dir', str(root / 'run'), '--device', 'cpu', '--attempts', '1']
            with patch.object(sys, 'argv', argv), patch.object(batch, 'ROOT', root), \
                    patch.object(batch, 'AUDIO_DIR', root / 'audio'), \
                    patch.object(batch, 'book_one', return_value=segments), \
                    patch.object(batch.time, 'sleep'), contextlib.redirect_stdout(io.StringIO()):
                # The queue uses its explicit destination; no real repo file is touched.
                result = batch.main()
            state = json.loads((root / 'run/state.json').read_text())
            return result, state, (root / 'audio/fw-i1-a.mp3').exists()

    def test_failed_batch_saves_state_and_exits_nonzero(self):
        result, state, published = self.run_fake_batch(False)
        self.assertEqual(result, 1)
        self.assertEqual(state['status'], 'complete_with_failures')
        self.assertEqual(state['failed_segments'], ['fw-i1-a'])
        self.assertFalse(published)

    def test_successful_batch_exits_zero_and_quarantines_candidate(self):
        result, state, published = self.run_fake_batch(True)
        self.assertEqual(result, 0)
        self.assertEqual(state['status'], 'complete')
        self.assertEqual(state['successes'][0]['segment_id'], 'fw-i1-a')
        self.assertEqual(state['review_status'], 'pending')
        self.assertFalse(published)


class AudioQualityTests(unittest.TestCase):
    def test_short_phrase_cannot_silently_produce_a_minute(self):
        with self.assertRaisesRegex(RuntimeError, '时长'):
            api.validate_group_audio('Oh!', 57.12, 0.01, 0.1)

    def test_nearly_dc_output_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, '直流'):
            api.validate_group_audio('Now to the obverse.', 3, -0.117, 0.118)

    def test_normal_duration_and_varying_signal_are_allowed(self):
        api.validate_group_audio('Now to the obverse.', 3, 0.001, 0.1)


class CheckpointCompatibilityTests(unittest.TestCase):
    def test_legacy_zip_v4_lora_uses_metadata_instead_of_file_size(self):
        checkpoint = {'config': {'model': {'version': 'v4'}}, 'lora_rank': 32,
                      'weight': {'cfm.base_model.model.estimator.attn.to_q.lora_A.default.weight': object()}}
        self.assertEqual(api.checkpoint_model_kind(checkpoint, ('v1', 'v1', False)), ('v2', 'v4', True))

    def test_ordinary_checkpoint_keeps_detector_result(self):
        self.assertEqual(api.checkpoint_model_kind({'config': {'model': {'version': 'v2'}}, 'weight': {}},
                                                  ('v2', 'v2', False)), ('v2', 'v2', False))

    def test_v4_without_lora_tensors_is_not_reclassified(self):
        checkpoint = {'config': {'model': {'version': 'v4'}}, 'lora_rank': 32, 'weight': {}}
        self.assertEqual(api.checkpoint_model_kind(checkpoint, ('v1', 'v1', False)), ('v1', 'v1', False))

    def test_pickled_hparams_config_is_supported(self):
        from types import SimpleNamespace
        checkpoint = {'config': SimpleNamespace(model=SimpleNamespace(version='v4')), 'lora_rank': 32,
                      'weight': {'cfm.estimator.attn.to_q.lora_A.default.weight': object()}}
        self.assertEqual(api.checkpoint_model_kind(checkpoint, ('v1', 'v1', False)), ('v2', 'v4', True))
