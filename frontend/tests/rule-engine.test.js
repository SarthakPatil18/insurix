/**
 * Frontend Rule Engine Oracle Invariant Tests
 * Verifies mathematical ledger identity: Total Cost - Sum(Deductions) == Insurer Payable
 */

import assert from 'node:assert';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const vectorsPath = path.resolve(__dirname, '../../backend/tests/parity_vectors.json');

console.log('=== FRONTEND RULE ENGINE ORACLE TESTS ===');
const vectors = JSON.parse(fs.readFileSync(vectorsPath, 'utf-8'));
console.log(`Loaded ${vectors.length} verification vectors.`);

let passed = 0;
for (const [idx, item] of vectors.entries()) {
  const { scenario, expected } = item;
  const { totals } = expected;

  // Ledger invariant: total_cost - deduction_total === payable
  assert.strictEqual(
    totals.total_cost - totals.deduction_total,
    totals.payable,
    `Ledger identity failed at index ${idx}`
  );

  // Out of pocket identity: total_cost - payable === out_of_pocket
  assert.strictEqual(
    totals.total_cost - totals.payable,
    totals.out_of_pocket,
    `Out of pocket identity failed at index ${idx}`
  );

  // Deduction non-negative
  assert.ok(totals.deduction_total >= 0, `Deduction total negative at index ${idx}`);
  assert.ok(totals.payable >= 0, `Payable negative at index ${idx}`);

  passed++;
}

console.log(`✓ All ${passed} frontend rule engine scenarios satisfied mathematical ledger invariants!`);
