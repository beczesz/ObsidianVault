// Badge — status/semantic. SavingsBadge — coins + -X RON green chip.

const BADGE_STYLES = {
  delivered: { color: 'var(--green)',  background: 'var(--green-light)'  },
  progress:  { color: 'var(--warn)',   background: 'var(--warn-light)'   },
  new:       { color: 'var(--info)',   background: 'var(--info-light)'   },
  cancelled: { color: 'var(--danger)', background: 'var(--danger-light)' },
  favorite:  { color: 'var(--gold)',   background: 'var(--gold-light)'   },
};

const Badge = ({ tone = 'delivered', children }) => (
  <span style={{
    display: 'inline-flex', alignItems: 'center', gap: 4,
    padding: '3px 10px', borderRadius: 999,
    fontSize: 12, fontWeight: 600, lineHeight: 1.25,
    ...BADGE_STYLES[tone],
  }}>{children}</span>
);

const SavingsBadge = ({ amount }) => (
  <div style={{
    visibility: amount > 0 ? 'visible' : 'hidden',
    background: 'var(--green)', borderRadius: 14,
    padding: '8px 12px', minWidth: 64,
    display: 'inline-flex', flexDirection: 'column', alignItems: 'center', gap: 2,
    color: '#fff',
  }}>
    <Icon name="coins" size={24} color="#fff" />
    <span style={{ fontSize: 12, fontWeight: 800, letterSpacing: 0.2 }}>-{amount} RON</span>
  </div>
);

window.Badge = Badge;
window.SavingsBadge = SavingsBadge;
