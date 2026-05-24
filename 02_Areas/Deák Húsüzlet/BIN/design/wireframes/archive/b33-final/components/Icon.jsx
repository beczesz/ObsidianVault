// Shared Lucide icon component for the mobile UI kit.
// Reuses the global `icon()` helper from /assets/icons.js.

const Icon = ({ name, size = 20, color, strokeWidth = 2, style }) => {
  const svg = window.icon(name, { size, color: color || 'currentColor', strokeWidth });
  return <span style={{ display: 'inline-flex', lineHeight: 0, color, ...style }} dangerouslySetInnerHTML={{ __html: svg }} />;
};

window.Icon = Icon;
