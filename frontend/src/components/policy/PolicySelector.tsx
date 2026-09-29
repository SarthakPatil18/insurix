import React from 'react';
import { Policy } from '@/types/policy';
import { Shield } from 'lucide-react';

interface PolicySelectorProps {
  policies: Policy[];
  activePolicyId: string;
  onSelectPolicy: (id: string) => void;
}

export const PolicySelector: React.FC<PolicySelectorProps> = ({
  policies,
  activePolicyId,
  onSelectPolicy,
}) => {
  return (
    <div style={{ marginBottom: '20px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
        <label style={{ fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
          Select Active Policy Wordings
        </label>
        <span style={{ fontSize: '0.75rem', fontWeight: 600, opacity: 0.7 }}>
          IRDAI-Aligned Schedule
        </span>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px' }}>
        {policies.map((p) => {
          const isActive = p.id === activePolicyId;
          return (
            <div
              key={p.id}
              onClick={() => onSelectPolicy(p.id)}
              className="paper-sheet"
              style={{
                padding: '12px 14px',
                cursor: 'pointer',
                background: isActive ? 'var(--sheet)' : 'var(--sheet-muted)',
                borderColor: 'var(--ink)',
                borderWidth: isActive ? '3.5px' : '2px',
                boxShadow: isActive ? '4px 4px 0 var(--ink)' : '2px 2px 0 var(--ink)',
                transform: isActive ? 'translate(-2px, -2px)' : 'none',
                transition: 'all 0.1s ease',
              }}
              role="button"
              tabIndex={0}
              aria-pressed={isActive}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  onSelectPolicy(p.id);
                }
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '4px' }}>
                <span
                  style={{
                    fontSize: '0.75rem',
                    fontWeight: 900,
                    padding: '2px 6px',
                    background: isActive ? 'var(--lime)' : 'var(--sheet)',
                    border: '1.5px solid var(--ink)',
                    color: '#111111',
                  }}
                >
                  {p.tag}
                </span>
                {isActive && <Shield size={14} color="var(--ink)" />}
              </div>
              <div style={{ fontWeight: 800, fontSize: '0.9375rem', lineHeight: 1.2, marginTop: '4px' }}>
                {p.insurer}
              </div>
              <div style={{ fontSize: '0.75rem', opacity: 0.8, marginTop: '4px' }}>
                {p.short_desc}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
