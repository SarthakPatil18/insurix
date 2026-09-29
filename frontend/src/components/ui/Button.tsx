import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost' | 'lime';
  size?: 'sm' | 'md' | 'lg';
  icon?: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'secondary',
  size = 'md',
  icon,
  children,
  className = '',
  disabled,
  style,
  ...props
}) => {
  const getVariantStyle = (): React.CSSProperties => {
    switch (variant) {
      case 'primary':
      case 'lime':
        return {
          background: 'var(--lime)',
          color: '#111111',
          borderColor: 'var(--ink)',
        };
      case 'danger':
        return {
          background: 'var(--red)',
          color: '#FFFFFF',
          borderColor: 'var(--ink)',
        };
      case 'ghost':
        return {
          background: 'transparent',
          boxShadow: 'none',
          borderColor: 'transparent',
        };
      case 'secondary':
      default:
        return {
          background: 'var(--sheet)',
          color: 'var(--ink)',
          borderColor: 'var(--ink)',
        };
    }
  };

  const getSizeStyle = (): React.CSSProperties => {
    switch (size) {
      case 'sm':
        return { padding: '4px 10px', fontSize: '0.8125rem' };
      case 'lg':
        return { padding: '12px 24px', fontSize: '1.0625rem' };
      case 'md':
      default:
        return { padding: '8px 16px', fontSize: '0.9375rem' };
    }
  };

  return (
    <button
      className={`btn ${className}`}
      disabled={disabled}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '8px',
        borderWidth: 'var(--bw)',
        borderStyle: 'solid',
        ...getVariantStyle(),
        ...getSizeStyle(),
        ...style,
      }}
      {...props}
    >
      {icon && <span style={{ display: 'inline-flex' }}>{icon}</span>}
      {children}
    </button>
  );
};
