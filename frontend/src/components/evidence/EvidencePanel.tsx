import React from 'react';
import { EvidenceCitation } from '@/types/query';
import { CitationChip } from './CitationChip';
import { BookOpen } from 'lucide-react';

interface EvidencePanelProps {
  evidence: EvidenceCitation[];
  onSelectCitation?: (item: EvidenceCitation) => void;
}

export const EvidencePanel: React.FC<EvidencePanelProps> = ({
  evidence,
  onSelectCitation,
}) => {
  if (!evidence || evidence.length === 0) {
    return (
      <div
        style={{
          padding: '12px 16px',
          background: 'var(--sheet-muted)',
          border: '2px dashed var(--ink)',
          fontSize: '0.8125rem',
          opacity: 0.8,
        }}
      >
        No direct policy clauses pinned yet. Ask a specific procedure question to retrieve exact citations.
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
        <BookOpen size={16} />
        <span style={{ fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.04em' }}>
          VERIFIED POLICY EVIDENCE ({evidence.length})
        </span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {evidence.map((item, idx) => (
          <div
            key={idx}
            style={{
              padding: '12px 14px',
              background: 'var(--sheet-muted)',
              border: '2px solid var(--ink)',
              position: 'relative',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
              <CitationChip
                page={item.page}
                section={item.section}
                onClick={() => onSelectCitation && onSelectCitation(item)}
              />
              {item.score && (
                <span style={{ fontSize: '0.6875rem', fontWeight: 700, opacity: 0.7 }}>
                  Match Score: {item.score.toFixed(1)}
                </span>
              )}
            </div>
            <p className="clause-quote" style={{ fontSize: '0.9375rem', lineHeight: 1.5, margin: 0 }}>
              "{item.text}"
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};
