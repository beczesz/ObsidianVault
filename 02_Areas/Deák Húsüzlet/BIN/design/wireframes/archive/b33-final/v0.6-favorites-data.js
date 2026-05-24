// ====================================================================
// DH v0.6 — Kedvenc Termékek — Product data (matches real-app screenshot)
// ====================================================================

const PRODUCTS = [
  // Füstölt Áruk
  { id: 'p1', name: 'Füstölt Has',       cat: 'fustolt',  catLabel: 'Füstölt Áruk',    price: 47, unit: 'kg', photoTint: 'meat-pink' },
  { id: 'p2', name: 'Füstölt Oldalas',   cat: 'fustolt',  catLabel: 'Füstölt Áruk',    price: 47, unit: 'kg', photoTint: 'meat-strip' },
  // Kolbász & Szalámi
  { id: 'p3', name: 'Deák háziKolbász',  cat: 'kolbasz',  catLabel: 'Kolbász & Szalámi', price: 45, unit: 'kg', photoTint: 'sausage', peach: true },
  // Friss Sertéshús
  { id: 'p4', name: 'Sertés Őrölt Hús',  cat: 'friss',    catLabel: 'Friss Sertéshús', price: 21, unit: 'kg', photoTint: 'ground', peach: true },
  { id: 'p5', name: 'Sertéskaraj',       cat: 'friss',    catLabel: 'Friss Sertéshús', price: 42, unit: 'kg', photoTint: 'cut',    peach: true },
  { id: 'p6', name: 'Sertéstarja',       cat: 'friss',    catLabel: 'Friss Sertéshús', price: 38, unit: 'kg', photoTint: 'cut2',   peach: true },
  // Csirkehús
  { id: 'p7', name: 'Csirkecomb',        cat: 'csirke',   catLabel: 'Friss Csirkehús', price: 28, unit: 'kg', photoTint: 'chicken' },
  { id: 'p8', name: 'Csirkemell',        cat: 'csirke',   catLabel: 'Friss Csirkehús', price: 34, unit: 'kg', photoTint: 'chicken2' },
];

const CATEGORIES = [
  { key: 'osszes',     label: 'Összes' },
  { key: 'felvagott',  label: 'Felvágott & Egyéb' },
  { key: 'fustolt',    label: 'Füstölt Áruk' },
  { key: 'friss',      label: 'Friss Növendékhús' },
  { key: 'kolbasz',    label: 'Kolbász & Szalámi' },
  { key: 'csirke',     label: 'Friss Csirkehús' },
];

