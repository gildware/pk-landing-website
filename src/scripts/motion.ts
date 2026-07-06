/** Scroll-triggered reveal animations (monday.com-style). Respects prefers-reduced-motion. */
function initMotion() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const header = document.getElementById('site-header');
  if (header) {
    const onScroll = () => {
      header.classList.toggle('header-scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  if (reduced) {
    document.querySelectorAll('.reveal, .reveal-scale, .reveal-left, .reveal-right').forEach((el) => {
      el.classList.add('is-visible');
    });
    return;
  }

  const revealEls = document.querySelectorAll('.reveal, .reveal-scale, .reveal-left, .reveal-right');
  if (!revealEls.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { rootMargin: '0px 0px -8% 0px', threshold: 0.12 },
  );

  revealEls.forEach((el) => observer.observe(el));
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMotion);
} else {
  initMotion();
}
