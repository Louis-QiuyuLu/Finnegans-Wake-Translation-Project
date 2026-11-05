(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.FWReader = api;
})(typeof window === 'object' ? window : this, function () {
  const defaults = {fontSize:24, lineHeight:2.1, width:760, font:'serif', margin:24};
  function normalizePreferences(input = {}) {
    if (!input || typeof input !== 'object' || Array.isArray(input)) input = {};
    const clamp = (value, min, max, fallback) => value !== null && value !== '' && Number.isFinite(Number(value)) ? Math.max(min, Math.min(max, Number(value))) : fallback;
    return {fontSize:clamp(input.fontSize,18,36,defaults.fontSize), lineHeight:clamp(input.lineHeight,1.5,2.6,defaults.lineHeight), width:clamp(input.width,440,1000,defaults.width), font:['serif','sans','kai'].includes(input.font) ? input.font : defaults.font, margin:clamp(input.margin,12,64,defaults.margin)};
  }
  function normalizeTheme(input) {
    return ['paper','light','sage','dark'].includes(input) ? input : 'paper';
  }
  function normalizeScript(input) {
    return input === 'hant' ? 'hant' : 'hans';
  }
  function createTextVariantStore(toTraditional) {
    const originals = new WeakMap();
    return {render(node, script) {
      const previous = originals.get(node);
      const source = previous && node.nodeValue === previous.display ? previous.source : node.nodeValue;
      const display = normalizeScript(script) === 'hant' ? toTraditional(source) : source;
      if (node.nodeValue !== display) node.nodeValue = display;
      originals.set(node, {source, display});
    }};
  }
  function parseNightlessons(text) {
    return text.split(/\r?\n/).filter(line => line.trim()).map(line => {
      const page = /^【(第\d+页)】\s*$/.exec(line);
      if (page) return {kind:'page', label:page[1], text:''};
      const block = /^【(正文|左旁注|右旁注|原注\d+)】(.*)$/.exec(line);
      if (!block) return {kind:'body', label:'', text:line};
      const [, label, content] = block;
      const kind = label === '正文' ? 'body' : label.startsWith('原注') ? 'footnote' : 'margin';
      return {kind, label, text:content};
    });
  }
  function mergeRevisions(source, revisions = {}) {
    const chapter = JSON.parse(JSON.stringify(source));
    const conflicts = [];
    for (const [id, revision] of Object.entries(revisions)) {
      const segment = chapter.segments.find(s => s.id === id);
      if (!segment) { conflicts.push(`${id}：正文段落已更改，请重新对照。`); continue; }
      const problems = [];
      const proposed = typeof revision.translation === 'string' ? revision.translation.trim() : '';
      if (!proposed) problems.push('译文不能为空');
      const translationChanged = proposed !== revision.baseTranslation;
      if (translationChanged && segment.translation !== revision.baseTranslation && proposed !== segment.translation) problems.push('公共译文已更新');
      const noteUpdates = [];
      for (const [noteId, text] of Object.entries(revision.notes || {})) {
        const note = segment.notes.find(n => n.id === noteId);
        if (!note) { problems.push('译注已更改'); continue; }
        if (typeof text !== 'string' || !text.trim()) { problems.push('译注不能为空'); continue; }
        const baseline = (revision.baseNotes || {})[noteId];
        if (text.trim() === baseline) continue;
        if (note.text !== baseline && text.trim() !== note.text) problems.push('公共译注已更新');
        else noteUpdates.push([note, text.trim()]);
      }
      if (problems.length) { conflicts.push(`${id}：${[...new Set(problems)].join('；')}。`); continue; }
      const changed = (translationChanged && proposed !== segment.translation) || noteUpdates.some(([note, text]) => note.text !== text);
      if (translationChanged) segment.translation = proposed;
      noteUpdates.forEach(([note, text]) => { note.text = text; });
      if (changed) { segment.status = 'revised'; segment.reviewers = []; }
    }
    return {chapter, conflicts};
  }
  function rebaseRevision(current, revision) {
    const notes = Object.fromEntries(current.notes.map(note => {
      const proposed = (revision.notes || {})[note.id];
      const edited = proposed !== undefined && proposed !== (revision.baseNotes || {})[note.id];
      return [note.id, edited ? proposed : note.text];
    }));
    return {baseTranslation:current.translation, baseNotes:Object.fromEntries(current.notes.map(n => [n.id,n.text])), translation:revision.translation !== revision.baseTranslation ? revision.translation : current.translation, notes};
  }
  function prepareExport(source, revisions, latest) {
    if (JSON.stringify(source) !== JSON.stringify(latest)) return {chapter:null,conflicts:['仓库章稿已更新。请刷新页面，对照现稿后继续；本机修订仍会保留。']};
    return mergeRevisions(source,revisions);
  }
  return {normalizePreferences, normalizeTheme, normalizeScript, createTextVariantStore, parseNightlessons, mergeRevisions, rebaseRevision, prepareExport};
});
