import React from 'react';
import { AlertTriangle, TrendingDown } from 'lucide-react';
import { formatINR } from '@/utils/money';

interface PenaltySlab3DProps {
  roomLimit: number;
  actualRate: number;
  proportionalDeduction: number;
  roomCategory: string;
}

export const PenaltySlab3D: React.FC<PenaltySlab3DProps> = ({
  roomLimit,
  actualRate,
  proportionalDeduction,
  roomCategory,
}) => {
  const isCapped = actualRate > roomLimit;
  const excess = Math.max(0, actualRate - roomLimit);
  const penaltyRatio = actualRate > 0 ? Math.round((excess / actualRate) * 100) : 0;

  return (
    <div
      className="paper-sheet"
      style={{
        padding: '16px',
        background: isCapped ? 'rgba(255, 75, 62, 0.04)' : 'var(--sheet)',
        border: '2px solid var(--ink)',
        position: 'relative',
        marginBottom: '16px',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <TrendingDown size={16} color={isCapped ? 'var(--red)' : 'var(--ink)'} />
          <span style={{ fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase' }}>
            Room Rent Proportionate Penalty Slab
          </span>
        </div>
        {isCapped ? (
          <span
            style={{
              fontSize: '0.6875rem',
              fontWeight: 900,
              background: 'var(--red)',
              color: '#FFFFFF',
              padding: '2px 6px',
              border: '1.5px solid var(--ink)',
            }}
          >
            {penaltyRatio}% SLAB PENALTY ACTIVE
          </span>
        ) : (
          <span
            style={{
              fontSize: '0.6875rem',
              fontWeight: 900,
              background: 'var(--lime)',
              color: '#111111',
              padding: '2px 6px',
              border: '1.5px solid var(--ink)',
            }}
          >
            NO PROPORTIONATE PENALTY
          </span>
        )}
      </div>

      {/* 2D/3D Visual Slab Comparison */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ width: '130px', fontSize: '0.75rem', fontWeight: 700 }}>
            Policy Cap:
          </div>
          <div style={{ flex: 1, background: 'var(--sheet-muted)', border: '1.5px solid var(--ink)', height: '20px', position: 'relative' }}>
            <div
              style={{
                width: '60%',
                height: '100%',
                background: 'var(--lime)',
                borderRight: '2px solid var(--ink)',
                display: 'flex',
                alignItems: 'center',
                paddingLeft: '6px',
                fontSize: '0.6875rem',
                fontWeight: 800,
              }}
            >
              {formatINR(roomLimit)}/day
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ width: '130px', fontSize: '0.75rem', fontWeight: 700 }}>
            Occupied ({roomCategory}):
          </div>
          <div style={{ flex: 1, background: 'var(--sheet-muted)', border: '1.5px solid var(--ink)', height: '20px', position: 'relative' }}>
            <div
              style={{
                width: `${Math.min(100, Math.round((actualRate / (roomLimit * 2)) * 100))}%`,
                height: '100%',
                background: isCapped ? 'var(--red)' : 'var(--lime)',
                borderRight: '2px solid var(--ink)',
                display: 'flex',
                alignItems: 'center',
                paddingLeft: '6px',
                fontSize: '0.6875rem',
                fontWeight: 800,
                color: isCapped ? '#FFFFFF' : '#111111',
              }}
            >
              {formatINR(actualRate)}/day
            </div>
          </div>
        </div>
      </div>

      {isCapped && (
        <div style={{ marginTop: '10px', fontSize: '0.75rem', color: 'var(--ink)', display: 'flex', alignItems: 'flex-start', gap: '6px' }}>
          <AlertTriangle size={14} color="var(--red)" style={{ marginTop: '2px', flexShrink: 0 }} />
          <span>
            Exceeding room cap triggers proportionate deductions across <strong>Surgeon, Anaesthesia, and OT fees</strong>, adding an estimated <strong>{formatINR(proportionalDeduction)}</strong> out-of-pocket loss.
          </span>
        </div>
      )}
    </div>
  );
};
