(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.FWReader = api;
})(typeof window === 'object' ? window : this, function () {
  const defaults = {fontSize:24, lineHeight:2.1, width:760, font:'serif'};
  function normalizePreferences(input = {}) {
    const clamp = (value, min, max, fallback) => value !== null && value !== '' && Number.isFinite(Number(value)) ? Math.max(min, Math.min(max, Number(value))) : fallback;
    return {fontSize:clamp(input.fontSize,18,36,defaults.fontSize), lineHeight:clamp(input.lineHeight,1.5,2.6,defaults.lineHeight), width:clamp(input.width,440,1000,defaults.width), font:['serif','sans','kai'].includes(input.font) ? input.font : defaults.font};
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
  return {normalizePreferences, mergeRevisions};
});
