import React, { useState } from 'react';
import { Layers, Bookmark, FileText } from 'lucide-react';

interface PolicyStack3DProps {
  policyName: string;
  pageCount?: number;
  onPageClick?: (page: number) => void;
}

export const PolicyStack3D: React.FC<PolicyStack3DProps> = ({
  policyName,
  pageCount = 60,
  onPageClick,
}) => {
  const [fanned, setFanned] = useState<boolean>(false);

  // Key policy landmark pages
  const bookmarks = [
    { page: 10, label: 'Waiting Periods (§2.1)', color: 'var(--yellow)' },
    { page: 18, label: 'Surgical Benefits (§4.2)', color: 'var(--lime)' },
    { page: 22, label: 'Sub-Limits (§6.3)', color: 'var(--lilac)' },
    { page: 26, label: 'Consumables (§8.2)', color: 'var(--red)' },
  ];

  return (
    <div
      className="paper-sheet"
      style={{
        padding: '24px',
        borderWidth: 'var(--bw-thick)',
        boxShadow: 'var(--shadow-md)',
        background: 'var(--sheet)',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Layers size={18} />
          <span style={{ fontWeight: 800, fontSize: '0.875rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
            The Physical Policy Stack (60 Pages)
          </span>
        </div>
        <button
          onClick={() => setFanned(!fanned)}
          style={{
            padding: '4px 8px',
            fontSize: '0.75rem',
            fontWeight: 800,
            border: '2px solid var(--ink)',
            background: fanned ? 'var(--lime)' : 'var(--sheet-muted)',
            boxShadow: '2px 2px 0 var(--ink)',
          }}
        >
          {fanned ? 'Stack Pages' : 'Dissect & Fan'}
        </button>
      </div>

      {/* Layered Paper Stack Visual */}
      <div
        style={{
          height: '140px',
          position: 'relative',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          perspective: '1000px',
        }}
      >
        {/* Shadow under stack */}
        <div
          style={{
            position: 'absolute',
            bottom: '10px',
            width: '85%',
            height: '20px',
            background: 'rgba(17, 17, 17, 0.25)',
            filter: 'blur(4px)',
            transform: 'rotateX(60deg)',
          }}
        />

        {/* Paper Layers */}
        {[0, 1, 2, 3, 4].map((idx) => {
          const isTop = idx === 4;
          const rotation = fanned ? (idx - 2) * 5 : (idx - 2) * 1.5;
          const translateY = fanned ? -idx * 8 : -idx * 3;
          const translateX = fanned ? (idx - 2) * 20 : (idx - 2) * 2;

          return (
            <div
              key={idx}
              style={{
                position: 'absolute',
                width: '78%',
                height: '90px',
                background: isTop ? 'var(--sheet)' : 'var(--sheet-muted)',
                border: '2.5px solid var(--ink)',
                boxShadow: isTop ? 'var(--shadow-sm)' : '1px 1px 0 var(--ink)',
                transform: `translate(${translateX}px, ${translateY}px) rotate(${rotation}deg)`,
                transition: 'all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '12px 16px',
                zIndex: idx,
              }}
            >
              {isTop && (
                <>
                  <div>
                    <div style={{ fontSize: '0.8125rem', fontWeight: 900 }}>{policyName}</div>
                    <div style={{ fontSize: '0.6875rem', opacity: 0.7 }}>IRDAI Standard Wording • 60 Pages</div>
                  </div>
                  <FileText size={24} opacity={0.4} />
                </>
              )}
            </div>
          );
        })}
      </div>

      {/* Bookmarked Key Clauses Strip */}
      <div style={{ marginTop: '16px', display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
        {bookmarks.map((b) => (
          <div
            key={b.page}
            onClick={() => onPageClick && onPageClick(b.page)}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '4px 10px',
              background: b.color,
              color: '#111111',
              border: '2px solid var(--ink)',
              fontSize: '0.75rem',
              fontWeight: 800,
              boxShadow: '2px 2px 0 var(--ink)',
              cursor: onPageClick ? 'pointer' : 'default',
            }}
          >
            <Bookmark size={12} />
            <span>P.{b.page}: {b.label}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
