const test = require('node:test');
const assert = require('node:assert/strict');
const { normalizePreferences, mergeRevisions } = require('../site/reader-model.js');

const chapter = () => ({id:'I.1', segments:[{id:'s1', original:'riverrun', draft:'初译', translation:'现译', status:'reviewed', reviewers:['reader'], notes:[{id:'n1', text:'原注', source_ids:['joyce']}]}]});

test('preference values stay within supported reading ranges', () => {
  assert.deepEqual(normalizePreferences({fontSize:99,lineHeight:0,width:'bad',font:'unknown'}), {fontSize:36,lineHeight:1.5,width:760,font:'serif'});
  assert.deepEqual(normalizePreferences({fontSize:22,lineHeight:2,width:700,font:'sans'}), {fontSize:22,lineHeight:2,width:700,font:'sans'});
});

test('edited translation and note preserve source data and require another review', () => {
  const source=chapter();
  const result=mergeRevisions(source, {s1:{baseTranslation:'现译',baseNotes:{n1:'原注'},translation:'修订译文',notes:{n1:'修订注'}}});
  assert.deepEqual(result.conflicts, []);
  const segment=result.chapter.segments[0];
  assert.equal(segment.translation,'修订译文');
  assert.equal(segment.notes[0].text,'修订注');
  assert.deepEqual(segment.notes[0].source_ids,['joyce']);
  assert.equal(segment.original,'riverrun');
  assert.equal(segment.draft,'初译');
  assert.equal(segment.status,'revised');
  assert.deepEqual(segment.reviewers,[]);
  assert.equal(source.segments[0].translation,'现译');
});

test('stale translation is flagged instead of silently replacing a newer manuscript', () => {
  const result=mergeRevisions(chapter(), {s1:{baseTranslation:'旧译',baseNotes:{n1:'原注'},translation:'本机修订',notes:{n1:'原注'}}});
  assert.equal(result.conflicts.length,1);
  assert.equal(result.chapter.segments[0].translation,'现译');
});

test('stale note and empty translation cannot be exported', () => {
  assert.equal(mergeRevisions(chapter(), {s1:{baseTranslation:'现译',baseNotes:{n1:'旧注'},translation:'现译',notes:{n1:'本机注'}}}).conflicts.length,1);
  assert.equal(mergeRevisions(chapter(), {s1:{baseTranslation:'现译',baseNotes:{n1:'原注'},translation:'  ',notes:{}}}).conflicts.length,1);
});

test('an unchanged local draft preserves the existing review record', () => {
  const result=mergeRevisions(chapter(), {s1:{baseTranslation:'现译',baseNotes:{n1:'原注'},translation:'现译',notes:{n1:'原注'}}});
  assert.deepEqual(result.conflicts,[]);
  assert.equal(result.chapter.segments[0].status,'reviewed');
  assert.deepEqual(result.chapter.segments[0].reviewers,['reader']);
});
