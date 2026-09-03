(function(){
'use strict';
var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var hasGSAP = typeof window.gsap !== 'undefined';
if (hasGSAP && window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);

/* ---------- 1. SMOOTH SCROLL ---------- */
var lenis = null;
if (!reduce && typeof window.Lenis !== 'undefined') {
  lenis = new Lenis({ duration: 1.15, lerp: 0.09, wheelMultiplier: 1, smoothWheel: true });
  if (hasGSAP) {
    lenis.on('scroll', function(){ if (window.ScrollTrigger) ScrollTrigger.update(); });
    gsap.ticker.add(function(t){ lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  } else {
    (function raf(t){ lenis.raf(t); requestAnimationFrame(raf); })(0);
  }
}
function goTo(target){
  var el = document.querySelector(target);
  if (!el) return;
  if (lenis) lenis.scrollTo(el, { offset: -70, duration: 1.35 });
  else el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
}

/* ---------- 1b. CASE-STUDY ROUTER ---------- */
var HOME = document.getElementById('home');
var PAGES = Array.prototype.slice.call(document.querySelectorAll('.cpage'));
function toTop(){
  if (lenis) lenis.scrollTo(0, { immediate: true });
  window.scrollTo(0, 0);
}
function showHome(){
  PAGES.forEach(function(p){ p.hidden = true; p.classList.remove('in'); });
  HOME.style.display = '';
  document.body.classList.remove('on-case');
  if (window.ScrollTrigger) ScrollTrigger.refresh();
}
function showCase(slug){
  var page = document.getElementById('case-' + slug);
  if (!page) { showHome(); return false; }
  PAGES.forEach(function(p){ p.hidden = (p !== page); p.classList.remove('in'); });
  HOME.style.display = 'none';
  document.body.classList.add('on-case');
  toTop();
  if (window.ScrollTrigger) ScrollTrigger.refresh();
  requestAnimationFrame(function(){ requestAnimationFrame(function(){ page.classList.add('in'); }); });
  return true;
}
function route(){
  var m = (location.hash || '').match(/^#work\/([a-z-]+)/);
  if (m) { if (showCase(m[1])) return; }
  if (document.body.classList.contains('on-case')) { showHome(); toTop(); }
}
window.addEventListener('hashchange', route);

document.querySelectorAll('a[href^="#"]').forEach(function(a){
  a.addEventListener('click', function(e){
    var h = a.getAttribute('href');
    if (h.length < 2) return;
    if (h.indexOf('#work/') === 0) return;          /* the router handles these */
    e.preventDefault();
    if (document.body.classList.contains('on-case')) {
      history.replaceState(null, '', location.pathname + location.search);
      showHome();
      requestAnimationFrame(function(){ h === '#top' ? toTop() : goTo(h); });
    } else {
      goTo(h);
    }
  });
});

/* ---------- 2. LOADER ---------- */
var loader = document.getElementById('loader');
var curtain = document.getElementById('curtain');
function startSite(){
  document.body.dataset.ready = '1';
  if (!hasGSAP) return;
  gsap.timeline()
    .to('#heroTitle .ln > span', { yPercent: 0, duration: 1.15, stagger: .09, ease: 'expo.out' }, 0)
    .fromTo('#heroTitle', { filter: 'blur(16px)' }, { filter: 'blur(0px)', duration: 1.1, ease: 'power2.out' }, 0)
    .fromTo('#hero .rv', { opacity: 0, y: 26, filter: 'blur(8px)' },
      { opacity: 1, y: 0, filter: 'blur(0px)', duration: 1, stagger: .09, ease: 'power3.out',
        onComplete: function(){ this.targets().forEach(settleFilter); } }, .25);
}
function bootstrap(){
  if (reduce || !hasGSAP) {
    if (loader) loader.style.display = 'none';
    document.querySelectorAll('.rv').forEach(function(e){ e.style.opacity = 1; e.style.transform = 'none'; e.style.filter = 'none'; });
    document.querySelectorAll('#heroTitle .ln > span').forEach(function(e){ e.style.transform = 'none'; });
    startSite(); return;
  }
  gsap.set('#heroTitle .ln > span', { yPercent: 108 });
  var counter = { v: 0 };
  var pct = loader.querySelector('.pct');
  gsap.timeline()
    .to(loader.querySelector('.mark'), { opacity: 1, filter: 'blur(0px)', duration: 1.1, ease: 'power2.out' })
    .to(loader.querySelector('.bar i'), { scaleX: 1, duration: 1.5, ease: 'power2.inOut' }, .1)
    .to(counter, { v: 100, duration: 1.5, ease: 'power2.inOut',
      onUpdate: function(){ pct.textContent = String(Math.round(counter.v)).padStart(3, '0'); } }, .1)
    .to(curtain, { y: '0%', duration: .7, ease: 'expo.inOut' }, '+=.12')
    .set(loader, { display: 'none' })
    .to(curtain, { y: '-100%', duration: .9, ease: 'expo.inOut' }, '+=.05')
    .add(startSite, '-=.55');
}
window.addEventListener('load', bootstrap);
/* failsafe: never leave the page hidden if a CDN script never arrives */
setTimeout(function(){
  if (document.body.dataset.ready) return;
  if (loader) loader.style.display = 'none';
  if (curtain) curtain.style.transform = 'translateY(100%)';
  document.querySelectorAll('.rv').forEach(function(e){ e.style.opacity = 1; e.style.transform = 'none'; e.style.filter = 'none'; });
  document.querySelectorAll('#heroTitle .ln > span').forEach(function(e){ e.style.transform = 'none'; });
  document.body.dataset.ready = '1';
}, 4200);

/* ---------- 3. CURSOR ---------- */
var cur = document.getElementById('cur'), ring = document.getElementById('ring');
if (cur && window.matchMedia('(hover:hover)').matches) {
  var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
  addEventListener('mousemove', function(e){ mx = e.clientX; my = e.clientY; });
  (function loop(){
    rx += (mx - rx) * .16; ry += (my - ry) * .16;
    cur.style.transform = 'translate3d(' + mx + 'px,' + my + 'px,0)';
    ring.style.transform = 'translate3d(' + rx + 'px,' + ry + 'px,0)';
    requestAnimationFrame(loop);
  })();
  document.querySelectorAll('[data-cursor]').forEach(function(el){
    el.addEventListener('mouseenter', function(){ document.body.classList.add('hovering'); });
    el.addEventListener('mouseleave', function(){ document.body.classList.remove('hovering'); });
  });
}

/* ---------- 4. MAGNETIC BUTTONS ---------- */
if (!reduce && hasGSAP && window.matchMedia('(hover:hover)').matches) {
  document.querySelectorAll('.magnet').forEach(function(el){
    el.addEventListener('mousemove', function(e){
      var r = el.getBoundingClientRect();
      gsap.to(el, { x: (e.clientX - r.left - r.width / 2) * .32, y: (e.clientY - r.top - r.height / 2) * .42,
        duration: .6, ease: 'power3.out' });
    });
    el.addEventListener('mouseleave', function(){
      gsap.to(el, { x: 0, y: 0, duration: .8, ease: 'elastic.out(1,.4)' });
    });
  });
}

/* ---------- 5. HEADER ---------- */
var hdr = document.getElementById('hdr');
function onScrollHeader(y){
  hdr.classList.toggle('solid', y > 40);
}

/* ---------- 6. SCROLL VELOCITY → MOTION BLUR ---------- */
var mblurG = document.getElementById('mblurG');
var mbEls = Array.prototype.slice.call(document.querySelectorAll('.mb'));
var lane = document.getElementById('lane'), ticker = document.getElementById('ticker');
var prog = document.getElementById('progress');
var lastPos = 0, vel = 0, smoothVel = 0, filtered = false, settleAt = 0, marqueeX = 0;

/* An element finishing its reveal must not stomp on a live motion blur, and must
   never fall back to the .rv class blur. Both paths go through this. */
function settleFilter(el){
  el.classList.remove('rv');
  el.style.filter = (filtered && el.classList.contains('mb')) ? 'url(#mblur)' : 'none';
}

/* duplicate ticker content for a seamless loop */
if (lane) {
  var base = lane.innerHTML;
  lane.innerHTML = base + base + base;
}

function frame(){
  var y = window.scrollY || document.documentElement.scrollTop;
  var raw = y - lastPos; lastPos = y;
  vel += (raw - vel) * .22;
  smoothVel += (Math.min(Math.abs(vel), 90) - smoothVel) * .18;

  /* progress bar */
  var max = document.documentElement.scrollHeight - innerHeight;
  if (prog) prog.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';

  onScrollHeader(y);

  /* directional motion blur — hysteresis so it can't chatter around the threshold,
     and an explicit 'none' on the way out so no class-level blur can creep back in */
  if (!reduce) {
    var b = Math.min(smoothVel * .17, 13);
    if (!filtered && b > 1.1) {
      mbEls.forEach(function(e){ e.style.filter = 'url(#mblur)'; });
      filtered = true;
    }
    if (filtered) {
      mblurG.setAttribute('stdDeviation', '0 ' + Math.max(b, 0).toFixed(2));
      if (b < .3) {
        if (!settleAt) settleAt = performance.now();
        else if (performance.now() - settleAt > 140) {
          mblurG.setAttribute('stdDeviation', '0 0');
          mbEls.forEach(function(e){ e.style.filter = 'none'; });
          filtered = false; settleAt = 0;
        }
      } else { settleAt = 0; }
    }
  }

  /* velocity-reactive marquee */
  if (lane) {
    marqueeX -= 1.15 + vel * .55;
    var w = lane.scrollWidth / 3;
    if (marqueeX <= -w) marqueeX += w;
    if (marqueeX > 0) marqueeX -= w;
    lane.style.transform = 'translate3d(' + marqueeX + 'px,0,0)';
    ticker.style.transform = 'skewY(' + (vel * -.035).toFixed(3) + 'deg)';
  }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);

/* ---------- 7. SCROLL REVEALS ---------- */
if (hasGSAP && !reduce) {
  document.querySelectorAll('#manifesto .rv, #partner .rv, #process .rv, #work .rv, #guild .rv, #cta .rv, footer .rv').forEach(function(el, i){
    gsap.to(el, {
      opacity: 1, y: 0, filter: 'blur(0px)', duration: 1.05, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 88%', once: true },
      onComplete: function(){ settleFilter(el); }
    });
  });

  /* parallax */
  document.querySelectorAll('[data-parallax]').forEach(function(el){
    gsap.to(el, {
      yPercent: parseFloat(el.dataset.parallax) * 100, ease: 'none',
      scrollTrigger: { trigger: el.parentNode, start: 'top top', end: 'bottom top', scrub: true }
    });
  });

  /* case image parallax */
  document.querySelectorAll('.case .shot img').forEach(function(img){
    gsap.fromTo(img, { yPercent: -8 }, { yPercent: 0, ease: 'none',
      scrollTrigger: { trigger: img, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* word-by-word manifesto reveal */
  document.querySelectorAll('[data-reveal-words]').forEach(function(p){
    var out = document.createDocumentFragment();
    function push(text, hi){
      text.split(/(\s+)/).forEach(function(t){
        if (!t) return;
        if (/^\s+$/.test(t)) { out.appendChild(document.createTextNode(' ')); return; }
        var w = document.createElement('w');
        if (hi) w.className = 'hi';
        w.textContent = t;
        out.appendChild(w);
      });
    }
    Array.prototype.slice.call(p.childNodes).forEach(function(node){
      if (node.nodeType === 3) push(node.textContent, false);
      else push(node.textContent, node.tagName && node.tagName.toLowerCase() === 'hi');
    });
    p.innerHTML = '';
    p.appendChild(out);
    var words = p.querySelectorAll('w');
    ScrollTrigger.create({
      trigger: p, start: 'top 78%', end: 'bottom 55%', scrub: true,
      onUpdate: function(self){
        var n = Math.round(self.progress * words.length);
        for (var i = 0; i < words.length; i++) words[i].classList.toggle('on', i < n);
      }
    });
  });

  /* counters */
  document.querySelectorAll('[data-count]').forEach(function(el){
    var target = parseFloat(el.dataset.count), suffix = el.dataset.suffix || '';
    var o = { v: 0 };
    ScrollTrigger.create({ trigger: el, start: 'top 90%', once: true, onEnter: function(){
      gsap.to(o, { v: target, duration: 1.6, ease: 'power2.out',
        onUpdate: function(){ el.textContent = Math.round(o.v) + suffix; } });
    }});
  });

  /* pinned horizontal process */
  ScrollTrigger.matchMedia({
    '(min-width: 900px)': function(){
      var track = document.getElementById('ptrack');
      var dist = function(){ return Math.max(0, track.scrollWidth - innerWidth + 120); };
      gsap.to(track, {
        x: function(){ return -dist(); }, ease: 'none',
        scrollTrigger: {
          trigger: '#process', start: 'top top', end: function(){ return '+=' + dist(); },
          pin: true, scrub: 1, anticipatePin: 1, invalidateOnRefresh: true
        }
      });
    }
  });

  /* header inverts while the orange section is behind it */
  ScrollTrigger.create({
    trigger: '#cta', start: 'top 74px', end: 'bottom 74px',
    onToggle: function(self){ hdr.classList.toggle('invert', self.isActive); }
  });

  /* section headline mask-ish rise */
  gsap.utils.toArray('h2.display').forEach(function(h){
    gsap.fromTo(h, { yPercent: 12, opacity: .001 }, {
      yPercent: 0, opacity: 1, duration: 1.1, ease: 'expo.out',
      scrollTrigger: { trigger: h, start: 'top 90%', once: true }
    });
  });
}

/* ---------- 8. HOUSEKEEPING ---------- */
addEventListener('resize', function(){ if (window.ScrollTrigger) ScrollTrigger.refresh(); });
route();
})();
