// BottomNav — 4 tabs: Termékek / Kosár / Rendelések / Fiók.

const TABS = [
  { key: 'products', label: 'Termékek',   icon: 'package-2' },
  { key: 'cart',     label: 'Kosár',      icon: 'shopping-cart' },
  { key: 'orders',   label: 'Rendelések', icon: 'list' },
  { key: 'profile',  label: 'Fiók',       icon: 'user' },
];

const BottomNav = ({ active, onChange, cartCount = 0 }) => (
  <nav style={{
    height: 65,
    flexShrink: 0,
    background: 'var(--card)',
    borderTop: '1px solid var(--border)',
    boxShadow: 'var(--shadow-bottom-nav)',
    display: 'grid',
    gridTemplateColumns: 'repeat(4, 1fr)',
  }}>
    {TABS.map(t => {
      const isActive = active === t.key;
      const color = isActive ? 'var(--primary)' : 'var(--text-muted)';
      return (
        <button key={t.key} onClick={() => onChange(t.key)} style={{
          position: 'relative',
          border: 0, background: 'transparent', cursor: 'pointer',
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
          gap: 4, color, fontSize: 10, fontWeight: 600, fontFamily: 'var(--font-sans)',
        }}>
          {isActive && (
            <span style={{
              position: 'absolute', top: 6, left: '50%', transform: 'translateX(-50%)',
              width: 24, height: 3, borderRadius: 999, background: 'var(--primary)',
            }} />
          )}
          <span style={{ position: 'relative' }}>
            <Icon name={t.icon} size={22} color={color} />
            {t.key === 'cart' && cartCount > 0 && (
              <span style={{
                position: 'absolute', top: -6, right: -10,
                minWidth: 16, height: 16, padding: '0 4px',
                background: 'var(--primary)', color: '#fff',
                borderRadius: 999, fontSize: 10, fontWeight: 700,
                display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
              }}>{cartCount}</span>
            )}
          </span>
          <span>{t.label}</span>
        </button>
      );
    })}
  </nav>
);

window.BottomNav = BottomNav;
