"""Full English witnesses must not advance Chinese translation progress."""
import copy
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

from test_project import sample

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


source = load('fw_source_text_test', ROOT / 'scripts/source_text.py')
project = load('fw_project_source_test', ROOT / 'scripts/project.py')

HTML = """<html><body><p>Publisher front matter.</p>
<div class='pagenumber'>----- 3 -----</div>
<p class='pindent'>riverrun &amp; return<br />across the page
<div class='pagenumber'>----- 4 -----</div>
<aside class='sl'>Left note.</aside><p>second page
<a id='FNanchor_4_1'></a><a href='#Footnote_4_1'>1</a></p>
<div class='footnote'><p><a id='Footnote_4_1'></a>Author's footnote.
<a href='#FNanchor_4_1'>return</a></p></div>
<div class='pagenumber'>----- 5 -----</div><p>Next chapter.</p>
</body></html>"""


class FullSourceTests(unittest.TestCase):
    def api(self):
        self.assertIsNotNone(source, 'Full English source importer is not implemented')
        return source

    def chapter(self):
        chapter = sample()['chapters'][0]
        chapter.update(pages=[3, 4], coverage='not_started', segments=[])
        chapter['source_text'] = self.api().extract_chapters(HTML, [chapter], source_id='text')['I.1']
        return chapter

    def test_import_preserves_words_notes_links_and_unclosed_paragraphs(self):
        chapter = self.chapter()
        witness = chapter['source_text']
        self.assertEqual(witness['pages'], [3, 4])
        fragment = witness['html']
        ET.fromstring('<div>' + fragment + '</div>')
        self.assertIn('riverrun &amp; return', fragment)
        self.assertIn('Left note.', fragment)
        self.assertIn("Author's footnote.", self.api().text_content(fragment))
        self.assertIn('href="#source-Footnote_4_1"', fragment)
        self.assertIn('id="source-Footnote_4_1"', fragment)
        self.assertNotIn('Publisher front matter', fragment)
        self.assertNotIn('Next chapter', fragment)

    def test_literal_text_outside_tags_survives_xhtml_serialization(self):
        fragment = self.api().sanitize_fragment('A &amp; B <p>déjà vu</p>')
        ET.fromstring('<div>' + fragment + '</div>')
        self.assertEqual(self.api().text_content(fragment), 'A & B déjà vu')

    def test_markdown_retains_a_readable_score_image(self):
        chapter = self.chapter()
        chapter['source_text']['html'] += '<p><img src="images/persseoreilly.jpg" alt="musical score" /></p>'
        markdown = self.api().markdown(chapter['source_text'])
        self.assertIn('![musical score](../manuscript/source-assets/persseoreilly.jpg)', markdown)

    def test_import_rejects_a_missing_printed_page(self):
        chapter = sample()['chapters'][0]
        chapter['pages'] = [3, 4]
        with self.assertRaisesRegex(ValueError, 'missing.*4'):
            self.api().extract_chapters(HTML.replace('----- 4 -----', 'not a page'), [chapter])

    def test_source_markup_cannot_run_scripts_or_load_external_images(self):
        api = self.api()
        for bad in ['<script>alert(1)</script>', '<img src="https://example.org/pixel.png" />',
                    '<p onclick="alert(1)">text</p>', '<a href="javascript:alert(1)">x</a>']:
            with self.assertRaises(ValueError):
                api.sanitize_fragment(bad)

    def test_english_only_import_does_not_count_as_translated(self):
        chapter = self.chapter()
        data = sample()
        data['chapters'] = [chapter]
        self.assertEqual(project.validate(data), [])
        self.assertEqual(project.statistics(data)['segments'], 0)
        self.assertEqual(project.statistics(data)['complete'], 0)
        stats = getattr(project, 'source_statistics', None)
        self.assertTrue(callable(stats), 'English coverage needs separate statistics')
        self.assertEqual(stats(data), {'chapters': 1, 'pages': 2})

    def test_reader_and_epub_show_the_full_witness_without_fake_translation(self):
        chapter = self.chapter()
        data = sample()
        data['chapters'] = [chapter]
        render = getattr(project, 'render_source_text', None)
        self.assertTrue(callable(render), 'Full English source is not rendered')
        html = render(chapter, data)
        self.assertIn('source-page-003', html)
        self.assertIn('second page', html)
        self.assertIn('英文原文', html)
        self.assertNotIn('edit-translation', html)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'book.epub'
            project.build_epub(data, path)
            with zipfile.ZipFile(path) as book:
                body = book.read('EPUB/chapters/I-1.xhtml').decode()
                self.assertIn('second page', body)
                self.assertIn('source-Footnote_4_1', body)

    def test_source_text_change_invalidates_its_import_fingerprint(self):
        chapter = self.chapter()
        chapter['source_text']['html'] = chapter['source_text']['html'].replace('riverrun', 'invented')
        data = sample()
        data['chapters'] = [chapter]
        self.assertTrue(any('source text' in e and 'hash' in e for e in project.validate(data)))


if __name__ == '__main__':
    unittest.main()
