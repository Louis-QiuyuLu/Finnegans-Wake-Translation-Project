"""Behavioral checks for editorial data and exported reader artifacts."""

import copy
import importlib.util
import json
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def sample():
    return {
        "config": {"title": "试译", "original_title": "Finnegans Wake", "author": "James Joyce", "repository": "https://github.com/example/book", "version": "0.1.0", "date": "2026-10-31"},
        "sources": [{"id": "text", "title": "底本", "url": "https://example.org/text", "type": "primary", "accessed": "2026-10-31"}],
        "glossary": [],
        "chapters": [{"id": "I.1", "book": "I", "number": 1, "pages": [3, 29], "title": "第一卷·第一章", "coverage": "partial", "segments": [{"id": "fw-i1-003-01", "locator": "003.01–003.03", "range": [3, 1, 3, 3], "source_id": "text", "original": "riverrun, past Eve and Adam's", "draft": "河流流过", "translation": "河流，流过夏娃与亚当", "status": "draft", "reviewers": [], "notes": [{"id": "n-river", "lemma": "riverrun", "kind": "wordplay", "certainty": "proposal", "text": "保留流动语感。", "source_ids": ["text"]}], "alternatives": []}]}],
    }


class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / "scripts" / "project.py"
        if not path.exists():
            cls.api = None
            return
        spec = importlib.util.spec_from_file_location("project", path)
        cls.api = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.api)

    def api_ready(self):
        self.assertIsNotNone(self.api, "构建工具尚未实现")
        return self.api

    def test_valid_sample_is_accepted(self):
        self.assertEqual(self.api_ready().validate(sample()), [])

    def test_epub_declares_embedded_source_figures(self):
        data = sample()
        data['chapters'][0]['segments'][0]['source_figures'] = [
            {'anchor': 'riverrun', 'letter': 'E', 'rotation': -90, 'replace': False}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'figures.epub'
            self.api_ready().build_epub(data, path)
            with zipfile.ZipFile(path) as book:
                root = ET.fromstring(book.read('EPUB/package.opf'))
                item = next(e for e in root.iter() if e.get('href') == 'chapters/I-1.xhtml')
                self.assertIn('svg', item.get('properties', '').split())
                self.assertIn(b'<svg', book.read('EPUB/chapters/I-1.xhtml'))

    def test_duplicate_segment_id_is_rejected(self):
        data = sample()
        data["chapters"][0]["segments"].append(copy.deepcopy(data["chapters"][0]["segments"][0]))
        self.assertTrue(any("duplicate segment" in e for e in self.api_ready().validate(data)))

    def test_note_requires_resolvable_source(self):
        data = sample()
        data["chapters"][0]["segments"][0]["notes"][0]["source_ids"] = ["missing"]
        self.assertTrue(any("unknown source" in e for e in self.api_ready().validate(data)))

    def test_page_outside_chapter_is_rejected(self):
        data = sample()
        data["chapters"][0]["segments"][0]["range"] = [30, 1, 30, 2]
        self.assertTrue(any("outside chapter" in e for e in self.api_ready().validate(data)))

    def test_reviewed_status_requires_named_reviewer(self):
        data = sample()
        data["chapters"][0]["segments"][0]["status"] = "reviewed"
        self.assertTrue(any("reviewer" in e for e in self.api_ready().validate(data)))

    def test_partial_chapter_is_not_counted_as_complete(self):
        stats = self.api_ready().statistics(sample())
        self.assertEqual(stats, {"chapters": 1, "started": 1, "complete": 0, "segments": 1, "reviewed": 0, "notes": 1})

    def test_checkpoint_rejects_cursor_before_latest_sequential_segment(self):
        data = sample()
        data["checkpoint"] = {"chapter": "I.1", "next": [3, 2], "next_original": "next", "notes": [], "updated": "2026-10-31"}
        self.assertTrue(any("checkpoint" in e for e in self.api_ready().validate(data)))

    def test_checkpoint_records_next_anchor_without_counting_end_sample(self):
        data = sample()
        data["checkpoint"] = {"chapter": "I.1", "next": [3, 4], "next_original": "Sir Tristram", "notes": ["回查双关"], "updated": "2026-10-31"}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "manuscript/chapters").mkdir(parents=True)
            (root / "progress").mkdir()
            self.api_ready().generate_views(data, root)
            resume = (root / "progress/RESUME.md").read_text()
            self.assertIn("003.04", resume)
            self.assertIn("Sir Tristram", resume)
            record = json.loads((root / "progress/chapters/I-1.json").read_text())
            self.assertEqual(record["last_segment"], "fw-i1-003-01")
            self.assertEqual(record["state"], "in_progress")

    def completed_translation(self):
        data = sample()
        chapters = []
        for cid, (pstart, pend) in self.api_ready().CANONICAL_CHAPTERS:
            c = {
                "id": cid,
                "book": cid.split(".")[0],
                "number": int(cid.split(".")[1]) if "." in cid else 1,
                "pages": [pstart, pend],
                "title": f"第{cid}章",
                "coverage": "complete",
                "coverage_review": "unit fixture",
                "segments": [{
                    "id": f"fw-{cid.lower().replace('.', '')}-{pstart:03d}-01",
                    "locator": f"{pstart:03d}.01–{pend:03d}.16" if cid == "IV" else f"{pstart:03d}.01–{pend:03d}.36",
                    "range": [pstart, 1, pend, 16] if cid == "IV" else [pstart, 1, pend, 36],
                    "source_id": "text",
                    "original": "riverrun, past Eve and Adam's" if cid == "I.1" else f"text {cid}",
                    "draft": "草稿",
                    "translation": "译文",
                    "status": "draft",
                    "reviewers": [],
                    "notes": [],
                    "alternatives": []
                }]
            }
            chapters.append(c)
        data["chapters"] = chapters
        data["checkpoint"] = {"chapter": "IV", "translation_complete": True,
                              "cycle_original": chapters[0]["segments"][0]["original"], "notes": ["待人工终审"], "updated": "2026-11-05"}
        return data

    def test_completed_translation_has_no_fictitious_next_line(self):
        data = self.completed_translation()
        self.assertEqual(self.api_ready().validate(data), [])
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "manuscript/chapters").mkdir(parents=True)
            (root / "progress").mkdir()
            self.api_ready().generate_views(data, root)
            resume = (root / "progress/RESUME.md").read_text()
            self.assertIn("顺序译稿已录至", resume)
            self.assertIn("628.16", resume)
            self.assertIn("待人工终审", resume)
            self.assertNotIn("下一段从", resume)
            record = json.loads((root / "progress/chapters/IV.json").read_text())
            self.assertTrue(record["translation_complete"])
            self.assertNotIn("next", record)

    def test_completed_translation_rejects_missing_chapter_coverage(self):
        data = self.completed_translation()
        data["chapters"][0]["coverage"] = "partial"
        self.assertTrue(any("checkpoint" in e for e in self.api_ready().validate(data)))

    def test_completed_translation_rejects_conflicting_next_anchor(self):
        data = self.completed_translation()
        data["checkpoint"].update(next=[628, 17], next_original="riverrun")
        self.assertTrue(any("checkpoint" in e for e in self.api_ready().validate(data)))

    def test_audio_manifest_only_publishes_registered_tracks(self):
        import hashlib
        from unittest.mock import patch
        data = sample()
        segment = data["chapters"][0]["segments"][0]
        data["audio"] = [{"segment_id":segment["id"], "file":segment["id"]+".mp3", "original_sha256":hashlib.sha256(segment["original"].encode()).hexdigest()}]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/"audio").mkdir()
            (root/"audio"/data["audio"][0]["file"]).write_bytes(b"test-mp3")
            (root/"audio"/"test_mastered.mp3").write_bytes(b"not-a-reader-track")
            with patch.object(self.api_ready(), "ROOT", root):
                # Source assets stay in the real project; the manifest helper owns audio copying.
                self.api_ready().publish_audio(data, root/"out")
            self.assertTrue((root/"out"/data["audio"][0]["file"]).exists())
            self.assertFalse((root/"out"/"test_mastered.mp3").exists())
            html = self.api_ready().render_segments(data["chapters"][0],data)
            self.assertIn('<audio controls preload="none"',html)
            self.assertIn('../assets/audio/'+segment["id"]+'.mp3',html)
            self.assertNotIn('<audio',self.api_ready().render_segments(data["chapters"][0],data,epub=True))
            self.assertNotIn('<audio',self.api_ready().render_segments(sample()["chapters"][0],sample()))

    def test_audio_for_a_changed_original_is_rejected(self):
        data = sample()
        data["audio"] = [{"segment_id":"fw-i1-003-01", "file":"fw-i1-003-01.mp3", "original_sha256":"0"*64}]
        self.assertTrue(any("audio" in error for error in self.api_ready().validate(data)))

    def test_missing_registered_audio_fails_instead_of_publishing_a_broken_player(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            with patch.object(self.api_ready(), "ROOT", root):
                with self.assertRaisesRegex(ValueError,"audio"):
                    self.api_ready().publish_audio({"audio":[{"segment_id":"fw-i1-003-01","file":"fw-i1-003-01.mp3"}]},root/"out")

    def test_markup_is_escaped_in_reader(self):
        data = sample()
        data["chapters"][0]["segments"][0]["translation"] = '<script>alert("x")</script>'
        with tempfile.TemporaryDirectory() as folder:
            self.api_ready().build(data, Path(folder))
            html = (Path(folder) / "site" / "chapters" / "I-1.html").read_text()
            self.assertIn("&lt;script&gt;", html)
            self.assertNotIn('<script>alert("x")</script>', html)

    def test_epub_notes_have_resolvable_return_links(self):
        with tempfile.TemporaryDirectory() as folder:
            self.api_ready().build(sample(), Path(folder))
            path = Path(folder) / "finnegans-wake-zh.epub"
            with zipfile.ZipFile(path) as book:
                self.assertEqual(book.infolist()[0].filename, "mimetype")
                self.assertEqual(book.infolist()[0].compress_type, zipfile.ZIP_STORED)
                self.assertEqual(book.read("mimetype"), b"application/epub+zip")
                root = ET.fromstring(book.read("EPUB/chapters/I-1.xhtml"))
                ids = {e.attrib["id"] for e in root.iter() if "id" in e.attrib}
                fragment_links = [e.attrib["href"][1:] for e in root.iter() if e.attrib.get("href", "").startswith("#")]
                self.assertIn("note-n-river", fragment_links)
                self.assertIn("ref-n-river", fragment_links)
                self.assertTrue(set(fragment_links) <= ids)
            self.assertEqual(self.api_ready().check_artifacts(Path(folder)), [])

    def test_reader_settings_live_in_the_header_and_have_unique_controls(self):
        class Controls(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids = []
                self.header_controls = []
                self.in_header = False
                self.dialogs = {}

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == 'header': self.in_header = True
                if attrs.get('id'): self.ids.append(attrs['id'])
                if self.in_header and tag == 'button': self.header_controls.append(attrs.get('id'))
                if tag == 'dialog': self.dialogs[attrs['id']] = attrs

            def handle_endtag(self, tag):
                if tag == 'header': self.in_header = False

        with tempfile.TemporaryDirectory() as folder:
            self.api_ready().build(sample(), Path(folder))
            for name in ['index.html', 'glossary.html', 'sources.html', 'chapters/I-1.html']:
                parsed = Controls()
                parsed.feed((Path(folder) / 'site' / name).read_text())
                self.assertIn('reading-settings-toggle', parsed.header_controls)
                self.assertIn('contents-toggle', parsed.header_controls)
                self.assertIn('script-toggle', parsed.header_controls)
                self.assertEqual(len(parsed.ids), len(set(parsed.ids)))
                self.assertEqual(parsed.dialogs['reading-settings']['aria-labelledby'], 'reading-settings-title')
                self.assertIn('reading-margin', parsed.ids)
                self.assertIn('show-original', parsed.ids)
                self.assertIn('show-notes', parsed.ids)
            with zipfile.ZipFile(Path(folder) / 'finnegans-wake-zh.epub') as book:
                self.assertNotIn('<dialog', book.read('EPUB/chapters/I-1.xhtml').decode())

    def test_empty_chapters_still_offer_reading_settings(self):
        data = sample()
        data['chapters'][0]['segments'] = []
        data['chapters'][0]['coverage'] = 'not_started'
        with tempfile.TemporaryDirectory() as folder:
            self.api_ready().build(data, Path(folder))
            html = (Path(folder) / 'site/chapters/I-1.html').read_text()
            self.assertIn('id="reading-settings-toggle"', html)
            self.assertIn('id="reading-settings"', html)

    def test_validation_rejects_missing_canonical_chapter(self):
        data = self.completed_translation()
        data['chapters'] = [c for c in data['chapters'] if c['id'] != 'I.6']
        errors = self.api_ready().validate(data)
        self.assertTrue(any('missing' in e and 'I.6' in e for e in errors))

    def test_validation_rejects_non_contiguous_or_missing_segment(self):
        data = self.completed_translation()
        ch = next(c for c in data['chapters'] if c['id'] == 'II.4')
        # Add two segments then remove the middle gap
        ch['segments'] = [
            {"id": "fw-ii4-383-01", "locator": "383.01–386.36", "range": [383, 1, 386, 36],
             "source_id": "text", "original": "a", "draft": "a", "translation": "a", "status": "draft", "reviewers": [], "notes": [], "alternatives": []},
            {"id": "fw-ii4-387-01", "locator": "387.01–390.36", "range": [387, 1, 390, 36],
             "source_id": "text", "original": "b", "draft": "b", "translation": "b", "status": "draft", "reviewers": [], "notes": [], "alternatives": []},
            {"id": "fw-ii4-391-01", "locator": "391.01–399.34", "range": [391, 1, 399, 34],
             "source_id": "text", "original": "c", "draft": "c", "translation": "c", "status": "draft", "reviewers": [], "notes": [], "alternatives": []},
        ]
        ch['segments'].pop(1)
        errors = self.api_ready().validate(data)
        self.assertTrue(any('non-contiguous' in e for e in errors))

    def test_validation_rejects_non_list_reviewers(self):
        data = sample()
        data['chapters'][0]['segments'][0]['reviewers'] = 'x'
        errors = self.api_ready().validate(data)
        self.assertTrue(any('reviewers must be a list' in e for e in errors))

    def test_validation_rejects_unreviewed_segment_with_reviewers(self):
        data = sample()
        data['chapters'][0]['segments'][0]['status'] = 'draft'
        data['chapters'][0]['segments'][0]['reviewers'] = ['Alice']
        errors = self.api_ready().validate(data)
        self.assertTrue(any('unreviewed segment must have empty reviewers' in e for e in errors))

    def test_validation_rejects_mismatched_cycle_original(self):
        data = self.completed_translation()
        for anchor in ('unrelated text', 'r', None):
            with self.subTest(anchor=anchor):
                data['checkpoint']['cycle_original'] = anchor
                errors = self.api_ready().validate(data)
                self.assertTrue(any('cycle_original does not match' in e for e in errors))

    def test_full_book_requires_chapters_source_and_checkpoint(self):
        data = self.completed_translation()
        data['chapters'].pop()
        data.pop('checkpoint')
        errors = self.api_ready().validate(data, full_book=True)
        self.assertIn('project requires all 17 canonical chapters', errors)
        self.assertIn('project requires a checkpoint', errors)
        self.assertIn('missing English source: I.1', errors)


if __name__ == "__main__":
    unittest.main()
