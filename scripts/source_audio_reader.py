"""Validate page/role recordings independently of translated segment IDs."""
from html import escape
from scripts.audio_source import prepare_queue

def validate_tracks(data):
 tracks=data.get('source_audio',[])
 if not tracks:return []
 expected={};errors=[];seen=set()
 for book in sorted({t.get('source_binding',{}).get('book','') for t in tracks}):
  try:
   q=prepare_queue(data['chapters'],book)
   for item in q['items']:
    expected[item['id']]={'kind':q['kind'],'book':book,**item,**q['sources'][item['chapter']]}
  except (ValueError,KeyError,TypeError) as exc:errors.append('source audio source invalid: '+str(exc))
 for t in tracks:
  sid=t.get('segment_id');binding=expected.get(sid)
  if not binding or sid in seen or t.get('file')!=sid+'.mp3' or t.get('source_binding')!=binding or t.get('original_sha256')!=binding['original_sha256']:
   errors.append('invalid, stale or duplicate source audio: '+str(sid))
  seen.add(sid)
 return errors

def render_tracks(chapter,data):
 tracks=[t for t in data.get('source_audio',[]) if t.get('source_binding',{}).get('chapter')==chapter['id']]
 if not tracks:return ''
 repository=data.get('config',{}).get('repository','https://github.com/example/book').rstrip('/').split('github.com/')[-1]
 roles={'main':'正文','left':'左旁注','right':'右旁注','footnotes':'原作脚注'};items=[]
 for t in tracks:
  b=t['source_binding'];label=f"第 {b['page']} 页 · {roles[b['role']]} · {b['id'].rsplit('-',1)[-1]}"
  url='https://raw.githubusercontent.com/'+repository+'/main/audio/'+t['file']
  items.append('<li><a href="#source-page-'+str(b['page']).zfill(3)+'">'+escape(label)+'</a><audio controls preload="none" aria-label="'+escape(label,quote=True)+'"><source src="'+escape(url,quote=True)+'" type="audio/mpeg">浏览器不支持音频播放。</audio></li>')
 return '<details class="source-recordings"><summary>英文逐页朗读 · '+str(len(tracks))+' 轨</summary><p>GPT-SoVITS · 重返未来1999 瓦尔汀 · 默认 1×。按页依次为正文、左旁注、右旁注和原作脚注；生造词采用近似读音。</p><ol>'+''.join(items)+'</ol></details>'
