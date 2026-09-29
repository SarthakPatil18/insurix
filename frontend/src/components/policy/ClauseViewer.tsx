import React from 'react';
import { Clause } from '@/types/policy';
import { Modal } from '../ui/Modal';
import { Badge } from '../ui/Badge';
import { BookOpen } from 'lucide-react';

interface ClauseViewerProps {
  clause: Clause | null;
  isOpen: boolean;
  onClose: () => void;
  policyName?: string;
}

export const ClauseViewer: React.FC<ClauseViewerProps> = ({
  clause,
  isOpen,
  onClose,
  policyName = 'Policy Wordings',
}) => {
  if (!clause) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={`POLICY EVIDENCE — SECTION ${clause.section}`}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '2px solid var(--ink)', paddingBottom: '12px' }}>
          <div>
            <div style={{ fontWeight: 800, fontSize: '1.125rem' }}>{clause.heading}</div>
            <div style={{ fontSize: '0.8125rem', opacity: 0.75 }}>{policyName}</div>
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <Badge color="teal">Page {clause.page}</Badge>
            <Badge color="neutral">§{clause.section}</Badge>
          </div>
        </div>

        {/* Verbatim Clause Text in Newsreader Italic */}
        <div
          style={{
            background: 'var(--sheet-muted)',
            border: '2px solid var(--ink)',
            padding: '18px 20px',
            position: 'relative',
          }}
        >
          <div
            style={{
              position: 'absolute',
              top: '-10px',
              left: '14px',
              background: 'var(--teal)',
              color: '#111111',
              border: '1.5px solid var(--ink)',
              padding: '1px 6px',
              fontSize: '0.6875rem',
              fontWeight: 800,
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
            }}
          >
            <BookOpen size={12} />
            VERBATIM POLICY TEXT
          </div>
          <p className="clause-quote" style={{ fontSize: '1.0625rem', color: 'var(--ink)' }}>
            "{clause.text}"
          </p>
        </div>

        <div style={{ fontSize: '0.8125rem', opacity: 0.7, lineHeight: 1.4 }}>
          This clause was extracted directly from the filed policy terms and conditions document submitted to the Insurance Regulatory and Development Authority of India (IRDAI).
        </div>
      </div>
    </Modal>
  );
};
