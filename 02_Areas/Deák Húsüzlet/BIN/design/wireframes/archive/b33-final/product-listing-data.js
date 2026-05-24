// ====================================================================
// DH v0.4 — Termékek oldal explorations — Product data
// ====================================================================
// Categories: Friss / Füstölt / Felvágott / Kolbász / Fűszer
// ====================================================================

const PRODUCTS = [
  // FRISS
  { id: 'P001', name: 'Sertéstarja',       cat: 'friss',    catLabel: 'Friss',     price: 38, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P002', name: 'Csirkecomb',        cat: 'friss',    catLabel: 'Friss',     price: 28, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P003', name: 'Csirkeszárny',      cat: 'friss',    catLabel: 'Friss',     price: 22, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P004', name: 'Sertéskaraj',       cat: 'friss',    catLabel: 'Friss',     price: 42, unit: 'RON/kg', oldPrice: 48,   badge: 'sale', isNew: false, stock: 'in'  },
  { id: 'P005', name: 'Marhalapocka',      cat: 'friss',    catLabel: 'Friss',     price: 58, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: true,  stock: 'in'  },
  { id: 'P006', name: 'Pulykamell',        cat: 'friss',    catLabel: 'Friss',     price: 45, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'oos' },

  // FÜSTÖLT
  { id: 'P010', name: 'Füstölt Szalonna',  cat: 'fustolt',  catLabel: 'Füstölt',   price: 42, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P011', name: 'Füstölt Sonka',     cat: 'fustolt',  catLabel: 'Füstölt',   price: 55, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P012', name: 'Füstölt Csülök',    cat: 'fustolt',  catLabel: 'Füstölt',   price: 34, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P013', name: 'Füstölt Oldalas',   cat: 'fustolt',  catLabel: 'Füstölt',   price: 48, unit: 'RON/kg', oldPrice: 52,   badge: 'sale', isNew: false, stock: 'in'  },
  { id: 'P014', name: 'Abált Szalonna',    cat: 'fustolt',  catLabel: 'Füstölt',   price: 35, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },

  // FELVÁGOTT
  { id: 'P020', name: 'Parasztsonka',      cat: 'felvagott', catLabel: 'Felvágott', price: 68, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P021', name: 'Párizsi',           cat: 'felvagott', catLabel: 'Felvágott', price: 32, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P022', name: 'Téliszalámi',       cat: 'felvagott', catLabel: 'Felvágott', price: 72, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: true,  stock: 'in'  },
  { id: 'P023', name: 'Krinolin',          cat: 'felvagott', catLabel: 'Felvágott', price: 38, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },

  // KOLBÁSZ
  { id: 'P030', name: 'Deák Házikolbász',  cat: 'kolbasz',  catLabel: 'Kolbász',   price: 45, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P031', name: 'Cérna Kolbász',     cat: 'kolbasz',  catLabel: 'Kolbász',   price: 48, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P032', name: 'Sütőkolbász',       cat: 'kolbasz',  catLabel: 'Kolbász',   price: 45, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },
  { id: 'P033', name: 'Csabai Kolbász',    cat: 'kolbasz',  catLabel: 'Kolbász',   price: 62, unit: 'RON/kg', oldPrice: 68,   badge: 'sale', isNew: false, stock: 'in'  },
  { id: 'P034', name: 'Cseh Virsli',       cat: 'kolbasz',  catLabel: 'Kolbász',   price: 42, unit: 'RON/kg', oldPrice: null, badge: null,   isNew: false, stock: 'in'  },

  // FŰSZER
  { id: 'P040', name: 'Grill fűszerkeverék',    cat: 'fuszer', catLabel: 'Fűszer', price: 15, unit: 'RON / 50g', oldPrice: null, badge: null, isNew: false, stock: 'in' },
  { id: 'P041', name: 'Pirospaprika (édes)',    cat: 'fuszer', catLabel: 'Fűszer', price: 22, unit: 'RON / 100g',oldPrice: null, badge: null, isNew: false, stock: 'in' },
  { id: 'P042', name: 'BBQ Szósz',              cat: 'fuszer', catLabel: 'Fűszer', price: 18, unit: 'RON / 250ml',oldPrice: null, badge: null, isNew: true,  stock: 'in' },
  { id: 'P043', name: 'Tormakrém',              cat: 'fuszer', catLabel: 'Fűszer', price: 14, unit: 'RON / 200g',oldPrice: null, badge: null, isNew: false, stock: 'in' },
];

const CATEGORIES = [
  { key: 'friss',     label: 'Friss',     count: 6, tint: 'friss'     },
  { key: 'fustolt',   label: 'Füstölt',   count: 5, tint: 'fustolt'   },
  { key: 'felvagott', label: 'Felvágott', count: 4, tint: 'felvagott' },
  { key: 'kolbasz',   label: 'Kolbász',   count: 5, tint: 'kolbasz'   },
  { key: 'fuszer',    label: 'Fűszer',    count: 4, tint: 'fuszer'    },
];

const BUNDLES = [
  { name: 'Családi Grill',      size: '3-4 fős',  items: 5, price: 150, saving: 10 },
  { name: 'Maxi Családi Grill', size: '6-8 fős',  items: 8, price: 300, saving: 16 },
];

// Hero banners (admin-editable)
const HEROES = [
  {
    eyebrow: 'Grillszezon',
    title: 'Tökéletes tarja — mindig friss',
    sub: '-15% a sertéstarján április 25-ig',
    tint: 's1',
    cta: 'Megnézem',
  },
  {
    eyebrow: 'Új érkezés',
    title: 'Téliszalámi — kézműves',
    sub: 'Csak néhány szelet hetente',
    tint: 's2',
    cta: 'Kipróbálom',
  },
  {
    eyebrow: 'Húsvéti ajánlat',
    title: 'Füstölt Sonka — családi méret',
    sub: 'Előrendelés április 30-ig',
    tint: 's3',
    cta: 'Előrendelem',
  },
];

// Lucide SVG icons used in this file
const ICO = {
  search:   (s=16,c='var(--text2)') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>`,
  filter:   (s=14,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>`,
  sort:     (s=14,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M7 12h10"/><path d="M10 18h4"/></svg>`,
  heart:    (s=16,c='#777',fill='none') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="${fill}" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>`,
  plus:     (s=16,c='white',w=2.5) => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>`,
  cart:     (s=20,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/></svg>`,
  home:     (s=20,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>`,
  pkg:      (s=20,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/></svg>`,
  user:     (s=20,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>`,
  truck:    (s=14,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></svg>`,
  chevR:    (s=14,c='currentColor') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>`,
  flame:    (s=14,c='#7B2D3B',w=2) => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3q1 4 4 6.5t3 5.5a1 1 0 0 1-14 0 5 5 0 0 1 1-3 1 1 0 0 0 5 0c0-2-1.5-3-1.5-5q0-2 2.5-4"/></svg>`,
  piggy:    (s=18,c='white') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13.744 17.736a6 6 0 1 1-7.48-7.48"/><path d="M15 6h1v4"/><path d="m6.134 14.768.866-.5 2 3.464"/><circle cx="16" cy="8" r="6"/></svg>`,
  bell:     (s=18,c='var(--text)') => `<svg xmlns="http://www.w3.org/2000/svg" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.268 21a2 2 0 0 0 3.464 0"/><path d="M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326"/></svg>`,
  wifi:     () => `<svg xmlns="http://www.w3.org/2000/svg" width="13" height="9" viewBox="0 0 13 9" fill="currentColor"><rect x="0" y="5" width="2" height="4" rx="0.5"/><rect x="3" y="3" width="2" height="6" rx="0.5"/><rect x="6" y="1" width="2" height="8" rx="0.5"/><rect x="9" y="0" width="2" height="9" rx="0.5"/></svg>`,
  battery:  () => `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="10" viewBox="0 0 20 10" fill="none"><rect x="0.5" y="0.5" width="17" height="9" rx="2" stroke="currentColor"/><rect x="2" y="2" width="13" height="6" rx="1" fill="currentColor"/><rect x="18.5" y="3.5" width="1.5" height="3" rx="0.5" fill="currentColor"/></svg>`,
};

// Stylized meat image — inline SVG for consistent look (placeholder until real photos)
function meatImg(cat, label, { small = false } = {}) {
  const ls = small ? '9px' : '10px';
  return `<div class="meat-img ${cat}"><span class="mi-label" style="font-size:${ls}">${label.toUpperCase()}</span></div>`;
}
