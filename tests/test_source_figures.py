"""Meaning-bearing rotated letters must survive reader and EPUB rendering."""
import importlib.util
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('project', ROOT / 'scripts/project.py')
project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(project)


class SourceFigureTests(unittest.TestCase):
    def test_inserts_rotated_e_without_changing_spoken_text(self):
        s = {'original': 'platterplate. Hum!', 'source_figures': [
            {'anchor': 'platterplate.', 'letter': 'E', 'rotation': -90, 'replace': False}]}
        html = project.source_paragraphs(s)
        self.assertIn('<svg', html)
        self.assertIn('rotate(-90', html)
        self.assertIn('Hum!', html)
        self.assertEqual(s['original'], 'platterplate. Hum!')

    def test_replaces_approximation_and_preserves_facing_pair_in_xhtml(self):
        s = {'original': '╖ace to ╙ace!', 'source_figures': [
            {'anchor': '╖', 'letter': 'F', 'rotation': 90, 'replace': True},
            {'anchor': '╙', 'letter': 'F', 'rotation': -90, 'replace': True}]}
        html = project.source_paragraphs(s)
        self.assertNotIn('╖', html)
        tree = ET.fromstring('<div>' + html + '</div>')
        self.assertEqual(len(tree.findall('.//{http://www.w3.org/2000/svg}svg')), 2)
        self.assertIn('F', project.source_plain_text(s))

    def test_figures_cannot_inject_markup_or_choose_ambiguous_anchors(self):
        for figure in [
                {'anchor': 'a', 'letter': '<script>', 'rotation': 90},
                {'anchor': 'a', 'letter': 'E', 'rotation': 45},
                {'anchor': 'aa', 'letter': 'E', 'rotation': 90}]:
            self.assertTrue(project.figure_errors({'original': 'a a', 'source_figures': [figure]}))


if __name__ == '__main__':
    unittest.main()
