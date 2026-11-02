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

    def run_fake_batch(self, child_success, source_queue=False, threads=None):
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
if '--threads' in args:
    (out.parent/'received-threads.txt').write_text(args[args.index('--threads')+1])
'''
            if not child_success:
                code = 'raise SystemExit(9)\n'
            (root / 'scripts/generate_audio.py').write_text(code)
            segments = [{'id': 'fw-i1-a', 'original': 'text', 'chapter': 'I.1'}]
            queue = None
            loader = lambda path, root: segments
            if source_queue:
                _, queue, segment, loader, _ = SourceQueueTests().source_fixture(root)
                segments = [segment]
                with (root / 'scripts/generate_audio.py').open('a') as script:
                    script.write("\nassert '--source-queue' in args\n")
                    script.write("(out.parent/'received-source-queue.txt').write_text(args[args.index('--source-queue')+1])\n")
            argv = ['audio_batch.py', '--run-dir', str(root / 'run'), '--device', 'cpu', '--attempts', '1']
            if source_queue:
                argv += ['--source-queue', str(queue)]
            if threads is not None:
                argv += ['--threads', str(threads)]
            with patch.object(sys, 'argv', argv), patch.object(batch, 'ROOT', root), \
                    patch.object(batch, 'AUDIO_DIR', root / 'audio'), \
                    patch.object(batch, 'book_one', return_value=[] if source_queue else segments), \
                    patch.object(batch, 'load_audio_segments', side_effect=lambda path: loader(path, root), create=True), \
                    patch.object(batch.time, 'sleep'), contextlib.redirect_stdout(io.StringIO()):
                # The queue uses its explicit destination; no real repo file is touched.
                result = batch.main()
            state = json.loads((root / 'run/state.json').read_text())
            received_threads = root / 'run/received-threads.txt'
            state['_received_threads'] = received_threads.read_text() if received_threads.exists() else None
            if source_queue:
                received = root / 'run/received-source-queue.txt'
                state['_received_source_queue'] = received.read_text() if received.exists() else None
            return result, state, (root / 'audio' / (segments[0]['id'] + '.mp3')).exists()

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


class NumericSamples(list):
    """Tiny ndarray stand-in; synthesis control-flow tests need no NumPy install."""
    def astype(self, dtype):
        return self

    def mean(self):
        return sum(self) / len(self)

    def __mul__(self, other):
        return NumericSamples(a * b for a, b in zip(self, other))


class PunctuationGroupTests(unittest.TestCase):
    def synthesize(self, groups):
        import contextlib
        import io
        import math
        from types import SimpleNamespace
        from unittest.mock import patch
        from scripts import joyce_phonetics

        class TTS:
            def __init__(self):
                self.calls = []

            def run(self, inputs):
                self.calls.append(inputs['text'])
                yield 48000, NumericSamples([1, -1])

        numpy = SimpleNamespace(
            zeros=lambda count, dtype: NumericSamples([0] * count),
            int16='int16', float64='float64',
            concatenate=lambda chunks: NumericSamples(item for chunk in chunks for item in chunk),
            mean=lambda values: sum(values) / len(values), sqrt=math.sqrt,
        )
        tts = TTS()
        with patch.dict('sys.modules', {'numpy': numpy}), \
                patch.object(joyce_phonetics, 'segment_into_sense_groups', return_value=groups), \
                contextlib.redirect_stdout(io.StringIO()):
            sr, samples = api.synthesize_segment(tts, 'test text', Path('reference.wav'), 'reference')
        return tts.calls, sr, samples

    def test_standalone_dash_keeps_its_pause_without_calling_tts(self):
        groups = [('Oh!', 0.12), ('—', 0.26), ('After.', 0.18)]
        calls, sr, samples = self.synthesize(groups)
        self.assertEqual(calls, ['Oh!', 'After.'])
        expected = int(sr * 0.06) + 4 + int(sr * 0.12) + int(sr * 0.26) + int(sr * 0.4)
        self.assertEqual(len(samples), expected)

    def test_punctuation_at_segment_end_keeps_final_pause_floor(self):
        calls, sr, samples = self.synthesize([('Word.', 0.12), ('—', 0.26)])
        self.assertEqual(calls, ['Word.'])
        self.assertEqual(len(samples), int(sr * 0.06) + 2 + int(sr * 0.12) + int(sr * 0.4))

    def test_letters_numbers_and_symbols_are_never_skipped(self):
        spoken = ['é', 'e\u0301', '—a—', '—９—', '2', 'Ⅳ', '×']
        calls, _, _ = self.synthesize([(text, 0.01) for text in spoken] + [('“— … !”', 0.26)])
        self.assertEqual(calls, spoken)

    def test_real_069_30_keeps_every_spoken_group_and_every_pause(self):
        from scripts.joyce_phonetics import segment_into_sense_groups
        chapter = json.loads((SCRIPT.parents[1] / 'manuscript/chapters/I-3.json').read_text())
        segment = next(s for s in chapter['segments'] if s['id'] == 'fw-i3-069-30')
        groups = segment_into_sense_groups(segment['original'])
        self.assertEqual(groups[57], ('—', 0.26))
        calls, sr, samples = self.synthesize(groups)
        self.assertEqual(calls, [text for i, (text, _) in enumerate(groups) if i != 57])
        expected = int(sr * 0.06) + 2 * len(calls)
        expected += sum(int(sr * (max(pause, 0.4) if i == len(groups) - 1 else pause))
                        for i, (_, pause) in enumerate(groups))
        self.assertEqual(len(samples), expected)


class SourceQueueTests(unittest.TestCase):
    def source_fixture(self, root):
        chapter = root / 'manuscript/chapters/II-1.json'
        chapter.parent.mkdir(parents=True)
        chapter.write_text(json.dumps({'id': 'II.1', 'segments': [],
                                      'source_text': {'html_sha256': 'initial-source'}}))
        original = 'Published source, without a Chinese draft.'
        segment = {'id': 'fw-ii1-219-01', 'chapter': 'II.1', 'locator': '219.01', 'original': original,
                   'source_binding': {'book': 'II', 'html_sha256': 'initial-source',
                                      'text_sha256': hashlib.sha256(original.encode()).hexdigest()}}
        queue = root / 'audio/source-queues/II.json'
        queue.parent.mkdir(parents=True)
        queue.write_text(json.dumps({'segments': [segment]}))
        calls = []

        def load_source_segments(queue_path, root):
            calls.append(Path(queue_path))
            items = json.loads(Path(queue_path).read_text())['segments']
            canonical = json.loads((Path(root) / 'manuscript/chapters/II-1.json').read_text())
            for item in items:
                if canonical['source_text']['html_sha256'] != item['source_binding']['html_sha256']:
                    raise RuntimeError('底本指纹已改变')
                if hashlib.sha256(item['original'].encode()).hexdigest() != item['source_binding']['text_sha256']:
                    raise RuntimeError('源段原文指纹已改变')
            return items

        return chapter, queue, segment, load_source_segments, calls

    def test_source_segment_can_be_selected_when_chinese_segments_are_empty(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            _, queue, segment, loader, calls = self.source_fixture(root)
            with patch.object(api, 'ROOT', root), \
                    patch.dict('sys.modules', {'scripts.audio_source': SimpleNamespace(load_source_segments=loader)}):
                self.assertEqual(api.load_segments(), [])
                self.assertEqual(api.load_audio_segments(queue), [segment])
            self.assertEqual(calls, [queue])

    def test_publish_reloads_queue_and_rejects_changed_source_even_with_startup_list(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            chapter, queue, segment, loader, calls = self.source_fixture(root)
            output = root / 'candidates'
            output.mkdir()
            previous = output / (segment['id'] + '.mp3')
            previous.write_bytes(b'old audio')
            candidate = output / 'candidate.mp3'
            candidate.write_bytes(b'new audio')
            with patch.object(api, 'ROOT', root), \
                    patch.dict('sys.modules', {'scripts.audio_source': SimpleNamespace(load_source_segments=loader)}):
                startup = api.load_audio_segments(queue)
                data = json.loads(chapter.read_text())
                data['source_text']['html_sha256'] = 'changed-source'
                chapter.write_text(json.dumps(data))
                with self.assertRaisesRegex(RuntimeError, '底本'):
                    api.publish_audio(segment, candidate, output, current_segments=startup, source_queue=queue)
            self.assertEqual(previous.read_bytes(), b'old audio')
            self.assertTrue(candidate.exists())
            self.assertEqual(len(calls), 2)

    def test_freeze_rejects_changed_source_binding_even_when_text_matches(self):
        from copy import deepcopy
        batch = AudioBatchTests().batch()
        frozen = [{'id': 'source-a', 'original': 'same words', 'source_binding': {'html_sha256': 'old'}}]
        current = deepcopy(frozen)
        current[0]['source_binding']['html_sha256'] = 'new'
        with self.assertRaisesRegex(RuntimeError, '原文'):
            batch.check_originals(frozen, current)

    def test_batch_passes_queue_to_child_and_preserves_binding(self):
        result, state, published = AudioBatchTests().run_fake_batch(True, source_queue=True)
        self.assertEqual(result, 0)
        self.assertIsNotNone(state['_received_source_queue'])
        self.assertTrue(state['_received_source_queue'].endswith('/audio/source-queues/II.json'))
        self.assertEqual(state['successes'][0]['segment_id'], 'fw-ii1-219-01')
        self.assertEqual(state['successes'][0]['source_binding']['html_sha256'], 'initial-source')
        self.assertFalse(published)

    def run_source_generator(self, changed_source=False, wrong_hash=False, threads=None):
        import contextlib
        import io
        import sys
        from types import SimpleNamespace
        from unittest.mock import patch
        from scripts import joyce_phonetics
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            chapter, queue, segment, loader, calls = self.source_fixture(root)
            model = root / 'model'
            (model / 'references').mkdir(parents=True)
            for name in ('tts.ckpt', 'vits.pth', 'references/e1.wav', 'references/e1.txt'):
                (model / name).write_bytes(b'test asset')
            output = root / 'candidates'
            output.mkdir()
            previous = output / (segment['id'] + '.mp3')
            previous.write_bytes(b'old audio')
            configs = SimpleNamespace(device='cpu', version='v4',
                                      t2s_weights_path=str(model / 'tts.ckpt'),
                                      vits_weights_path=str(model / 'vits.pth'))
            synthesized = []

            def synthesize(tts, original, *args, **kwargs):
                synthesized.append(original)
                if changed_source:
                    data = json.loads(chapter.read_text())
                    data['source_text']['html_sha256'] = 'changed-source'
                    chapter.write_text(json.dumps(data))
                return 48000, NumericSamples([1, -1])

            def ffmpeg(command, **kwargs):
                Path(command[-1]).write_bytes(b'new audio')

            argv = ['generate_audio.py', '--source-queue', str(queue), '--segment', segment['id'],
                    '--model', 'vertin', '--ref', 'e1', '--audio-dir', str(output),
                    '--expected-original-sha256', 'wrong' if wrong_hash else api.original_hash(segment)]
            if threads is not None:
                argv += ['--threads', str(threads)]
            error = None
            with patch.object(sys, 'argv', argv), patch.object(api, 'ROOT', root), \
                    patch.dict('sys.modules', {'scripts.audio_source': SimpleNamespace(load_source_segments=loader),
                                               'soundfile': SimpleNamespace(write=lambda *args: None)}), \
                    patch.object(api, 'find_model_dir', return_value=model), \
                    patch.object(joyce_phonetics, 'update_engdict_hot'), \
                    patch.object(api, 'init_tts_pipeline', return_value=SimpleNamespace(configs=configs)) as initialize, \
                    patch.object(api, 'synthesize_segment', side_effect=synthesize), \
                    patch.object(api.subprocess, 'run', side_effect=ffmpeg), \
                    contextlib.redirect_stdout(io.StringIO()):
                try:
                    api.main()
                except RuntimeError as caught:
                    error = str(caught)
            provenance = output / (segment['id'] + '.provenance.json')
            return {'error': error, 'calls': len(calls), 'synthesized': synthesized,
                    'initialized_threads': initialize.call_args.kwargs.get('threads') if initialize.called else None,
                    'audio': previous.read_bytes(), 'indexed': (output / 'index.json').exists(),
                    'provenance': json.loads(provenance.read_text()) if provenance.exists() else None,
                    'source_binding': segment['source_binding']}

    def test_generator_selects_source_and_writes_its_binding_to_provenance(self):
        result = self.run_source_generator()
        self.assertIsNone(result['error'])
        self.assertEqual(result['synthesized'], ['Published source, without a Chinese draft.'])
        self.assertEqual(result['calls'], 2)
        self.assertEqual(result['audio'], b'new audio')
        self.assertTrue(result['indexed'])
        self.assertEqual(result['provenance']['source_binding'], result['source_binding'])
        self.assertTrue(result['provenance']['source_queue'].endswith('/audio/source-queues/II.json'))

    def test_generator_rechecks_source_after_synthesis_and_preserves_previous_audio(self):
        result = self.run_source_generator(changed_source=True)
        self.assertIn('底本', result['error'])
        self.assertEqual(result['calls'], 2)
        self.assertEqual(result['audio'], b'old audio')
        self.assertFalse(result['indexed'])

    def test_generator_rejects_expected_hash_before_any_synthesis(self):
        result = self.run_source_generator(wrong_hash=True)
        self.assertIn('原文', result['error'])
        self.assertEqual(result['synthesized'], [])
        self.assertEqual(result['audio'], b'old audio')


class RealSourceQueueTests(unittest.TestCase):
    def copy_book_ii(self, root):
        import shutil
        source = SCRIPT.parents[1]
        chapter_dir = root / 'manuscript/chapters'
        chapter_dir.mkdir(parents=True)
        for path in sorted((source / 'manuscript/chapters').glob('II-*.json')):
            chapter = json.loads(path.read_text())
            chapter['segments'] = []
            (chapter_dir / path.name).write_text(json.dumps(chapter, ensure_ascii=False))
        queue = root / 'audio/source-queues/II.json'
        queue.parent.mkdir(parents=True)
        shutil.copy2(source / 'audio/source-queues/II.json', queue)
        return queue

    def test_real_ii_source_queue_loads_with_no_chinese_segments(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            queue = self.copy_book_ii(root)
            expected = json.loads(queue.read_text())
            with patch.object(api, 'ROOT', root):
                self.assertEqual(api.load_segments(), [])
                segments = api.load_audio_segments(queue)
            self.assertEqual(len(segments), expected['statistics']['items'])
            self.assertEqual([s['id'] for s in segments], [s['id'] for s in expected['items']])
            self.assertTrue(all(api.original_hash(s) == s['source_binding']['original_sha256'] for s in segments))

    def test_real_ii_source_is_reloaded_before_publication(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            queue = self.copy_book_ii(root)
            output = root / 'candidates'
            output.mkdir()
            with patch.object(api, 'ROOT', root):
                startup = api.load_audio_segments(queue)
                segment = startup[0]
                previous = output / (segment['id'] + '.mp3')
                previous.write_bytes(b'old audio')
                candidate = output / 'candidate.mp3'
                candidate.write_bytes(b'new audio')
                chapter_path = root / 'manuscript/chapters/II-1.json'
                chapter = json.loads(chapter_path.read_text())
                chapter['source_text']['html'] += '\n'
                chapter['source_text']['html_sha256'] = hashlib.sha256(chapter['source_text']['html'].encode()).hexdigest()
                chapter_path.write_text(json.dumps(chapter, ensure_ascii=False))
                with self.assertRaisesRegex(ValueError, 'source'):
                    api.publish_audio(segment, candidate, output, current_segments=startup, source_queue=queue)
            self.assertEqual(previous.read_bytes(), b'old audio')
            self.assertTrue(candidate.exists())
            self.assertFalse((output / 'index.json').exists())


class SourceQueueIsolationTests(unittest.TestCase):
    def test_cli_refuses_default_or_explicit_formal_directory_before_model_setup(self):
        import contextlib
        import io
        import sys
        from unittest.mock import patch
        from scripts import joyce_phonetics
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            _, queue, _, _, _ = SourceQueueTests().source_fixture(root)
            formal = root / 'audio'
            index = formal / 'index.json'
            index.write_bytes(b'{"tracks": []}\n')
            before = index.read_bytes()
            alias = root / 'formal-link'
            alias.symlink_to(formal, target_is_directory=True)
            for extra in ([], ['--audio-dir', str(formal)], ['--audio-dir', str(alias)]):
                with self.subTest(arguments=extra):
                    stderr = io.StringIO()
                    argv = ['generate_audio.py', '--source-queue', str(queue)] + extra
                    with patch.object(sys, 'argv', argv), patch.object(api, 'AUDIO_DIR', formal), \
                            patch.object(api, 'find_model_dir', side_effect=AssertionError('model setup must not run')) as find_model, \
                            patch.object(api, 'init_tts_pipeline') as initialize, \
                            patch.object(joyce_phonetics, 'update_engdict_hot') as dictionary, \
                            contextlib.redirect_stderr(stderr):
                        with self.assertRaises(SystemExit) as error:
                            api.main()
                    self.assertEqual(error.exception.code, 2)
                    self.assertIn('--audio-dir', stderr.getvalue())
                    self.assertIn('隔离', stderr.getvalue())
                    find_model.assert_not_called()
                    initialize.assert_not_called()
                    dictionary.assert_not_called()
                    self.assertEqual(index.read_bytes(), before)
                    self.assertFalse((formal / '.index.lock').exists())

    def test_publish_cannot_bypass_source_queue_isolation(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            _, queue, segment, _, _ = SourceQueueTests().source_fixture(root)
            formal = root / 'audio'
            index = formal / 'index.json'
            index.write_bytes(b'{"tracks": []}\n')
            previous = formal / (segment['id'] + '.mp3')
            previous.write_bytes(b'old audio')
            candidate = root / 'candidate.mp3'
            candidate.write_bytes(b'new audio')
            alias = root / 'formal-link'
            alias.symlink_to(formal, target_is_directory=True)
            for destination in (formal, alias):
                index.write_bytes(b'{"tracks": []}\n')
                previous.write_bytes(b'old audio')
                candidate.write_bytes(b'new audio')
                with self.subTest(destination=destination):
                    with patch.object(api, 'AUDIO_DIR', formal), \
                            patch.object(api, 'load_audio_segments', return_value=[segment]) as loader:
                        with self.assertRaisesRegex(ValueError, '隔离'):
                            api.publish_audio(segment, candidate, destination, source_queue=queue)
                    loader.assert_not_called()
                    self.assertEqual(index.read_bytes(), b'{"tracks": []}\n')
                    self.assertEqual(previous.read_bytes(), b'old audio')
                    self.assertEqual(candidate.read_bytes(), b'new audio')
                    self.assertFalse((formal / '.index.lock').exists())


class BatchLockScopeTests(unittest.TestCase):
    def test_distinct_books_and_legacy_book_can_hold_locks_together(self):
        batch = AudioBatchTests().batch()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            handles = []
            try:
                handles.append(batch.acquire_batch_lock(root))
                handles.append(batch.acquire_batch_lock(root, [{'source_binding': {'book': 'II'}}]))
                handles.append(batch.acquire_batch_lock(root, [{'source_binding': {'book': 'III'}}]))
                handles.append(batch.acquire_batch_lock(root, [{'source_binding': {'book': 'IV'}}]))
                self.assertEqual([Path(h.name).name for h in handles],
                                 ['.batch.lock', '.source-II.lock', '.source-III.lock', '.source-IV.lock'])
            finally:
                for handle in handles:
                    handle.close()

    def test_same_book_refuses_a_second_lock(self):
        batch = AudioBatchTests().batch()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            segments = [{'source_binding': {'book': 'II'}}]
            first = batch.acquire_batch_lock(root, segments)
            try:
                with self.assertRaises(SystemExit):
                    batch.acquire_batch_lock(root, segments)
            finally:
                first.close()
            batch.acquire_batch_lock(root, segments).close()

    def test_invalid_or_mixed_book_never_becomes_a_lock_path(self):
        batch = AudioBatchTests().batch()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            cases = [[], [{'source_binding': {'book': '../outside'}}],
                     [{'source_binding': {'book': 'II'}}, {'source_binding': {'book': 'III'}}]]
            for segments in cases:
                with self.subTest(segments=segments), self.assertRaises(ValueError):
                    batch.acquire_batch_lock(root, segments)
            self.assertEqual(list(root.iterdir()), [])

    def test_queue_is_validated_before_a_source_lock_is_created(self):
        import sys
        from unittest.mock import patch
        batch = AudioBatchTests().batch()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            argv = ['audio_batch.py', '--run-dir', str(root / 'run'), '--source-queue', str(root / 'invalid.json')]
            with patch.object(sys, 'argv', argv), patch.object(batch, 'AUDIO_DIR', root / 'audio'), \
                    patch.object(batch, 'load_audio_segments', side_effect=ValueError('source changed')):
                with self.assertRaisesRegex(ValueError, 'source changed'):
                    batch.main()
            self.assertEqual(list((root / 'audio').glob('*.lock')), [])
            self.assertFalse((root / 'audio/.batch.lock').exists())


class ThreadConfigurationTests(unittest.TestCase):
    def test_batch_defaults_to_eight_threads_and_passes_two_when_requested(self):
        result, state, _ = AudioBatchTests().run_fake_batch(True)
        self.assertEqual(result, 0)
        self.assertEqual(state['parameters']['threads'], 8)
        self.assertEqual(state['_received_threads'], '8')
        result, state, _ = AudioBatchTests().run_fake_batch(True, source_queue=True, threads=2)
        self.assertEqual(result, 0)
        self.assertEqual(state['parameters']['threads'], 2)
        self.assertEqual(state['_received_threads'], '2')
        self.assertTrue(state['lock_file'].endswith('/audio/.source-II.lock'))

    def test_generator_records_default_and_explicit_threads(self):
        for requested, expected in ((None, 8), (2, 2)):
            with self.subTest(threads=requested):
                result = SourceQueueTests().run_source_generator(threads=requested)
                self.assertIsNone(result['error'])
                self.assertEqual(result['initialized_threads'], expected)
                self.assertEqual(result['provenance']['parameters']['threads'], expected)

    def test_pipeline_sets_actual_torch_thread_count(self):
        import contextlib
        import io
        from types import SimpleNamespace
        from unittest.mock import Mock, patch
        for requested in (8, 2):
            with self.subTest(threads=requested):
                torch = SimpleNamespace(set_num_threads=Mock())
                module = SimpleNamespace(
                    TTS_Config=lambda data: SimpleNamespace(**data['custom']),
                    TTS=lambda config: SimpleNamespace(configs=config),
                    get_sovits_version_from_path_fast=lambda path: ('v2', 'v2', False),
                )
                checkpoint = SimpleNamespace(load_sovits_new=lambda path: {'config': {}, 'weight': {}})
                modules = {'torch': torch, 'GPT_SoVITS.TTS_infer_pack.TTS': module, 'process_ckpt': checkpoint}
                with patch.dict('sys.modules', modules), patch.object(api.os, 'chdir'), \
                        contextlib.redirect_stdout(io.StringIO()):
                    if requested == 8:
                        api.init_tts_pipeline(Path('/test/model'))
                    else:
                        api.init_tts_pipeline(Path('/test/model'), threads=requested)
                torch.set_num_threads.assert_called_once_with(requested)

    def test_cli_rejects_nonpositive_or_noninteger_threads_before_model_or_lock(self):
        import contextlib
        import io
        import sys
        from unittest.mock import patch
        batch = AudioBatchTests().batch()
        for value in ('0', '-2', '1.5', 'bad'):
            with self.subTest(threads=value):
                with tempfile.TemporaryDirectory() as folder:
                    root = Path(folder)
                    with patch.object(sys, 'argv', ['generate_audio.py', '--threads', value]), \
                            patch.object(api, 'find_model_dir') as model, contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as error:
                            api.main()
                    self.assertEqual(error.exception.code, 2)
                    model.assert_not_called()
                    argv = ['audio_batch.py', '--run-dir', str(root / 'run'), '--threads', value]
                    with patch.object(sys, 'argv', argv), patch.object(batch, 'AUDIO_DIR', root / 'audio'), \
                            contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as error:
                            batch.main()
                    self.assertEqual(error.exception.code, 2)
                    self.assertFalse((root / 'audio/.batch.lock').exists())
