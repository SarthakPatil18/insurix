/**
 * Security & File Validation Utilities
 * Zero unsafe innerHTML, strict PDF inspection, and PII protection.
 */

export const POLICY_KEYWORDS = [
  'policy', 'insured', 'insurer', 'insurance', 'premium', 'deductible',
  'coverage', 'claim', 'benefit', 'exclusion', 'copay', 'co-pay',
  'coinsurance', 'co-insurance', 'waiting period', 'preauthorization',
  'hospitalization', 'sum insured', 'policyholder', 'reimbursement',
  'endorsement', 'in-patient', 'out-patient', 'out-of-pocket',
  'health plan', 'underwriter', 'sub-limit', 'rider', 'maternity',
  'cashless', 'network provider', 'day care', 'domiciliary'
];

export const MIN_KEYWORD_HITS = 3;
export const MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024; // 10 MB

export interface FileValidationResult {
  valid: boolean;
  reason?: string;
  keywordHits?: number;
}

export function sanitizeInput(input: string): string {
  return input
    .replace(/[<>]/g, '')
    .trim();
}

export function sanitizeFilename(filename: string): string {
  return filename
    .replace(/[^a-zA-Z0-9._-]/g, '_')
    .slice(0, 100);
}

export async function validatePolicyFile(file: File): Promise<FileValidationResult> {
  // 1. File size check
  if (file.size > MAX_FILE_SIZE_BYTES) {
    return {
      valid: false,
      reason: `File size exceeds the 10 MB limit (${(file.size / (1024 * 1024)).toFixed(1)} MB). Please upload a smaller PDF.`,
    };
  }

  // 2. Extension check
  const ext = file.name.split('.').pop()?.toLowerCase();
  if (ext !== 'pdf' && file.type !== 'application/pdf') {
    return {
      valid: false,
      reason: `Only PDF files are accepted. You provided a .${ext?.toUpperCase() || 'unknown'} file.`,
    };
  }

  // 3. Read bytes & check %PDF- magic header + insurance keywords
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const raw = e.target?.result as string;
      if (!raw || !raw.startsWith('%PDF-')) {
        resolve({
          valid: false,
          reason: 'The file does not appear to be a valid PDF (missing %PDF- header).',
        });
        return;
      }

      const lower = raw.toLowerCase();
      const hits = POLICY_KEYWORDS.filter((kw) => lower.includes(kw));

      if (hits.length >= MIN_KEYWORD_HITS) {
        resolve({
          valid: true,
          keywordHits: hits.length,
        });
      } else {
        resolve({
          valid: false,
          reason: `Could not verify document as health insurance policy (${hits.length} of ${MIN_KEYWORD_HITS} required policy terms detected).`,
          keywordHits: hits.length,
        });
      }
    };

    reader.onerror = () => {
      resolve({
        valid: false,
        reason: 'Could not read the file. It may be corrupted or protected.',
      });
    };

    reader.readAsBinaryString(file);
  });
}
