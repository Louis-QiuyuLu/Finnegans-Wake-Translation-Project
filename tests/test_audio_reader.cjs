const test = require('node:test');
const assert = require('node:assert/strict');
const {normalizeSpeed, coordinatePlayers} = require('../site/audio-reader.js');

test('old or damaged playback speed falls back to normal', () => {
  for (const value of [null, '', 'fast', 'NaN', -1, 99]) assert.equal(normalizeSpeed(value),1);
  assert.equal(normalizeSpeed('1.25'),1.25);
  assert.equal(normalizeSpeed('0.75'),0.75);
});

test('starting another paragraph pauses the previous recording', () => {
  class Player extends EventTarget {
    paused=true; playbackRate=1;
    play() { this.paused=false; this.dispatchEvent(new Event('play')); }
    pause() { this.paused=true; }
  }
  const a=new Player(),b=new Player();
  const group=coordinatePlayers([a,b]);
  a.play(); b.play();
  assert.equal(a.paused,true); assert.equal(b.paused,false);
  group.setSpeed(1.5);
  assert.equal(a.playbackRate,1.5); assert.equal(b.playbackRate,1.5);
  group.setSpeed('broken'); assert.equal(b.playbackRate,1);
  group.pauseAll(); assert.equal(b.paused,true);
});
