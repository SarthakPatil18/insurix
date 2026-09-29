import React from 'react';
import { CalculationResult } from '@/types/estimate';
import { LedgerLine } from './LedgerLine';
import { formatINR } from '@/utils/money';
import { Receipt, CheckCircle, AlertTriangle } from 'lucide-react';

interface CostReceiptProps {
  result: CalculationResult | null;
  policyName: string;
}

export const CostReceipt: React.FC<CostReceiptProps> = ({ result, policyName }) => {
  if (!result) {
    return (
      <div
        className="receipt-container"
        style={{
          minHeight: '260px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          textAlign: 'center',
          opacity: 0.7,
        }}
      >
        <div>
          <Receipt size={36} style={{ marginBottom: '8px' }} />
          <div style={{ fontWeight: 800 }}>RECEIPT LEDGER READY</div>
          <div style={{ fontSize: '0.8125rem' }}>Select treatment parameters to compute itemized settlement</div>
        </div>
      </div>
    );
  }

  return (
    <div className="receipt-container">
      {/* Receipt Header */}
      <div style={{ textAlign: 'center', borderBottom: '2px solid var(--ink)', paddingBottom: '14px', marginBottom: '16px' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontWeight: 900, fontSize: '0.875rem', letterSpacing: '0.08em', textTransform: 'uppercase' }}>
          <Receipt size={16} />
          INSURIXX SETTLEMENT AUDIT RECEIPT
        </div>
        <div style={{ fontSize: '0.75rem', opacity: 0.75, marginTop: '2px' }}>
          Schedule Reference: {policyName}
        </div>
        <div style={{ fontSize: '0.6875rem', opacity: 0.6 }}>
          Time: {new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })} • 14-Rule Deterministic Pass
        </div>
      </div>

      {/* Top 3 Metric Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', marginBottom: '18px' }}>
        <div style={{ padding: '8px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)', textAlign: 'center' }}>
          <div style={{ fontSize: '0.6875rem', fontWeight: 800, textTransform: 'uppercase', opacity: 0.7 }}>
            Quoted Total
          </div>
          <div className="tabular-num" style={{ fontSize: '1.125rem', fontWeight: 900 }}>
            {formatINR(result.total_cost)}
          </div>
        </div>

        <div style={{ padding: '8px', background: 'var(--lime)', border: '2px solid var(--ink)', textAlign: 'center', color: '#111111' }}>
          <div style={{ fontSize: '0.6875rem', fontWeight: 900, textTransform: 'uppercase' }}>
            Insurer Pays
          </div>
          <div className="tabular-num" style={{ fontSize: '1.125rem', fontWeight: 900 }}>
            {formatINR(result.payable)}
          </div>
        </div>

        <div style={{ padding: '8px', background: result.out_of_pocket > 0 ? 'var(--red)' : 'var(--sheet-muted)', border: '2px solid var(--ink)', textAlign: 'center', color: result.out_of_pocket > 0 ? '#FFFFFF' : 'var(--ink)' }}>
          <div style={{ fontSize: '0.6875rem', fontWeight: 900, textTransform: 'uppercase' }}>
            You Pay
          </div>
          <div className="tabular-num" style={{ fontSize: '1.125rem', fontWeight: 900 }}>
            {formatINR(result.out_of_pocket)}
          </div>
        </div>
      </div>

      {/* Itemized Lines Breakdown */}
      <div style={{ marginBottom: '18px' }}>
        <div style={{ fontSize: '0.75rem', fontWeight: 900, textTransform: 'uppercase', letterSpacing: '0.04em', borderBottom: '1px solid var(--ink)', paddingBottom: '4px', marginBottom: '6px' }}>
          Itemized Disallowance Ledger
        </div>
        {result.lines.map((line, idx) => (
          <LedgerLine key={idx} line={line} />
        ))}
      </div>

      {/* Coverage Ratio Gauge */}
      <div style={{ padding: '10px 14px', background: 'var(--sheet-muted)', border: '2px solid var(--ink)', marginBottom: '16px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8125rem', fontWeight: 800, marginBottom: '6px' }}>
          <span>Coverage Admissibility</span>
          <span className="tabular-num">{result.pct}% Admissible</span>
        </div>
        <div style={{ height: '10px', background: 'var(--sheet)', border: '1.5px solid var(--ink)', overflow: 'hidden' }}>
          <div
            style={{
              height: '100%',
              width: `${Math.min(100, Math.max(0, result.pct))}%`,
              background: result.pct >= 80 ? 'var(--lime)' : result.pct >= 50 ? 'var(--yellow)' : 'var(--red)',
              transition: 'width 0.3s ease',
            }}
          />
        </div>
      </div>

      {/* Trace Proof List */}
      {result.trace && result.trace.length > 0 && (
        <div style={{ fontSize: '0.75rem', opacity: 0.85, marginTop: '12px' }}>
          <div style={{ fontWeight: 800, textTransform: 'uppercase', marginBottom: '4px' }}>Deterministic Audit Trace:</div>
          <ul style={{ paddingLeft: '18px', display: 'flex', flexDirection: 'column', gap: '2px' }}>
            {result.trace.map((t, idx) => (
              <li key={idx}>{t}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Legal Fine Print Note */}
      <div style={{ fontSize: '0.6875rem', opacity: 0.6, marginTop: '16px', textAlign: 'center', lineHeight: 1.3 }}>
        Reconciled against IRDAI Non-Medical Guidelines (Annexure 1). Final cashless or reimbursement approval depends on hospital discharge summary and TPA scrutiny.
      </div>
    </div>
  );
};
