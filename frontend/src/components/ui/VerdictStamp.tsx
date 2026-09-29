import React from 'react';
import { VerdictType } from '@/types/query';

interface VerdictStampProps {
  verdict: VerdictType;
  label?: string;
  className?: string;
  size?: 'sm' | 'md' | 'lg';
}

export const VerdictStamp: React.FC<VerdictStampProps> = ({
  verdict,
  label,
  className = '',
  size = 'md',
}) => {
  let displayLabel = label;
  if (!displayLabel) {
    switch (verdict) {
      case 'covered':
        displayLabel = 'COVERED';
        break;
      case 'excluded':
        displayLabel = 'EXCLUDED';
        break;
      case 'conditional':
        displayLabel = 'CONDITIONAL';
        break;
      case 'uncertain':
      default:
        displayLabel = 'UNCERTAIN';
        break;
    }
  }

  const getStampClass = () => {
    switch (verdict) {
      case 'covered':
        return 'stamp-covered';
      case 'excluded':
        return 'stamp-excluded';
      case 'conditional':
        return 'stamp-conditional';
      case 'uncertain':
      default:
        return 'stamp-uncertain';
    }
  };

  const getSizeStyle = () => {
    switch (size) {
      case 'sm':
        return { fontSize: '0.75rem', padding: '3px 8px', borderWidth: '2px' };
      case 'lg':
        return { fontSize: '1.25rem', padding: '8px 18px', borderWidth: '5px' };
      case 'md':
      default:
        return { fontSize: '0.9375rem', padding: '5px 12px', borderWidth: '3.5px' };
    }
  };

  return (
    <div
      className={`verdict-stamp ${getStampClass()} ${className}`}
      style={getSizeStyle()}
      role="status"
      aria-label={`Verdict: ${displayLabel}`}
    >
      {displayLabel}
    </div>
  );
};