// SVG icons
const ICO = {
  heartOff: (s=20) => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>`,
  heartOn:  (s=20) => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>`,
  home:    (s=22,c='currentColor',sw=2) => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>`,
  pkg:     (s=22,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/></svg>`,
  cart:    (s=22,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/></svg>`,
  clipboard: (s=22,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>`,
  user:    (s=22,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>`,
  back:    (s=22,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>`,
  check:   (s=16,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  plus:    (s=18,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>`,
  wifi:    () => `<svg xmlns="http://www.w3.org/2000/svg" width="17" height="12" viewBox="0 0 17 12" fill="currentColor"><path d="M8.5 0C5.6 0 2.9 1 .8 2.8c-.3.2-.3.6 0 .8l1.4 1.4c.2.2.6.2.8 0C4.4 3.7 6.4 3 8.5 3s4.1.7 5.5 2c.2.2.6.2.8 0l1.4-1.4c.3-.2.3-.6 0-.8C14.1 1 11.4 0 8.5 0zm0 4.5c-1.9 0-3.7.6-5 1.8-.3.2-.3.6 0 .8l1.4 1.4c.2.2.6.2.8 0 .8-.7 1.7-1 2.8-1s2 .3 2.8 1c.2.2.6.2.8 0l1.4-1.4c.3-.2.3-.6 0-.8-1.3-1.2-3.1-1.8-5-1.8zm0 4.5c-.9 0-1.7.3-2.3.9-.3.2-.3.6 0 .9l1.9 1.9c.2.2.6.2.8 0l1.9-1.9c.3-.3.3-.7 0-.9-.6-.6-1.4-.9-2.3-.9z"/></svg>`,
};

// Meat photo — stylized SVG placeholder (until real photos are swapped in)
// Uses gradient + meat shape + vegetable accents to look like the screenshot style
function meatPhoto(tint) {
  const palettes = {
    'meat-pink':  { bg: '#F5E6DC', main: '#C67B6B', dark: '#8C4A3D', accent: '#4A7C35' },
    'meat-strip': { bg: '#F5E6DC', main: '#B86856', dark: '#7A3727', accent: '#4A7C35' },
    'sausage':    { bg: '#F7ECDC', main: '#8B3A1F', dark: '#4A1E0E', accent: '#4A7C35' },
    'ground':     { bg: '#F5DED2', main: '#D6989A', dark: '#A66670', accent: '#D84535' },
    'cut':        { bg: '#F5DFD5', main: '#C57676', dark: '#8A4444', accent: '#4A7C35' },
    'cut2':       { bg: '#F5E0D8', main: '#B0666A', dark: '#7A3840', accent: '#4A7C35' },
    'chicken':    { bg: '#FBF0DE', main: '#E8C48A', dark: '#B59057', accent: '#4A7C35' },
    'chicken2':   { bg: '#FBF0DE', main: '#EED4A8', dark: '#B59057', accent: '#4A7C35' },
  };
  const p = palettes[tint] || palettes['meat-pink'];

  // Different compositions per tint — still stylized but recognizable categories
  if (tint === 'sausage') {
    return `
      <div class="meat-photo" style="background:${p.bg}">
        <svg viewBox="0 0 200 170" preserveAspectRatio="xMidYMid slice">
          <!-- wooden board -->
          <ellipse cx="100" cy="130" rx="85" ry="18" fill="#A67B4D" opacity="0.6"/>
          <!-- sausage 1 -->
          <rect x="30" y="50" width="120" height="20" rx="10" fill="${p.main}" transform="rotate(-15, 90, 60)"/>
          <rect x="30" y="50" width="120" height="6" rx="3" fill="${p.dark}" transform="rotate(-15, 90, 60)" opacity="0.5"/>
          <!-- sausage 2 -->
          <rect x="35" y="75" width="120" height="22" rx="11" fill="${p.main}" transform="rotate(-10, 95, 86)"/>
          <!-- tomato accents -->
          <circle cx="160" cy="70" r="16" fill="#D84535"/>
          <circle cx="155" cy="65" r="5" fill="#E05C4A" opacity="0.6"/>
          <ellipse cx="160" cy="53" rx="10" ry="5" fill="${p.accent}"/>
          <!-- lettuce -->
          <path d="M 15 105 Q 35 90 55 108 Q 40 115 20 115 Z" fill="${p.accent}" opacity="0.85"/>
        </svg>
      </div>`;
  }
  if (tint === 'ground') {
    return `
      <div class="meat-photo" style="background:${p.bg}">
        <svg viewBox="0 0 200 170" preserveAspectRatio="xMidYMid slice">
          <ellipse cx="100" cy="100" rx="75" ry="40" fill="${p.main}"/>
          <ellipse cx="85" cy="90" rx="15" ry="8" fill="${p.dark}" opacity="0.3"/>
          <ellipse cx="115" cy="100" rx="18" ry="7" fill="${p.dark}" opacity="0.3"/>
          <ellipse cx="100" cy="110" rx="20" ry="8" fill="${p.dark}" opacity="0.25"/>
          <!-- tomatoes -->
          <circle cx="165" cy="75" r="18" fill="${p.accent}"/>
          <circle cx="160" cy="68" r="6" fill="#F06050" opacity="0.7"/>
          <ellipse cx="168" cy="55" rx="8" ry="4" fill="#4A7C35"/>
          <path d="M 18 105 Q 40 92 60 112 Q 45 118 25 118 Z" fill="#4A7C35" opacity="0.85"/>
        </svg>
      </div>`;
  }
  if (tint === 'chicken' || tint === 'chicken2') {
    return `
      <div class="meat-photo" style="background:${p.bg}">
        <svg viewBox="0 0 200 170" preserveAspectRatio="xMidYMid slice">
          <!-- drumsticks -->
          <ellipse cx="80" cy="100" rx="42" ry="20" fill="${p.main}"/>
          <ellipse cx="80" cy="95" rx="30" ry="12" fill="${p.dark}" opacity="0.3"/>
          <ellipse cx="55" cy="115" rx="10" ry="6" fill="#F5EBDA"/>
          <ellipse cx="125" cy="95" rx="38" ry="18" fill="${p.main}"/>
          <ellipse cx="125" cy="90" rx="25" ry="10" fill="${p.dark}" opacity="0.3"/>
          <ellipse cx="152" cy="105" rx="8" ry="5" fill="#F5EBDA"/>
          <!-- lettuce -->
          <path d="M 18 125 Q 40 108 60 128 Q 45 135 25 135 Z" fill="${p.accent}" opacity="0.8"/>
          <!-- tomato -->
          <circle cx="168" cy="130" r="12" fill="#D84535"/>
        </svg>
      </div>`;
  }
  // default: sliced meat with vegetable accent
  return `
    <div class="meat-photo" style="background:${p.bg}">
      <svg viewBox="0 0 200 170" preserveAspectRatio="xMidYMid slice">
        <!-- main meat slab -->
        <path d="M 40 55 Q 30 45 55 45 L 140 45 Q 170 45 170 70 L 170 115 Q 170 135 140 135 L 55 135 Q 35 135 35 115 Z" fill="${p.main}"/>
        <path d="M 50 65 Q 45 55 65 55 L 135 55 Q 160 55 160 75 L 160 110 Q 160 125 140 125 L 60 125 Q 45 125 45 110 Z" fill="${p.dark}" opacity="0.35"/>
        <!-- fat marbling -->
        <path d="M 60 75 Q 90 80 120 75 Q 130 85 100 90 Q 70 85 60 80 Z" fill="#FAF0E6" opacity="0.6"/>
        <path d="M 55 100 Q 95 105 140 100 Q 125 110 100 110 Q 70 108 55 100 Z" fill="#FAF0E6" opacity="0.5"/>
        <!-- tomato -->
        <circle cx="170" cy="75" r="16" fill="#D84535"/>
        <circle cx="165" cy="68" r="5" fill="#F06050" opacity="0.7"/>
        <ellipse cx="172" cy="57" rx="9" ry="4" fill="#4A7C35"/>
        <!-- lettuce -->
        <path d="M 10 105 Q 30 92 52 110 Q 38 118 18 118 Z" fill="${p.accent}" opacity="0.85"/>
      </svg>
    </div>`;
}
