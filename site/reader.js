(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('#theme-toggle');
  const stored = (key) => { try { return localStorage.getItem(key); } catch { return null; } };
  const save = (key, value) => { try { localStorage.setItem(key, value); } catch {} };
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
})();
