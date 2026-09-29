import React from 'react';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'sheet' | 'hero' | 'muted' | 'danger' | 'evidence';
  headerTag?: string;
  tagColor?: 'lime' | 'red' | 'teal' | 'lilac';
}

export const Card: React.FC<CardProps> = ({
  variant = 'sheet',
  headerTag,
  tagColor = 'lime',
  children,
  className = '',
  style,
  ...props
}) => {
  const getVariantClass = () => {
    switch (variant) {
      case 'hero':
        return 'paper-sheet paper-sheet-hero';
      case 'danger':
        return 'paper-sheet';
      case 'evidence':
        return 'paper-sheet';
      case 'muted':
      case 'sheet':
      default:
        return 'paper-sheet';
    }
  };

  const getTagColor = () => {
    switch (tagColor) {
      case 'red': return 'var(--red)';
      case 'teal': return 'var(--teal)';
      case 'lilac': return 'var(--lilac)';
      case 'lime':
      default:
        return 'var(--lime)';
    }
  };

  return (
    <div
      className={`${getVariantClass()} ${className}`}
      style={{
        padding: '20px',
        position: 'relative',
        ...style,
      }}
      {...props}
    >
      {headerTag && (
        <span
          style={{
            position: 'absolute',
            top: '-12px',
            right: '16px',
            background: getTagColor(),
            color: '#111111',
            border: '2px solid var(--ink)',
            padding: '2px 8px',
            fontSize: '0.75rem',
            fontWeight: 800,
            textTransform: 'uppercase',
            boxShadow: '2px 2px 0 var(--ink)',
          }}
        >
          {headerTag}
        </span>
      )}
      {children}
    </div>
  );
};
