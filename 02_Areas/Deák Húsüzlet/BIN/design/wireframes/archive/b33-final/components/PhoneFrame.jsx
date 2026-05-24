// PhoneFrame — 375×812 rounded bezel with iOS status bar.
// Children are rendered inside a scrollable screen area (375×812 - header - tabbar).

const PhoneFrame = ({ children, style }) => (
  <div style={{
    width: 375,
    height: 812,
    background: 'var(--card)',
    borderRadius: 36,
    border: '10px solid #1a1a1a',
    boxShadow: '0 10px 40px rgba(0,0,0,0.18)',
    overflow: 'hidden',
    position: 'relative',
    fontFamily: 'var(--font-sans)',
    color: 'var(--text)',
    ...style,
  }}>
    <StatusBar />
    <div style={{ height: 'calc(100% - 44px)', display: 'flex', flexDirection: 'column' }}>
      {children}
    </div>
  </div>
);

const StatusBar = () => (
  <div style={{
    height: 44,
    display: 'flex',
    alignItems: 'flex-end',
    justifyContent: 'space-between',
    padding: '0 22px 6px',
    fontSize: 14,
    fontWeight: 600,
    color: 'var(--text)',
    background: 'var(--card)',
  }}>
    <span>9:41</span>
    <span style={{ display: 'inline-flex', gap: 5, alignItems: 'center' }}>
      <span style={{ width: 16, height: 10, background: 'var(--text)', clipPath: 'polygon(0 60%, 25% 60%, 25% 30%, 50% 30%, 50% 10%, 75% 10%, 75% 0, 100% 0, 100% 100%, 0 100%)' }} />
      <span style={{ width: 22, height: 10, border: '1px solid var(--text)', borderRadius: 2, position: 'relative' }}>
        <span style={{ position: 'absolute', inset: 1, background: 'var(--text)', width: 14, borderRadius: 1 }} />
      </span>
    </span>
  </div>
);

window.PhoneFrame = PhoneFrame;
