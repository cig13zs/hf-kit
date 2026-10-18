(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  var reel = document.getElementById('reel');
  function holdReel() {
    if (reel && reduce.matches) {
      reel.removeAttribute('autoplay');
      reel.pause();
    }
  }
  holdReel();
  if (reduce.addEventListener) reduce.addEventListener('change', holdReel);

  var tiles = Array.prototype.slice.call(document.querySelectorAll('.tile'));
  var active = null;

  function parts(t) {
    return { button: t.querySelector('.play'), video: t.querySelector('video'), img: t.querySelector('img') };
  }

  function load(t, still) {
    var v = parts(t).video;
    if (!v.getAttribute('src')) {
      v.preload = still ? 'metadata' : 'auto';
      v.src = v.getAttribute('data-src') + (still ? '#t=0.5' : '');
    }
    return v;
  }

  function stop(t) {
    var p = parts(t);
    p.video.pause();
    t.classList.remove('is-playing');
    p.button.setAttribute('aria-pressed', 'false');
    if (active === t) active = null;
  }

  function start(t) {
    if (t.classList.contains('no-video')) return;
    if (active && active !== t) stop(active);
    var v = load(t, false);
    active = t;
    t.classList.add('is-playing');
    parts(t).button.setAttribute('aria-pressed', 'true');
    var played = v.play();
    if (played && played.catch) played.catch(function () { stop(t); });
  }

  tiles.forEach(function (t) {
    var p = parts(t);
    p.video.addEventListener('error', function () {
      t.classList.add('no-video');
      stop(t);
    });
    if (p.img) {
      p.img.addEventListener('error', function () { t.classList.add('no-gif'); });
      // A GIF can fail before this deferred script runs.
      if (p.img.complete && p.img.naturalWidth === 0) t.classList.add('no-gif');
    }
    p.button.addEventListener('click', function () {
      if (p.button.getAttribute('aria-pressed') === 'true') stop(t); else start(t);
    });
    // Hover preview for a real mouse only: touch taps also fire pointerenter.
    p.button.addEventListener('pointerenter', function (e) {
      if (e.pointerType === 'mouse' && !reduce.matches) start(t);
    });
    p.button.addEventListener('pointerleave', function (e) {
      if (e.pointerType === 'mouse' && !reduce.matches) stop(t);
    });
  });

  // With reduced motion the GIFs are swapped out, so show a still frame of each demo instead.
  if (reduce.matches && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        load(e.target, true);
        e.target.classList.add('is-still');
      });
    }, { rootMargin: '200px 0px' });
    tiles.forEach(function (t) { io.observe(t); });
  }
})();
