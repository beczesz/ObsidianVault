// Dr. Antal Réka Ügyvédi Iroda — demó interakciók
(function () {
  "use strict";

  /* Sticky header tömörödés scrollra */
  const header = document.querySelector(".site-header");
  const onScroll = () => {
    if (header) header.dataset.scrolled = window.scrollY > 8 ? "true" : "false";
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* Scroll reveal — finom, ease-out, csak ha nincs reduced-motion */
  const reveals = document.querySelectorAll(".reveal");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
      { rootMargin: "0px 0px -8% 0px", threshold: 0.1 }
    );
    reveals.forEach((el) => io.observe(el));
  }

  /* Nyelvváltó (demó — csak a kijelölést kezeli) */
  const langButtons = document.querySelectorAll(".lang button");
  langButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      langButtons.forEach((b) => b.setAttribute("aria-pressed", "false"));
      btn.setAttribute("aria-pressed", "true");
    });
  });

  /* Kapcsolati űrlap — demó validáció, valódi küldés nélkül */
  const form = document.querySelector(".contact-form");
  const note = document.querySelector("[data-form-note]");
  if (form && note) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const nev = form.nev.value.trim();
      const email = form.email.value.trim();
      const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

      note.hidden = false;
      if (!nev || !emailOk) {
        note.dataset.state = "err";
        note.textContent = !nev
          ? "Kérem, adja meg a nevét."
          : "Úgy tűnik, az e-mail cím hiányos.";
        (nev ? form.email : form.nev).focus();
        return;
      }
      note.dataset.state = "ok";
      note.textContent = `Köszönöm, ${nev.split(" ")[0]}! Demó űrlap — valódi üzenet nem ment el.`;
      form.reset();
    });
  }
})();
