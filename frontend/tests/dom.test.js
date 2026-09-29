/**
 * Frontend DOM Verification Tests (64 assertions)
 * Ensures all required IDs, interactive elements, views, and Neo-Brutalist controls exist.
 */

import assert from 'node:assert';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const indexPath = path.resolve(__dirname, '../../index.html');

console.log('=== FRONTEND DOM & INTERACTION VERIFICATION ===');
const html = fs.readFileSync(indexPath, 'utf-8');

const requiredIds = [
  'theme-btn', 'mobile-drawer', 'hero-upload-zone', 'hero-file-input',
  'hero-active-strip', 'landing-chat-input', 'landing-chat-container',
  'demo-chat-input', 'demo-chat-container', 'calc-treatment-select',
  'calc-bill-amount', 'calc-hospital-type', 'calc-room-type',
  'calc-patient-age', 'calc-waiting-status', 'res-total-bill',
  'res-insurer-pays', 'res-you-pay', 'sample-btn-star', 'sample-btn-royal',
  'sample-btn-hdfc', 'view-home', 'view-demo', 'view-how-it-works',
  'view-features', 'view-pricing', 'view-faq', 'view-contact', 'clause-modal',
  'landing-loaded-policy-badge', 'spec-insurer',
  'spec-sum', 'spec-wait-init', 'spec-wait-ped', 'spec-wait-spec',
  'spec-room', 'spec-icu', 'spec-copay', 'spec-cataract', 'spec-knee'
];

let checks = 0;
for (const id of requiredIds) {
  assert.ok(html.includes(`id="${id}"`), `Missing required element ID: ${id}`);
  checks++;
}

// Check key interactive functions
const requiredFunctions = [
  'setupThemeToggle', 'navigateTo', 'loadSamplePolicy', 'runTreatmentCalculation',
  'sendChatQuery', 'openClauseModal', 'validateAndUpload', 'showToast',
  'switchDemoTab', 'toggleAccordion', 'setBilling', 'confirmPlanSubscription'
];

for (const fn of requiredFunctions) {
  assert.ok(html.includes(`function ${fn}`), `Missing function: ${fn}`);
  checks++;
}

// Check views
const views = ['home', 'how-it-works', 'features', 'demo', 'pricing', 'faq', 'contact'];
for (const v of views) {
  assert.ok(html.includes(`view-${v}`), `Missing view: ${v}`);
  checks++;
}

// Check Neo-Brutalist CSS classes
const neoClasses = [
  'hero-card', 'cta-button', 'ghost-button', 'upload-zone', 'confidence-badge',
  'source-badge', 'cost-table', 'pricing-card', 'feature-card', 'step-card'
];

for (const cls of neoClasses) {
  assert.ok(html.includes(`.${cls}`), `Missing Neo-Brutalist class: .${cls}`);
  checks++;
}

console.log(`✓ Completed ${checks} DOM and UI structure assertions successfully!`);
