"""English-only audio preparation must not invent translated segments."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import source_text


def api():
    path = ROOT / 'scripts/audio_source.py'
    if not path.exists():
        raise AssertionError('source-only audio preparation is not implemented')
    spec = importlib.util.spec_from_file_location('audio_source_test', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def chapter():
    html = '''<div class="pagenumber">----- 260 -----</div>
<aside class="sr">Right words.</aside><p>Main one<a href="#Footnote_260_1" class="fnanchor">1</a>.</p>
<aside class="sl">Left words.</aside><p>Main two.</p>
<div class="footnote"><p><a id="Footnote_260_1" /><a class="fnanchor" href="#FNanchor_260_1">1</a>Footnote words.</p></div>
<p><img src="images/geometricdiagram.jpg" alt="geometry" /></p>
<div class="pagenumber">----- 261 -----</div><p>Last page.</p>'''
    html = source_text.sanitize_fragment(html)
    return {'id': 'II.2', 'book': 'II', 'pages': [260, 261],
            'coverage': 'not_started', 'segments': [],
            'source_text': {'source_id': 'joyce-fp', 'pages': [260, 261],
                            'html': html, 'html_sha256': source_text.fingerprint(html),
                            'text_sha256': source_text.text_fingerprint(html)}}


class AudioSourceTests(unittest.TestCase):
    def test_page_order_keeps_main_notes_and_figure_inventory(self):
        module = api()
        parts, figures = module.page_tracks(chapter())
        self.assertEqual([(p['page'], p['role'], p['text']) for p in parts], [
            (260, 'main', 'Main one. Main two.'),
            (260, 'left', 'Left words.'), (260, 'right', 'Right words.'),
            (260, 'footnotes', '1Footnote words.'), (261, 'main', 'Last page.')])
        self.assertEqual(figures[0]['page'], 260)
        self.assertEqual(figures[0]['asset'], 'geometricdiagram.jpg')

    def test_chunk_boundaries_preserve_every_word_once(self):
        module = api()
        c = chapter()
        queue = module.prepare_queue([c], 'II', max_words=2)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'manuscript/chapters').mkdir(parents=True)
            (root / 'manuscript/chapters/II-2.json').write_text(json.dumps(c))
            path = root / 'queue.json'; path.write_text(json.dumps(queue))
            segments = module.load_source_segments(path, root)
        self.assertTrue(all(len(s['original'].split()) <= 2 for s in segments))
        self.assertEqual(' '.join(s['original'] for s in segments),
                         'Main one. Main two. Left words. Right words. 1Footnote words. Last page.')
        self.assertEqual(c['segments'], [])
        self.assertEqual(c['coverage'], 'not_started')
        self.assertTrue(all(s['id'].startswith('fw-source-ii2-') for s in segments))

    def test_source_drift_and_queue_tampering_are_rejected(self):
        module = api(); c = chapter(); queue = module.prepare_queue([c], 'II')
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); (root / 'manuscript/chapters').mkdir(parents=True)
            cp = root / 'manuscript/chapters/II-2.json'; cp.write_text(json.dumps(c))
            path = root / 'queue.json'; path.write_text(json.dumps(queue))
            changed = copy.deepcopy(c); changed['source_text']['html'] += '<p>Extra.</p>'
            cp.write_text(json.dumps(changed))
            with self.assertRaisesRegex(ValueError, 'source'):
                module.load_source_segments(path, root)
            cp.write_text(json.dumps(c))
            bad = copy.deepcopy(queue); bad['items'][0]['end'] -= 1
            path.write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                module.load_source_segments(path, root)

    def test_missing_or_reordered_chunk_is_not_silent_coverage(self):
        module = api(); c = chapter(); queue = module.prepare_queue([c], 'II', 2)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); (root / 'manuscript/chapters').mkdir(parents=True)
            (root / 'manuscript/chapters/II-2.json').write_text(json.dumps(c))
            path = root / 'queue.json'
            for items in [queue['items'][1:], list(reversed(queue['items']))]:
                bad = copy.deepcopy(queue); bad['items'] = items; path.write_text(json.dumps(bad))
                with self.assertRaises(ValueError):
                    module.load_source_segments(path, root)

    def test_translation_changes_do_not_invalidate_english_jobs(self):
        module = api(); c = chapter(); queue = module.prepare_queue([c], 'II')
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); (root / 'manuscript/chapters').mkdir(parents=True)
            cp = root / 'manuscript/chapters/II-2.json'; cp.write_text(json.dumps(c))
            path = root / 'queue.json'; path.write_text(json.dumps(queue))
            before = module.load_source_segments(path, root)
            c['segments'] = [{'translation': '后来补入的中文'}]
            c['coverage'] = 'partial'; cp.write_text(json.dumps(c))
            self.assertEqual(module.load_source_segments(path, root), before)


if __name__ == '__main__':
    unittest.main()
