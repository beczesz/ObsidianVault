// Button — primary (48h), secondary (38h, 2px border), ghost (38h, underline).

const Button = ({ variant = 'primary', leadingIcon, block, disabled, children, onClick, style }) => {
  const base = {
    display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 8,
    padding: '0 20px', borderRadius: 12,
    fontFamily: 'var(--font-sans)', fontSize: 15, fontWeight: 600, lineHeight: 1,
    cursor: disabled ? 'default' : 'pointer',
    border: 0, width: block ? '100%' : 'auto',
    transition: 'background 180ms var(--ease-out), box-shadow 180ms var(--ease-out)',
  };
  const variants = {
    primary: {
      height: 48, background: disabled ? 'var(--disabled-bg)' : 'var(--primary)',
      color: '#fff',
    },
    secondary: {
      height: 38, background: 'transparent',
      color: 'var(--primary)', border: '2px solid var(--primary)',
    },
    ghost: {
      height: 38, background: 'transparent',
      color: 'var(--primary)', textDecoration: 'underline',
    },
  };
  return (
    <button onClick={disabled ? undefined : onClick} disabled={disabled}
            style={{ ...base, ...variants[variant], ...style }}>
      {leadingIcon && <Icon name={leadingIcon} size={18} color="currentColor" />}
      {children}
    </button>
  );
};

window.Button = Button;
