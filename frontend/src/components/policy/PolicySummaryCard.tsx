import React from 'react';
import { Policy } from '@/types/policy';
import { Card } from '../ui/Card';
import { formatLakhs } from '@/utils/money';

interface PolicySummaryCardProps {
  policy: Policy;
}

export const PolicySummaryCard: React.FC<PolicySummaryCardProps> = ({ policy }) => {
  return (
    <Card headerTag="POLICY SCHEDULE" tagColor="lime" style={{ marginBottom: '24px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '12px', borderBottom: '2px solid var(--ink)', paddingBottom: '12px', marginBottom: '14px' }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: 900 }}>{policy.policy_name}</h2>
          <div style={{ fontSize: '0.875rem', opacity: 0.75 }}>{policy.insurer} • Schedule Form IRDAI/NL-HLT</div>
        </div>
        <div style={{ textAlign: 'right' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', display: 'block' }}>Sum Insured</span>
          <span className="tabular-num" style={{ fontSize: '1.5rem', fontWeight: 900, color: 'var(--ink)' }}>
            {formatLakhs(policy.sum_insured)}
          </span>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
        <div style={{ padding: '8px 12px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)' }}>
          <span style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7, display: 'block' }}>
            Room Rent Limit
          </span>
          <span style={{ fontSize: '0.875rem', fontWeight: 800 }}>{policy.room_rent_limit}</span>
        </div>

        <div style={{ padding: '8px 12px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)' }}>
          <span style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7, display: 'block' }}>
            ICU Capping
          </span>
          <span style={{ fontSize: '0.875rem', fontWeight: 800 }}>{policy.icu_limit}</span>
        </div>

        <div style={{ padding: '8px 12px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)' }}>
          <span style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7, display: 'block' }}>
            Pre-Existing Disease Clock
          </span>
          <span style={{ fontSize: '0.875rem', fontWeight: 800 }}>{policy.waiting_periods.pre_existing}</span>
        </div>

        <div style={{ padding: '8px 12px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)' }}>
          <span style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7, display: 'block' }}>
            Specific Surgeries Clock
          </span>
          <span style={{ fontSize: '0.875rem', fontWeight: 800 }}>{policy.waiting_periods.specific_diseases}</span>
        </div>

        <div style={{ padding: '8px 12px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)' }}>
          <span style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7, display: 'block' }}>
            Cataract Sub-limit
          </span>
          <span style={{ fontSize: '0.875rem', fontWeight: 800 }}>{policy.sub_limits.cataract}</span>
        </div>

        <div style={{ padding: '8px 12px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)' }}>
          <span style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7, display: 'block' }}>
            Co-Payment Rule
          </span>
          <span style={{ fontSize: '0.875rem', fontWeight: 800 }}>{policy.co_payment}</span>
        </div>
      </div>
    </Card>
  );
};
