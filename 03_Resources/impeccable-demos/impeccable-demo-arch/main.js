// OBLIQUE — interactions (demo)
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Scroll reveal ---- */
  const reveals = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach((el) => el.classList.add("is-in"));
  } else {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.12 }
    );
    reveals.forEach((el) => io.observe(el));
  }

  /* ---- Masthead: solid background once past the hero ---- */
  const masthead = document.querySelector(".masthead");
  const hero = document.querySelector(".hero");
  if (masthead && hero && "IntersectionObserver" in window) {
    const heroIO = new IntersectionObserver(
      ([e]) => {
        const past = !e.isIntersecting;
        masthead.style.mixBlendMode = past ? "normal" : "difference";
        masthead.style.background = past
          ? "color-mix(in oklch, oklch(0.957 0.006 75) 88%, transparent)"
          : "transparent";
        masthead.style.color = past ? "oklch(0.205 0.008 65)" : "#fff";
        masthead.style.borderBottom = past
          ? "1px solid oklch(0.86 0.008 70)"
          : "1px solid transparent";
        masthead.style.backdropFilter = past ? "blur(10px)" : "none";
      },
      { rootMargin: "-72px 0px 0px 0px", threshold: 0 }
    );
    heroIO.observe(hero);
  }

  /* ---- Lightweight parallax (rAF-throttled, transform only) ---- */
  const layers = Array.from(document.querySelectorAll("[data-parallax]"));
  if (!reduce && layers.length) {
    let ticking = false;
    const update = () => {
      const vh = window.innerHeight;
      layers.forEach((el) => {
        const rect = el.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > vh + 200) return;
        const speed = parseFloat(el.dataset.parallax) || 0.1;
        // progress: -1 (entering bottom) .. 1 (leaving top)
        const progress = (rect.top + rect.height / 2 - vh / 2) / vh;
        const shift = -progress * speed * 100;
        el.style.transform = `translate3d(0, ${shift.toFixed(2)}px, 0)`;
      });
      ticking = false;
    };
    const onScroll = () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
  }
})();
