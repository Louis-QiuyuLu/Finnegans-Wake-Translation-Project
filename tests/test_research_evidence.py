"""Research tooling checks retrieval and collation, never scholarly truth."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / '.ai/skills/joyce-research/scripts/verify_evidence.py'


class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('verify_evidence', SCRIPT)
        cls.api = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.api)

    def capture(self, body, **kw):
        args = dict(status=200, requested_url='https://example.org/text',
                    effective_url='https://example.org/text', content_type='text/html',
                    needles=['see peegee'], body=body)
        args.update(kw)
        return self.api.capture(**args)

    def test_http_200_landing_page_is_not_passage_evidence(self):
        r = self.capture(b'<title>Finnegans Wake</title><p>Download book</p>',
                         effective_url='https://example.org/showbook')
        self.assertFalse(r['ok'])
        self.assertEqual(r['anchors'][0]['count'], 0)
        self.assertIn('sha256', r)

    def test_failed_http_is_not_accepted_even_with_anchor(self):
        self.assertFalse(self.capture(b'see peegee', status=403)['ok'])

    def test_script_anchor_does_not_count_as_visible_text(self):
        self.assertFalse(self.capture(b'<script>see peegee</script>')['ok'])

    def test_explicitly_hidden_anchor_does_not_count(self):
        self.assertFalse(self.capture(b'<p hidden><b>see peegee</b></p><p>book record</p>')['ok'])

    def test_capture_does_not_claim_reading_or_scholarship(self):
        r = self.capture(b'<p>see <b>peegee</b></p>')
        self.assertTrue(r['ok'])
        self.assertNotIn('read_state', r)
        self.assertNotIn('supported', str(r))

    def test_pdf_requires_page_inspection(self):
        self.assertFalse(self.capture(b'%PDF-1.4 see peegee', content_type='application/pdf')['ok'])

    def witness(self, text):
        return dict(text=text, basis='external_witness', source_id='test',
                    url='https://example.org/text', edition='test edition',
                    locator='008.21–008.22', capture_method='web_tool_cached_transcription')

    def test_comparison_normalizes_only_whitespace(self):
        self.assertTrue(self.api.compare('a\n b', self.witness('a b'))['ok'])
        self.assertFalse(self.api.compare('cafe', self.witness('café'))['ok'])
        self.assertFalse(self.api.compare('A—B', self.witness('A-B'))['ok'])

    def test_internal_hash_agreement_does_not_hide_inserted_text(self):
        r = self.api.compare('This is the first in the ditch.',
                             self.witness('This is the three lipoleum boyne grouching down in the living detch.'))
        self.assertFalse(r['ok'])
        self.assertIn('first', r['diff'])
        self.assertEqual(r['verdict'], 'text_mismatch')

    def test_missing_provenance_is_rejected(self):
        self.assertFalse(self.api.compare('same', {'text': 'same'})['ok'])

    def test_same_internal_copy_is_rejected_as_witness(self):
        w = self.witness('same'); w['basis'] = 'internal_workpack'
        self.assertFalse(self.api.compare('same', w)['ok'])

    def test_scope_anchors_must_be_unique_and_ordered(self):
        with self.assertRaises(ValueError):
            self.api.select_span('start end start end', 'start', 'end')
        with self.assertRaises(ValueError):
            self.api.select_span('end start', 'start', 'end')


if __name__ == '__main__':
    unittest.main()
