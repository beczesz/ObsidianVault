// IGNIS professional — interactions (demo)
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
      { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
    );
    reveals.forEach((el) => io.observe(el));
  }

  const masthead = document.querySelector(".masthead");
  const onScroll = () => { if (masthead) masthead.dataset.scrolled = window.scrollY > 8 ? "true" : "false"; };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
})();
