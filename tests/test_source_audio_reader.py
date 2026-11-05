import unittest,copy,hashlib
from scripts import project,source_text,audio_source
class SourceAudioReaderTests(unittest.TestCase):
 def fixture(self):
  html=source_text.sanitize_fragment('<div class="pagenumber">----- 593 -----</div><p>Wake now.</p>')
  c={'id':'IV','book':'IV','number':1,'pages':[593,593],'title':'第四卷','coverage':'not_started','segments':[],'source_text':{'source_id':'joyce-fp','pages':[593],'html':html,'html_sha256':source_text.fingerprint(html)}}
  q=audio_source.prepare_queue([c],'IV');item=q['items'][0];binding={'kind':q['kind'],'book':'IV',**item,**q['sources']['IV']};sid=item['id']
  t={'segment_id':sid,'file':sid+'.mp3','original_sha256':item['original_sha256'],'source_binding':binding}
  return c,{'chapters':[c],'sources':[{'id':'joyce-fp','title':'底本'}],'source_audio':[t]}
 def test_original_page_audio_is_playable_without_chinese_segments(self):
  c,data=self.fixture();html=project.render_source_text(c,data)
  self.assertIn('https://raw.githubusercontent.com/example/book/main/audio/',html);self.assertNotIn('../assets/audio/',html);self.assertIn('<audio controls',html);self.assertIn('preload="none"',html);self.assertIn(data['source_audio'][0]['file'],html)
  self.assertNotIn('<audio',project.render_source_text(c,data,epub=True))
 def test_source_change_and_duplicate_are_rejected(self):
  from scripts.source_audio_reader import validate_tracks
  c,data=self.fixture();self.assertEqual(validate_tracks(data),[])
  data['source_audio'].append(copy.deepcopy(data['source_audio'][0]));self.assertTrue(validate_tracks(data))
  data['source_audio'].pop();c['source_text']['html']+='<p>Changed.</p>';self.assertTrue(validate_tracks(data))
