import React from 'react';
import { DeductionLine } from '@/types/estimate';
import { formatINR } from '@/utils/money';

interface LedgerLineProps {
  line: DeductionLine;
}

export const LedgerLine: React.FC<LedgerLineProps> = ({ line }) => {
  const isSub = line.kind === 'sub';
  const isTotal = line.kind === 'total';
  const isInfo = line.kind === 'info';

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: isTotal ? '10px 0' : '6px 0',
        borderBottom: isTotal ? '3px double var(--ink)' : '1px dashed rgba(17, 17, 17, 0.25)',
        borderTop: isTotal ? '2px solid var(--ink)' : 'none',
        marginTop: isTotal ? '6px' : '0',
        fontWeight: isTotal ? 900 : 600,
        fontSize: isTotal ? '1.0625rem' : '0.875rem',
      }}
    >
      <span style={{ color: isSub ? 'var(--ink)' : 'inherit', display: 'flex', alignItems: 'center', gap: '6px' }}>
        {isSub && <span style={{ color: 'var(--red)', fontWeight: 900 }}>—</span>}
        {line.label}
      </span>
      <span
        className="tabular-num"
        style={{
          color: isSub ? 'var(--red)' : isTotal ? 'var(--ink)' : 'inherit',
          fontWeight: isTotal ? 900 : 700,
        }}
      >
        {isSub ? `— ${formatINR(line.amount)}` : formatINR(line.amount)}
      </span>
    </div>
  );
};
