(() => {
  const root = document.documentElement;
  const stored = (key) => { try { return localStorage.getItem(key); } catch { return null; } };
  const save = (key, value) => { try { localStorage.setItem(key, value); return true; } catch { return false; } };
  const readJSON = (key, fallback) => { try { return JSON.parse(stored(key)) || fallback; } catch { return fallback; } };
  const storageHint = document.getElementById('reading-settings-hint');
  const persist = (key, value) => {
    const saved = save(key, value);
    if (storageHint) storageHint.textContent = saved ? '设置只保存在当前浏览器' : '已应用到本页，浏览器未能保存设置。';
    return saved;
  };
  const themeNames = {paper:'纸张', light:'浅色', sage:'护眼', dark:'深色'};
  const fontNames = {serif:'思源宋体', sans:'思源黑体', kai:'霞鹜文楷'};
  const fonts = {serif:'var(--serif)', sans:'var(--sans)', kai:'var(--kai)'};
  const preferenceInputs = {fontSize:document.getElementById('font-size'), lineHeight:document.getElementById('line-height'), width:document.getElementById('reading-width'), margin:document.getElementById('reading-margin')};
  let preferences = FWReader.normalizePreferences(readJSON('fw:reading-preferences', {}));
  const updateSummary = () => {
    const summary = document.getElementById('reading-summary');
    if (summary) summary.textContent = `${fontNames[preferences.font]} · ${preferences.fontSize}px · ${themeNames[root.dataset.theme]}`;
  };
  const setTheme = (value) => {
    const theme = FWReader.normalizeTheme(value);
    root.dataset.theme = theme;
    document.querySelectorAll('[data-reading-theme]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.readingTheme === theme)));
    updateSummary();
    return theme;
  };
  const setPreferences = (values) => {
    preferences = FWReader.normalizePreferences(values);
    root.style.setProperty('--reading-size', `${preferences.fontSize}px`);
    root.style.setProperty('--reading-leading', preferences.lineHeight);
    root.style.setProperty('--reading-width', `${preferences.width}px`);
    root.style.setProperty('--reading-margin', `${preferences.margin}px`);
    root.style.setProperty('--reading-font', fonts[preferences.font]);
    for (const [key, input] of Object.entries(preferenceInputs)) if (input) input.value = preferences[key];
    for (const [id, value] of [['line-height-value',preferences.lineHeight.toFixed(1)],['reading-width-value',`${preferences.width}px`],['reading-margin-value',`${preferences.margin}px`]]) {
      const output = document.getElementById(id);
      if (output) output.textContent = value;
    }
    document.querySelectorAll('[data-reading-font]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.readingFont === preferences.font)));
    const smaller = document.getElementById('decrease-font');
    const larger = document.getElementById('increase-font');
    if (smaller) smaller.disabled = preferences.fontSize <= 18;
    if (larger) larger.disabled = preferences.fontSize >= 36;
    updateSummary();
    return preferences;
  };
  const changePreferences = (values) => persist('fw:reading-preferences', JSON.stringify(setPreferences(values)));
  setTheme(stored('fw:theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'paper'));
  setPreferences(preferences);
  for (const [key, input] of Object.entries(preferenceInputs)) input?.addEventListener(key === 'fontSize' ? 'change' : 'input', () => changePreferences({...preferences, [key]:input.value}));
  preferenceInputs.fontSize?.addEventListener('input', event => {
    const value = Number(event.target.value);
    if (event.target.value !== '' && Number.isFinite(value) && value >= 18 && value <= 36) changePreferences({...preferences, fontSize:value});
  });
  for (const [id, step] of [['decrease-font',-1],['increase-font',1]]) document.getElementById(id)?.addEventListener('click', () => changePreferences({...preferences, fontSize:preferences.fontSize + step}));
  document.querySelectorAll('[data-reading-font]').forEach(button => button.addEventListener('click', () => changePreferences({...preferences, font:button.dataset.readingFont})));
  document.querySelectorAll('[data-reading-theme]').forEach(button => button.addEventListener('click', () => persist('fw:theme', setTheme(button.dataset.readingTheme))));

  if (matchMedia('(max-width: 700px)').matches) document.querySelector('.sidebar details')?.removeAttribute('open');
  for (const [id, className] of [['show-original', 'hide-original'], ['show-notes', 'hide-notes']]) {
    const input = document.getElementById(id);
    if (!input) continue;
    input.checked = stored(`fw:${id}`) !== 'false';
    document.body.classList.toggle(className, !input.checked);
    input.addEventListener('change', () => {
      document.body.classList.toggle(className, !input.checked);
      persist(`fw:${id}`, String(input.checked));
    });
  }
  document.getElementById('reset-reading')?.addEventListener('click', () => {
    const saved = changePreferences({});
    const themeSaved = persist('fw:theme', setTheme('paper'));
    const scriptSaved = persist('fw:script', setScript('hans'));
    let togglesSaved = true;
    for (const [id, className] of [['show-original','hide-original'],['show-notes','hide-notes']]) {
      const input = document.getElementById(id);
      if (input) input.checked = true;
      document.body.classList.remove(className);
      togglesSaved = save(`fw:${id}`, 'true') && togglesSaved;
    }
    if (storageHint) storageHint.textContent = saved && themeSaved && scriptSaved && togglesSaved ? '已恢复默认阅读设置，本机修订仍保留。' : '已恢复本页设置，浏览器未能保存；本机修订未改动。';
  });

  const openers = new Map();
  document.querySelectorAll('[data-open-dialog]').forEach(button => button.addEventListener('click', () => {
    const dialog = document.getElementById(button.dataset.openDialog);
    if (!dialog || dialog.open) return;
    openers.set(dialog, button);
    dialog.showModal();
    button.setAttribute('aria-expanded', 'true');
    document.body.classList.add('dialog-open');
  }));
  document.querySelectorAll('.reader-dialog').forEach(dialog => {
    let startedOnBackdrop = false;
    const outside = event => {
      const rect = dialog.getBoundingClientRect();
      return event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom;
    };
    dialog.addEventListener('pointerdown', event => { startedOnBackdrop = event.target === dialog && outside(event); });
    dialog.addEventListener('click', event => { if (startedOnBackdrop && event.target === dialog && outside(event)) dialog.close(); });
    dialog.querySelector('[data-close-dialog]')?.addEventListener('click', () => dialog.close());
    dialog.addEventListener('close', () => {
      const opener = openers.get(dialog);
      opener?.setAttribute('aria-expanded', 'false');
      document.body.classList.toggle('dialog-open', Boolean(document.querySelector('.reader-dialog[open]')));
      opener?.focus({preventScroll:true});
    });
  });
  // Convert display text from an exact cached source. Editor values and chapter JSON stay untouched.
  const scriptToggle = document.getElementById('script-toggle');
  const scriptButtons = [...document.querySelectorAll('[data-reading-script]')];
  const converter = typeof OpenCC === 'object' ? OpenCC.Converter({from:'cn', to:'tw'}) : null;
  const variants = FWReader.createTextVariantStore(converter || (text => text));
  let script = 'hans';
  const attributeExcluded = 'script,style,code,pre,[contenteditable],[lang="en"],[data-no-convert]';
  const excluded = `textarea,input,${attributeExcluded}`;
  const attributes = new WeakMap();
  const renderScript = () => {
    observer.disconnect();
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.parentElement.closest(excluded)) variants.render(node, script);
    }
    document.querySelectorAll('[aria-label],[placeholder],[title]').forEach(element => {
      if (element.closest(attributeExcluded)) return;
      const saved = attributes.get(element) || {};
      for (const name of ['aria-label','placeholder','title']) {
        if (!element.hasAttribute(name)) continue;
        const value = element.getAttribute(name);
        const node = saved[name] || {nodeValue:value};
        node.nodeValue = value;
        variants.render(node, script);
        if (value !== node.nodeValue) element.setAttribute(name, node.nodeValue);
        saved[name] = node;
      }
      attributes.set(element, saved);
    });
    observer.observe(document.body, {childList:true, subtree:true, characterData:true});
  };
  const observer = new MutationObserver(renderScript);
  const setScript = value => {
    script = converter ? FWReader.normalizeScript(value) : 'hans';
    root.lang = script === 'hant' ? 'zh-Hant' : 'zh-Hans';
    scriptButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.readingScript === script)));
    if (scriptToggle) {
      scriptToggle.textContent = script === 'hant' ? '简体' : '繁體';
      scriptToggle.setAttribute('aria-label', script === 'hant' ? '切換為簡體中文' : '切换为繁体中文');
    }
    renderScript();
    return script;
  };
  setScript(stored('fw:script'));
  const changeScript = value => {
    persist('fw:script', setScript(value));
    document.getElementById('reader-search')?.dispatchEvent(new Event('input'));
  };
  scriptToggle?.addEventListener('click', () => changeScript(script === 'hans' ? 'hant' : 'hans'));
  scriptButtons.forEach(button => button.addEventListener('click', () => changeScript(button.dataset.readingScript)));
  if (!converter) {
    if (scriptToggle) scriptToggle.disabled = true;
    scriptButtons.forEach(button => { button.disabled = true; });
    if (storageHint) storageHint.textContent = '简繁字形工具未能加载，请刷新后重试。其余阅读设置可照常使用。';
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
  const baseFor = (segment) => ({
    baseOriginal: segment.original,
    baseRange: segment.range,
    baseSourceId: segment.source_id,
    baseTranslation: segment.translation,
    baseNotes: Object.fromEntries(segment.notes.map(n => [n.id, n.text]))
  });
  const replaceParagraphs = (container, text, selector=':scope > p', before=null) => {
    container.querySelectorAll(selector).forEach(p => p.remove());
    for (const part of text.split('\n\n')) {
      const p=document.createElement('p');
      p.textContent=part;
      container.insertBefore(p,before);
    }
  };
  const renderNightlessons = (container, text) => {
    const output = document.createDocumentFragment();
    let page = output;
    let footnotes = null;
    for (const block of FWReader.parseNightlessons(text)) {
      if (block.kind !== 'footnote') footnotes = null;
      if (block.kind === 'page') {
        page = document.createElement('section');
        page.className = 'nightlessons-page';
        const heading = document.createElement('h4');
        heading.textContent = block.label;
        page.append(heading);
        output.append(page);
        continue;
      }
      const paragraph = document.createElement('p');
      if (block.kind === 'margin' || block.kind === 'footnote') {
        const label = document.createElement('strong');
        label.className = 'nightlessons-label';
        label.textContent = block.label;
        paragraph.append(label, ' ');
      }
      paragraph.append(block.text);
      if (block.kind === 'footnote') {
        if (!footnotes) {
          footnotes = document.createElement('details');
          footnotes.className = 'nightlessons-footnotes';
          const summary = document.createElement('summary');
          summary.textContent = '原作脚注';
          footnotes.append(summary);
          page.append(footnotes);
        }
        footnotes.append(paragraph);
      } else if (block.kind === 'margin') {
        const margin = document.createElement('aside');
        margin.className = 'nightlessons-margin';
        margin.append(paragraph);
        page.append(margin);
      } else {
        page.append(paragraph);
      }
    }
    container.replaceChildren(output);
  };
  const paint = () => {
    const result=FWReader.mergeRevisions(canonical,revisions);
    for (const segment of result.chapter.segments) {
      const section=document.getElementById(segment.id);
      const translation = section.querySelector('.translation');
      const nightlessons = translation.querySelector('.nightlessons-text');
      if (nightlessons) renderNightlessons(nightlessons, segment.translation);
      else replaceParagraphs(translation, segment.translation);
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
    const candidate={...(revisions[segment.id] || baseFor(segment)), translation:editor.querySelector('.edit-translation').value, notes:Object.fromEntries([...editor.querySelectorAll('.edit-note')].map(input => [input.dataset.note,input.value]))};
    revisions[segment.id]=rebase ? FWReader.rebaseRevision(segment,candidate) : candidate;
    if (rebase) fillEditor(editor);
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
  const exportText = async () => {
    for (const editor of editors) {
      const source=canonical.segments.find(s => s.id===editor.dataset.segment);
      const revision=revisions[source.id];
      const changed=editor.querySelector('.edit-translation').value !== (revision?.translation ?? source.translation) || [...editor.querySelectorAll('.edit-note')].some(input => input.value !== (revision?.notes?.[input.dataset.note] ?? source.notes.find(n => n.id===input.dataset.note).text));
      if (changed) captureEditor(editor);
    }
    if (paint().conflicts.length) return null;
    summary.textContent='正在核对仓库现稿…';
    try {
      const response=await fetch(payload.source_api,{headers:{Accept:'application/vnd.github.raw+json'},cache:'no-store'});
      if (!response.ok) throw new Error('source unavailable');
      const latest=await response.json();
      const result=FWReader.prepareExport(canonical,revisions,latest);
      if (result.conflicts.length) { summary.textContent=result.conflicts.join(' '); return null; }
      return JSON.stringify(result.chapter,null,2)+'\n';
    } catch {
      summary.textContent='暂时无法核对仓库现稿。修订仍保存在本机，请联网后重试。';
      return null;
    }
  };
  document.getElementById('export-revisions').addEventListener('click', async () => {
    const text=await exportText();
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
    const text=await exportText();
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
