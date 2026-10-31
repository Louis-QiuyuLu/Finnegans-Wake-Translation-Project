(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('#theme-toggle');
  const stored = (key) => { try { return localStorage.getItem(key); } catch { return null; } };
  const save = (key, value) => { try { localStorage.setItem(key, value); return true; } catch { return false; } };
  const readJSON = (key, fallback) => { try { return JSON.parse(stored(key)) || fallback; } catch { return fallback; } };
  const setTheme = (theme) => {
    root.dataset.theme = theme;
    themeButton.textContent = theme === 'dark' ? '日读' : '夜读';
    themeButton.setAttribute('aria-pressed', String(theme === 'dark'));
  };
  setTheme(stored('fw:theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  themeButton.addEventListener('click', () => {
    const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(theme);
    save('fw:theme', theme);
  });
  if (matchMedia('(max-width: 700px)').matches) document.querySelector('.sidebar details')?.removeAttribute('open');
  const preferenceInputs = {fontSize:document.getElementById('font-size'), lineHeight:document.getElementById('line-height'), width:document.getElementById('reading-width'), font:document.getElementById('reading-font')};
  const fonts = {serif:'var(--serif)', sans:'var(--sans)', kai:'"Kaiti SC","STKaiti","KaiTi",var(--serif)'};
  const setPreferences = (values) => {
    const preferences = FWReader.normalizePreferences(values);
    root.style.setProperty('--reading-size', `${preferences.fontSize}px`);
    root.style.setProperty('--reading-leading', preferences.lineHeight);
    root.style.setProperty('--reading-width', `${preferences.width}px`);
    root.style.setProperty('--reading-font', fonts[preferences.font]);
    for (const [key, input] of Object.entries(preferenceInputs)) if (input) input.value = preferences[key];
    for (const [id, value] of [['font-size-value',preferences.fontSize],['line-height-value',preferences.lineHeight],['reading-width-value',preferences.width]]) {
      const output=document.getElementById(id);
      if (output) output.textContent=value;
    }
    return preferences;
  };
  setPreferences(readJSON('fw:reading-preferences', {}));
  for (const input of Object.values(preferenceInputs)) input?.addEventListener('input', () => {
    const values=Object.fromEntries(Object.entries(preferenceInputs).map(([key, control]) => [key, control.value]));
    save('fw:reading-preferences',JSON.stringify(setPreferences(values)));
  });
  document.getElementById('reset-reading')?.addEventListener('click', () => save('fw:reading-preferences',JSON.stringify(setPreferences({}))));
  for (const [id, className] of [['show-original', 'hide-original'], ['show-notes', 'hide-notes']]) {
    const input = document.getElementById(id);
    if (!input) continue;
    input.checked = stored(`fw:${id}`) !== 'false';
    document.body.classList.toggle(className, !input.checked);
    input.addEventListener('change', () => {
      document.body.classList.toggle(className, !input.checked);
      save(`fw:${id}`, String(input.checked));
    });
  }
  const search = document.getElementById('reader-search');
  const segments = [...document.querySelectorAll('.segment')];
  search?.addEventListener('input', () => {
    const words = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const segment of segments) {
      const text = segment.textContent.toLocaleLowerCase();
      segment.hidden = !words.every(word => text.includes(word));
      if (!segment.hidden) shown++;
    }
    document.getElementById('search-status').textContent = words.length ? `找到 ${shown} 段，共 ${segments.length} 段` : '';
  });
  const openHash = () => {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    const segment = target.closest('.segment');
    if (segment?.hidden) {
      search.value = '';
      search.dispatchEvent(new Event('input'));
    }
    if (target.closest('.notes') && document.body.classList.contains('hide-notes')) {
      const toggle = document.getElementById('show-notes');
      toggle.checked = true;
      toggle.dispatchEvent(new Event('change'));
    }
    if (target.matches('details')) target.open = true;
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  };
  addEventListener('hashchange', openHash);
  document.querySelectorAll('.noteref').forEach(link => link.addEventListener('click', () => {
    if (link.hash === location.hash) openHash();
  }));
  if (location.hash) openHash();

  const dataElement=document.getElementById('chapter-data');
  if (!dataElement) return;
  const payload=JSON.parse(dataElement.textContent);
  const canonical=payload.chapter;
  const revisionKey=`fw:${payload.repository}:revisions:${canonical.id}`;
  let revisions=readJSON(revisionKey,{});
  if (typeof revisions !== 'object' || Array.isArray(revisions)) revisions={};
  const editors=[...document.querySelectorAll('.revision-editor')];
  const summary=document.getElementById('revision-summary');
  const baseFor = (segment) => ({baseTranslation:segment.translation,baseNotes:Object.fromEntries(segment.notes.map(n => [n.id,n.text]))});
  const replaceParagraphs = (container, text, selector=':scope > p', before=null) => {
    container.querySelectorAll(selector).forEach(p => p.remove());
    for (const part of text.split('\n\n')) {
      const p=document.createElement('p');
      p.textContent=part;
      container.insertBefore(p,before);
    }
  };
  const paint = () => {
    const result=FWReader.mergeRevisions(canonical,revisions);
    for (const segment of result.chapter.segments) {
      const section=document.getElementById(segment.id);
      replaceParagraphs(section.querySelector('.translation'),segment.translation);
      for (const note of segment.notes) {
        const container=document.getElementById(`note-${note.id}`);
        replaceParagraphs(container,note.text,':scope > p:not(.source-links)',container.querySelector('.source-links'));
      }
      let badge=section.querySelector('.local-revision-badge');
      if (!badge) { badge=document.createElement('span'); badge.className='local-revision-badge'; section.querySelector('.locator').append(badge); }
      badge.hidden=!revisions[segment.id];
      badge.textContent=result.conflicts.some(c => c.startsWith(`${segment.id}：`)) ? '本机修订待复核' : '本机修订';
      const editor=section.querySelector('.revision-editor');
      editor.querySelector('.rebase-revision').hidden=!result.conflicts.some(c => c.startsWith(`${segment.id}：`));
    }
    const count=Object.keys(revisions).length;
    summary.textContent=result.conflicts.length ? `${result.conflicts.join(' ')}请对照现稿后确认，再导出或提交。` : count ? `已保存 ${count} 段本机修订，尚未提交 GitHub。` : '当前显示公共译稿。';
    return result;
  };
  const fillEditor = (editor) => {
    const segment=canonical.segments.find(s => s.id===editor.dataset.segment);
    const revision=revisions[segment.id];
    editor.querySelector('.edit-translation').value=revision?.translation ?? segment.translation;
    editor.querySelectorAll('.edit-note').forEach(input => {
      input.value=revision?.notes?.[input.dataset.note] ?? segment.notes.find(n => n.id===input.dataset.note).text;
    });
  };
  const captureEditor = (editor, rebase=false) => {
    const segment=canonical.segments.find(s => s.id===editor.dataset.segment);
    revisions[segment.id]={...(rebase ? baseFor(segment) : revisions[segment.id] || baseFor(segment)), translation:editor.querySelector('.edit-translation').value, notes:Object.fromEntries([...editor.querySelectorAll('.edit-note')].map(input => [input.dataset.note,input.value]))};
    const persisted=save(revisionKey,JSON.stringify(revisions));
    const result=paint();
    editor.querySelector('.revision-status').textContent=!persisted ? '已预览，浏览器未能保存。请立即导出修订稿。' : result.conflicts.some(c => c.startsWith(`${segment.id}：`)) ? '本机修订已保留。请对照现稿后确认。' : '已保存到本机，并应用到本页。';
  };
  for (const editor of editors) {
    fillEditor(editor);
    editor.querySelector('.save-revision').addEventListener('click', () => captureEditor(editor));
    editor.querySelector('.rebase-revision').addEventListener('click', () => captureEditor(editor,true));
    editor.querySelector('.discard-revision').addEventListener('click', () => {
      delete revisions[editor.dataset.segment];
      const persisted=save(revisionKey,JSON.stringify(revisions));
      fillEditor(editor);
      paint();
      editor.querySelector('.revision-status').textContent=persisted ? '已清除此段本机修订，恢复公共译稿。' : '当前预览已恢复；浏览器未能清除存储，请导出后再处理。';
    });
  }
  paint();
  const exportText = () => {
    for (const editor of editors) {
      const source=canonical.segments.find(s => s.id===editor.dataset.segment);
      const revision=revisions[source.id];
      const changed=editor.querySelector('.edit-translation').value !== (revision?.translation ?? source.translation) || [...editor.querySelectorAll('.edit-note')].some(input => input.value !== (revision?.notes?.[input.dataset.note] ?? source.notes.find(n => n.id===input.dataset.note).text));
      if (changed) captureEditor(editor);
    }
    const result=paint();
    return result.conflicts.length ? null : JSON.stringify(result.chapter,null,2)+'\n';
  };
  document.getElementById('export-revisions').addEventListener('click', () => {
    const text=exportText();
    if (text===null) return;
    const url=URL.createObjectURL(new Blob([text],{type:'application/json;charset=utf-8'}));
    const link=document.createElement('a');
    link.href=url;
    link.download=canonical.id.replaceAll('.','-')+'.json';
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url),1000);
    summary.textContent='已导出本章修订稿。可在 GitHub 编辑页粘贴文件内容并提交。';
  });
  document.getElementById('submit-revisions').addEventListener('click', async () => {
    const text=exportText();
    if (text===null) return;
    window.open(payload.edit_url,'_blank','noopener,noreferrer');
    try {
      await navigator.clipboard.writeText(text);
      summary.textContent='已复制本章修订稿。请在 GitHub 编辑页全选、粘贴并提交；若新页未打开，可点「直接编辑仓库稿件」。';
    } catch {
      summary.textContent='请先导出本章修订稿，再把文件内容粘贴到 GitHub 编辑页提交。';
    }
  });
})();
