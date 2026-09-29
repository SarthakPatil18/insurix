import React from 'react';
import { Pin } from 'lucide-react';

interface CitationChipProps {
  page: number;
  section: string;
  onClick?: () => void;
  className?: string;
}

export const CitationChip: React.FC<CitationChipProps> = ({
  page,
  section,
  onClick,
  className = '',
}) => {
  const cleanSec = section.startsWith('§') ? section : `§${section}`;

  return (
    <button
      type="button"
      className={`citation-chip ${className}`}
      onClick={onClick}
      aria-label={`View evidence clause from Page ${page}, Section ${cleanSec}`}
      title="Click to view verbatim policy clause"
    >
      <Pin size={12} style={{ transform: 'rotate(45deg)' }} />
      <span>Page {page}, {cleanSec}</span>
    </button>
  );
};
