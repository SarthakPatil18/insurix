import React from 'react';

interface BadgeProps {
  color?: 'lime' | 'red' | 'teal' | 'lilac' | 'neutral';
  children: React.ReactNode;
  className?: string;
  dashed?: boolean;
}

export const Badge: React.FC<BadgeProps> = ({
  color = 'lime',
  children,
  className = '',
  dashed = false,
}) => {
  const getBadgeStyle = (): React.CSSProperties => {
    switch (color) {
      case 'red':
        return { background: 'var(--red)', color: '#FFFFFF' };
      case 'teal':
        return { background: 'var(--teal)', color: '#111111' };
      case 'lilac':
        return { background: 'var(--lilac)', color: '#111111' };
      case 'neutral':
        return { background: 'var(--sheet-muted)', color: 'var(--ink)' };
      case 'lime':
      default:
        return { background: 'var(--lime)', color: '#111111' };
    }
  };

  return (
    <span
      className={`badge ${className}`}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        padding: '3px 8px',
        fontSize: '0.75rem',
        fontWeight: 800,
        textTransform: 'uppercase',
        letterSpacing: '0.04em',
        border: dashed ? '2px dashed var(--ink)' : '2px solid var(--ink)',
        boxShadow: '2px 2px 0 var(--ink)',
        borderRadius: 'var(--radius-sticker)',
        ...getBadgeStyle(),
      }}
    >
      {children}
    </span>
  );
};
