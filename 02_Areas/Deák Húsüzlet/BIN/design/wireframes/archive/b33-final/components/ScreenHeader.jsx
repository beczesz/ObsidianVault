// ScreenHeader — 56 px white, bottom border, optional back + trailing slot.

const ScreenHeader = ({ title, onBack, trailing }) => (
  <header style={{
    height: 56,
    flexShrink: 0,
    background: 'var(--card)',
    borderBottom: '1px solid var(--border)',
    display: 'flex',
    alignItems: 'center',
    padding: '0 8px',
    gap: 4,
  }}>
    {onBack ? (
      <button onClick={onBack} aria-label="Vissza" style={{
        width: 44, height: 44, border: 0, background: 'transparent', cursor: 'pointer',
        display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
        color: 'var(--text)',
      }}>
        <Icon name="chevron-left" size={22} />
      </button>
    ) : <div style={{ width: 44 }} />}
    <h1 style={{
      flex: 1,
      fontSize: 'var(--fs-h1)',
      lineHeight: 'var(--lh-h1)',
      fontWeight: 'var(--fw-h1)',
      margin: 0,
      textAlign: onBack ? 'center' : 'left',
      paddingLeft: onBack ? 0 : 8,
    }}>{title}</h1>
    <div style={{ width: 44, display: 'flex', justifyContent: 'flex-end' }}>{trailing}</div>
  </header>
);

window.ScreenHeader = ScreenHeader;
