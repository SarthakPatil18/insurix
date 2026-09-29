/**
 * Money Arithmetic and Formatting Utilities
 * Adheres to Indian Rupee standards and deterministic rounding.
 */

export function formatINR(val: number): string {
  const num = Math.round(val);
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(num);
}

export function formatLakhs(val: number): string {
  if (val >= 10000000) {
    return `₹${(val / 10000000).toFixed(1)} Cr`;
  }
  if (val >= 100000) {
    const lakhs = val / 100000;
    return `₹${Number.isInteger(lakhs) ? lakhs : lakhs.toFixed(1)}L`;
  }
  return formatINR(val);
}

export function parseINR(str: string): number {
  const cleaned = str.replace(/[^0-9.-]+/g, '');
  const val = parseFloat(cleaned);
  return isNaN(val) ? 0 : Math.round(val);
}

/**
 * Enforces fundamental ledger invariant:
 * Total Quoted Cost - Sum(Deductions) === Insurer Payable
 */
export function verifyLedgerInvariant(
  totalCost: number,
  deductionTotal: number,
  payable: number
): boolean {
  return totalCost - deductionTotal === payable;
}
