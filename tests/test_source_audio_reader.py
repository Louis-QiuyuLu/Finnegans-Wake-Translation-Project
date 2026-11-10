import unittest,copy,hashlib
from unittest.mock import patch
from scripts import project,source_text,audio_source
class SourceAudioReaderTests(unittest.TestCase):
 def fixture(self):
  html=source_text.sanitize_fragment('<div class="pagenumber">----- 593 -----</div><p>Wake now.</p>')
  c={'id':'IV','book':'IV','number':1,'pages':[593,593],'title':'第四卷','coverage':'not_started','segments':[],'source_text':{'source_id':'joyce-fp','pages':[593],'html':html,'html_sha256':source_text.fingerprint(html)}}
  q=audio_source.prepare_queue([c],'IV');item=q['items'][0];binding={'kind':q['kind'],'book':'IV',**item,**q['sources']['IV']};sid=item['id']
  t={'segment_id':sid,'file':sid+'.mp3','original_sha256':item['original_sha256'],'source_binding':binding}
  return c,{'chapters':[c],'sources':[{'id':'joyce-fp','title':'底本'}],'source_audio':[t],'config':{'audio_ref':'a' * 40}}
 def test_original_page_audio_is_playable_without_chinese_segments(self):
  c,data=self.fixture()
  with patch.dict('os.environ', {'GITHUB_SHA': 'b' * 40}):
   html=project.render_source_text(c,data)
  self.assertIn('https://raw.githubusercontent.com/example/book/'+'b'*40+'/audio/',html);self.assertNotIn('../assets/audio/',html);self.assertIn('<audio controls',html);self.assertIn('preload="none"',html);self.assertIn(data['source_audio'][0]['file'],html)
  self.assertNotIn('<audio',project.render_source_text(c,data,epub=True))
 def test_chapter_audio_entry_is_visible_without_opening_source_text(self):
  c,data=self.fixture()
  c['coverage']='complete'
  html=project.render_source_text(c,data)
  audio_entry=html.index('<details class="source-recordings">')
  source_entry=html.index('<details class="full-source-details">')
  self.assertLess(audio_entry,source_entry)
  self.assertIn('</details>',html[audio_entry:source_entry])
  self.assertIn('href="#source-page-593"',html[audio_entry:source_entry])
 def test_source_change_and_duplicate_are_rejected(self):
  from scripts.source_audio_reader import validate_tracks
  c,data=self.fixture();self.assertEqual(validate_tracks(data),[])
  data['source_audio'].append(copy.deepcopy(data['source_audio'][0]));self.assertTrue(validate_tracks(data))
  data['source_audio'].pop();c['source_text']['html']+='<p>Changed.</p>';self.assertTrue(validate_tracks(data))
 def test_render_tracks_sorts_by_page_and_role_order(self):
  from scripts.source_audio_reader import render_tracks
  c = {'id': 'II.2', 'book': 'II', 'number': 2, 'pages': [260, 260], 'title': 'II.2'}
  data = {
      'config': {'repository': 'https://github.com/example/book', 'audio_ref': 'a' * 40},
      'source_audio': [
          {'segment_id': 't4', 'file': 't4.mp3', 'source_binding': {'chapter': 'II.2', 'book': 'II', 'page': 260, 'role': 'footnotes', 'start': 0, 'id': 't4'}},
          {'segment_id': 't2', 'file': 't2.mp3', 'source_binding': {'chapter': 'II.2', 'book': 'II', 'page': 260, 'role': 'left', 'start': 0, 'id': 't2'}},
          {'segment_id': 't1', 'file': 't1.mp3', 'source_binding': {'chapter': 'II.2', 'book': 'II', 'page': 260, 'role': 'main', 'start': 0, 'id': 't1'}},
          {'segment_id': 't3', 'file': 't3.mp3', 'source_binding': {'chapter': 'II.2', 'book': 'II', 'page': 260, 'role': 'right', 'start': 0, 'id': 't3'}},
      ]
  }
  html = render_tracks(c, data)
  # verify order in rendered html: main, left, right, footnotes
  pos1 = html.find('正文')
  pos2 = html.find('左旁注')
  pos3 = html.find('右旁注')
  pos4 = html.find('原作脚注')
  self.assertTrue(0 < pos1 < pos2 < pos3 < pos4)
