import React, { useEffect } from 'react';

interface ToastProps {
  message: string;
  type?: 'success' | 'error' | 'info';
  onClose: () => void;
  duration?: number;
}

export const Toast: React.FC<ToastProps> = ({
  message,
  type = 'success',
  onClose,
  duration = 3000,
}) => {
  useEffect(() => {
    const timer = setTimeout(onClose, duration);
    return () => clearTimeout(timer);
  }, [onClose, duration]);

  const getStyle = () => {
    switch (type) {
      case 'error':
        return { background: 'var(--red)', color: '#FFFFFF' };
      case 'info':
        return { background: 'var(--teal)', color: '#111111' };
      case 'success':
      default:
        return { background: 'var(--lime)', color: '#111111' };
    }
  };

  return (
    <div
      style={{
        position: 'fixed',
        bottom: '24px',
        right: '24px',
        padding: '12px 20px',
        fontWeight: 700,
        fontSize: '0.9375rem',
        border: 'var(--bw) solid var(--ink)',
        boxShadow: 'var(--shadow-md)',
        zIndex: 99999,
        display: 'flex',
        alignItems: 'center',
        gap: '10px',
        ...getStyle(),
      }}
      role="alert"
    >
      <span>{message}</span>
    </div>
  );
};
