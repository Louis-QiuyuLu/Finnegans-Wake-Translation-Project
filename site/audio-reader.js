(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else api.attach(document);
})(typeof window === 'object' ? window : this, function () {
  function normalizeSpeed(value) {
    const speed = Number(value);
    return [0.75, 1, 1.25, 1.5].includes(speed) ? speed : 1;
  }
  function coordinatePlayers(players) {
    const pauseAll = except => players.forEach(player => { if (player !== except) player.pause(); });
    players.forEach(player => player.addEventListener('play', () => pauseAll(player)));
    return {
      pauseAll,
      setSpeed(value) { const speed=normalizeSpeed(value); players.forEach(player => { player.playbackRate=speed; }); return speed; }
    };
  }
  function attach(doc) {
    const players = [...doc.querySelectorAll('.audio-reading audio')];
    const group = coordinatePlayers(players);
    const control = doc.getElementById('audio-speed');
    const key = 'fw:audio-speed';
    const read = () => { try { return doc.defaultView.localStorage.getItem(key); } catch { return null; } };
    const save = value => { try { doc.defaultView.localStorage.setItem(key, String(value)); } catch { /* Playback still works without storage. */ } };
    const setSpeed = value => {
      const speed = group.setSpeed(value);
      if (control) control.value=String(speed);
      return speed;
    };
    setSpeed(read());
    control?.addEventListener('change', () => save(setSpeed(control.value)));
    doc.getElementById('reset-reading')?.addEventListener('click', () => save(setSpeed(1)));
    players.forEach(player => {
      const feedback = player.closest('.audio-reading').querySelector('.audio-feedback');
      player.addEventListener('error', () => { feedback.textContent='音频暂时无法播放，请刷新后重试。'; });
      player.addEventListener('playing', () => { feedback.textContent=''; });
    });
    doc.getElementById('reader-search')?.addEventListener('input', () => {
      players.forEach(player => { if (player.closest('.segment').hidden) player.pause(); });
    });
    doc.defaultView.addEventListener('pagehide', () => group.pauseAll());
  }
  return {normalizeSpeed, coordinatePlayers, attach};
});
