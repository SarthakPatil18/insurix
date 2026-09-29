import React from 'react';
import { Clock, CheckCircle2, Lock } from 'lucide-react';

interface WaitingDial3DProps {
  tenureMonths: number;
  requiredMonths?: number;
  label?: string;
}

export const WaitingDial3D: React.FC<WaitingDial3DProps> = ({
  tenureMonths,
  requiredMonths = 24,
  label = 'Specific Surgery Waiting Clock',
}) => {
  const isSatisfied = tenureMonths >= requiredMonths;
  const pct = Math.min(100, Math.round((tenureMonths / requiredMonths) * 100));

  return (
    <div
      style={{
        padding: '12px 14px',
        background: isSatisfied ? 'rgba(221, 242, 71, 0.15)' : 'rgba(255, 75, 62, 0.08)',
        border: '2px solid var(--ink)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: '12px',
        marginBottom: '14px',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        {isSatisfied ? (
          <CheckCircle2 size={18} color="var(--ink)" />
        ) : (
          <Lock size={18} color="var(--red)" />
        )}
        <div>
          <div style={{ fontSize: '0.8125rem', fontWeight: 800 }}>
            {label} ({requiredMonths} Months)
          </div>
          <div style={{ fontSize: '0.6875rem', opacity: 0.8 }}>
            Current continuous active policy tenure: <strong>{tenureMonths} months</strong>
          </div>
        </div>
      </div>

      <div style={{ textAlign: 'right' }}>
        <span
          style={{
            fontSize: '0.75rem',
            fontWeight: 900,
            padding: '2px 8px',
            background: isSatisfied ? 'var(--lime)' : 'var(--red)',
            color: isSatisfied ? '#111111' : '#FFFFFF',
            border: '1.5px solid var(--ink)',
            textTransform: 'uppercase',
          }}
        >
          {isSatisfied ? 'Clock Satisfied' : 'Waiting Active'}
        </span>
      </div>
    </div>
  );
};
