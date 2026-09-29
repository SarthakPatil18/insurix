/**
 * Text and UI formatting utilities
 */

export function truncateText(text: string, maxLen: number = 100): string {
  if (text.length <= maxLen) return text;
  return text.slice(0, maxLen).trim() + '...';
}

export function formatCitationRef(page: number, section: string): string {
  const cleanSec = section.startsWith('§') ? section : `§${section}`;
  return `Page ${page}, ${cleanSec}`;
}

export function getVerdictLabel(verdict: string): string {
  switch (verdict.toLowerCase()) {
    case 'covered':
      return 'COVERED IN FULL';
    case 'excluded':
      return 'EXCLUDED FROM COVER';
    case 'conditional':
      return 'COVERED — WITH DEDUCTIONS';
    case 'uncertain':
    default:
      return 'UNCERTAIN — NEEDS TPA REVIEW';
  }
}
