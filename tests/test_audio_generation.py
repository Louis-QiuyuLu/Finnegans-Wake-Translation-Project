import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

class AudioGenerationTests(unittest.TestCase):
    def test_registering_a_regenerated_track_preserves_other_tracks(self):
        spec=importlib.util.spec_from_file_location('generate_audio',Path(__file__).resolve().parents[1]/'scripts/generate_audio.py')
        api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            api.register_audio({'id':'a','original':'first'},root)
            api.register_audio({'id':'b','original':'second'},root)
            api.register_audio({'id':'a','original':'revised'},root)
            tracks=json.loads((root/'index.json').read_text())['tracks']
            self.assertEqual([t['segment_id'] for t in tracks],['a','b'])
            import hashlib
            self.assertEqual(tracks[0]['original_sha256'],hashlib.sha256(b'revised').hexdigest())
