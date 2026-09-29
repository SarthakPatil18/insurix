import React from 'react';
import { Pin } from 'lucide-react';
import { EvidenceCitation } from '@/types/query';

interface RedStringBoardProps {
  evidence: EvidenceCitation[];
  verdictLabel: string;
  totalCost?: number;
  payable?: number;
}

export const RedStringBoard: React.FC<RedStringBoardProps> = ({
  evidence,
  verdictLabel,
  totalCost,
  payable,
}) => {
  return (
    <div
      className="paper-sheet"
      style={{
        padding: '20px',
        background: 'var(--sheet)',
        borderWidth: 'var(--bw)',
        position: 'relative',
        overflow: 'hidden',
        boxShadow: 'var(--shadow-md)',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '14px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Pin size={18} color="var(--red)" style={{ transform: 'rotate(45deg)' }} />
          <span style={{ fontWeight: 900, fontSize: '0.875rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
            Evidence Lab Board • Red-String Trace
          </span>
        </div>
        <span
          style={{
            fontSize: '0.6875rem',
            fontWeight: 800,
            background: 'var(--teal)',
            color: '#111111',
            padding: '2px 8px',
            border: '1.5px solid var(--ink)',
          }}
        >
          {evidence.length} PINNED CLAUSES
        </span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', position: 'relative' }}>
        {/* Visual Red String Indicator */}
        <div
          style={{
            position: 'absolute',
            left: '19px',
            top: '16px',
            bottom: '16px',
            width: '2px',
            background: 'var(--red)',
            zIndex: 1,
            boxShadow: '0 0 4px rgba(255, 75, 62, 0.4)',
          }}
        />

        {evidence.map((item, idx) => (
          <div
            key={idx}
            style={{
              display: 'flex',
              alignItems: 'flex-start',
              gap: '14px',
              position: 'relative',
              zIndex: 2,
            }}
          >
            {/* Red Thumbtack Pin */}
            <div
              style={{
                width: '12px',
                height: '12px',
                borderRadius: '50%',
                background: 'var(--red)',
                border: '2px solid var(--ink)',
                marginTop: '6px',
                boxShadow: '1px 1px 0 var(--ink)',
                flexShrink: 0,
              }}
            />

            <div
              style={{
                flex: 1,
                padding: '10px 14px',
                background: 'var(--sheet-muted)',
                border: '2px solid var(--ink)',
                fontSize: '0.875rem',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
                <span style={{ fontWeight: 800, color: 'var(--ink)' }}>
                  Pin #{idx + 1} — Page {item.page}, Section {item.section}
                </span>
                {item.score && (
                  <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--muted-text)' }}>
                    Cosine: {item.score.toFixed(1)}
                  </span>
                )}
              </div>
              <p className="clause-quote" style={{ margin: 0, fontSize: '0.875rem', opacity: 0.9 }}>
                "{item.text}"
              </p>
            </div>
          </div>
        ))}

        {/* Conclusion Node */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px', zIndex: 2, marginTop: '4px' }}>
          <div
            style={{
              width: '12px',
              height: '12px',
              background: 'var(--lime)',
              border: '2px solid var(--ink)',
              borderRadius: '2px',
              flexShrink: 0,
            }}
          />
          <div
            style={{
              padding: '6px 12px',
              background: 'var(--sheet)',
              border: '2px solid var(--ink)',
              fontWeight: 800,
              fontSize: '0.8125rem',
              display: 'flex',
              gap: '12px',
            }}
          >
            <span>Trace Verdict: <strong style={{ color: 'var(--ink)' }}>{verdictLabel}</strong></span>
            {payable !== undefined && totalCost !== undefined && (
              <span className="tabular-num">Payable Ratio: {Math.round((payable / totalCost) * 100)}%</span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
