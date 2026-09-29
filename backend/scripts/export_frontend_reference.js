#!/usr/bin/env node
/**
 * Insurix Frontend Reference Exporter
 * Extracts sample policies, treatments catalogue, and produces >=2,000 parity test vectors.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const indexPath = path.resolve(rootDir, '../index.html');

console.log('Reading frontend index.html from:', indexPath);
const indexHtml = fs.readFileSync(indexPath, 'utf-8');

// 1. Extract SAMPLE_POLICIES
const samplePoliciesMatch = indexHtml.match(/const\s+SAMPLE_POLICIES\s*=\s*(\{[\s\S]*?\n\s*\});/);
if (!samplePoliciesMatch) {
  console.error('Could not locate SAMPLE_POLICIES in index.html');
  process.exit(1);
}

// Safely evaluate SAMPLE_POLICIES in isolated scope
const samplePolicies = new Function(`return ${samplePoliciesMatch[1]}`)();

// Enhance policies with full clauses and schedule data
const enrichedPolicies = {
  star: {
    ...samplePolicies.star,
    proportionality: true,
    deductible: 0,
    non_network_copay_pct: 0,
    implant_caps: {
      intraocular_lens: 15000,
      knee_joint_prosthesis: 90000
    },
    clauses: [
      {
        page: 18,
        section: "4.2",
        heading: "Medically Necessary Surgical Expenses",
        text: "Knee replacement surgery is covered as a medically necessary procedure under Section 4.2 of the policy wording subject to standard specific illness waiting periods."
      },
      {
        page: 12,
        section: "5.1",
        heading: "Pre-Existing Diseases Waiting Period",
        text: "Waiting period of 36 months applies for pre-existing conditions and their direct complications. Pre-existing disease coverage commences only after 36 months of continuous active policy renewal."
      },
      {
        page: 22,
        section: "6.3",
        heading: "Cataract Treatment Sub-limit",
        text: "Coverage for cataract surgery is limited to a maximum of ₹25,000 per eye inclusive of cost of intraocular lens."
      },
      {
        page: 11,
        section: "2.4",
        heading: "Specific Illness Waiting Period",
        text: "Specific illness waiting period of 24 consecutive months of continuous coverage applies for cataract, hernia, joint replacement surgeries, and hydrocele."
      },
      {
        page: 14,
        section: "3.8",
        heading: "Room Rent and Proportionate Deductions",
        text: "If the insured person occupies a room with room rent higher than the entitled limit (1% of Sum Insured per day), the insurer shall bear all associated medical expenses proportionately."
      },
      {
        page: 15,
        section: "3.9",
        heading: "Intensive Care Unit (ICU) Charges",
        text: "ICU charges covered up to 2% of Sum Insured per day without proportionate deduction on doctor fees."
      },
      {
        page: 10,
        section: "5.0",
        heading: "Initial 30-Day Waiting Period",
        text: "A 30-day waiting period from inception applies for all medical treatments other than accidental injury."
      },
      {
        page: 26,
        section: "8.2",
        heading: "Exclusions: Consumables & Non-Medical",
        text: "Non-medical consumables, convenience charges, and luxury amenities are excluded under IRDAI guidelines (approx. 8% statutory deduction)."
      }
    ]
  },
  royal: {
    ...samplePolicies.royal,
    proportionality: false,
    deductible: 0,
    non_network_copay_pct: 0,
    implant_caps: {
      intraocular_lens: 25000,
      knee_joint_prosthesis: 120000
    },
    clauses: [
      {
        page: 16,
        section: "3.1",
        heading: "Single Standard A/C Room Cover",
        text: "The insured is eligible for a Single Standard A/C Room without proportionate deduction penalties across associated medical practitioner fees."
      },
      {
        page: 19,
        section: "4.5",
        heading: "Cataract Benefit",
        text: "Cataract surgery is covered up to ₹50,000 per eye after continuous coverage of 24 months."
      },
      {
        page: 10,
        section: "2.1",
        heading: "Waiting Periods Schedule",
        text: "Pre-existing conditions covered after 24 months. Specific diseases covered after 24 months. Initial waiting period of 30 days applies."
      },
      {
        page: 25,
        section: "7.1",
        heading: "Non-Medical Items Exclusion",
        text: "Expenses incurred on non-medical items and toiletries shall not be admissible as per IRDAI list."
      }
    ]
  },
  hdfc: {
    ...samplePolicies.hdfc,
    proportionality: false,
    deductible: 0,
    non_network_copay_pct: 0,
    implant_caps: {
      intraocular_lens: 35000,
      knee_joint_prosthesis: 150000
    },
    clauses: [
      {
        page: 14,
        section: "2.2",
        heading: "Any Room Except Suite Eligibility",
        text: "The insured person is entitled to occupy Any Room category except a Suite room with zero proportionate billing deduction."
      },
      {
        page: 20,
        section: "5.3",
        heading: "Restore Benefit & No Sub-limits",
        text: "No sub-limits apply for cataract or joint replacement surgery; expenses are payable up to the Sum Insured."
      },
      {
        page: 12,
        section: "3.2",
        heading: "Waiting Periods",
        text: "Initial waiting period 30 days. Pre-existing disease waiting period is 36 consecutive months."
      }
    ]
  }
};

// 2. Define Comprehensive Treatment Catalogue
const treatments = {
  knee_replacement: {
    id: "knee_replacement",
    name: "Total Knee Replacement (Unilateral)",
    category: "Orthopedic Surgery",
    icd: "Z96.651",
    specific_waiting: true,
    excluded: false,
    exclusion_code: null,
    day_care: false,
    cost_range: { min: 220000, avg: 280000, max: 350000 },
    average: 280000,
    room_rate: 6500,
    icu_rate: 14000,
    icu_days: 1,
    default_days: 4,
    heads: {
      surgeon: 75000,
      ot: 35000,
      anaesthesia: 20000,
      implant: 85000,
      medicines: 30000,
      diagnostics: 15000,
      room: 20000,
      icu: 0
    }
  },
  cataract: {
    id: "cataract",
    name: "Cataract Surgery with IOL (Per Eye)",
    category: "Ophthalmology Daycare",
    icd: "H25.9",
    specific_waiting: true,
    excluded: false,
    exclusion_code: null,
    day_care: true,
    cost_range: { min: 30000, avg: 45000, max: 65000 },
    average: 45000,
    room_rate: 4000,
    icu_rate: 0,
    icu_days: 0,
    default_days: 1,
    heads: {
      surgeon: 16000,
      ot: 9000,
      anaesthesia: 4000,
      implant: 11000,
      medicines: 3000,
      diagnostics: 2000,
      room: 0,
      icu: 0
    }
  },
  appendectomy: {
    id: "appendectomy",
    name: "Laparoscopic Appendectomy",
    category: "General Surgery",
    icd: "K35.80",
    specific_waiting: false,
    excluded: false,
    exclusion_code: null,
    day_care: false,
    cost_range: { min: 45000, avg: 65000, max: 95000 },
    average: 65000,
    room_rate: 5000,
    icu_rate: 10000,
    icu_days: 0,
    default_days: 2,
    heads: {
      surgeon: 25000,
      ot: 15000,
      anaesthesia: 7000,
      implant: 0,
      medicines: 8000,
      diagnostics: 5000,
      room: 5000,
      icu: 0
    }
  },
  cabg: {
    id: "cabg",
    name: "Coronary Artery Bypass Graft (CABG)",
    category: "Cardiothoracic Surgery",
    icd: "I25.10",
    specific_waiting: true,
    excluded: false,
    exclusion_code: null,
    day_care: false,
    cost_range: { min: 300000, avg: 380000, max: 550000 },
    average: 380000,
    room_rate: 7500,
    icu_rate: 18000,
    icu_days: 3,
    default_days: 7,
    heads: {
      surgeon: 110000,
      ot: 60000,
      anaesthesia: 35000,
      implant: 45000,
      medicines: 45000,
      diagnostics: 30000,
      room: 25000,
      icu: 30000
    }
  },
  dialysis: {
    id: "dialysis",
    name: "Hemodialysis (Single Session)",
    category: "Nephrology Daycare",
    icd: "Z99.2",
    specific_waiting: false,
    excluded: false,
    exclusion_code: null,
    day_care: true,
    cost_range: { min: 2500, avg: 3500, max: 5000 },
    average: 3500,
    room_rate: 1500,
    icu_rate: 0,
    icu_days: 0,
    default_days: 1,
    heads: {
      surgeon: 800,
      ot: 0,
      anaesthesia: 0,
      implant: 700,
      medicines: 1200,
      diagnostics: 800,
      room: 0,
      icu: 0
    }
  }
};

// 3. Write data/sample_policies.json and data/treatments.json
const dataDir = path.resolve(rootDir, 'data');
fs.mkdirSync(dataDir, { recursive: true });
fs.writeFileSync(path.join(dataDir, 'sample_policies.json'), JSON.stringify(enrichedPolicies, null, 2));
fs.writeFileSync(path.join(dataDir, 'treatments.json'), JSON.stringify(treatments, null, 2));
console.log('✓ Wrote data/sample_policies.json and data/treatments.json');

// 4. Parity Vector Generator
// Replicates frontend index.html calculation logic exactly
function evaluateFrontendScenario(policy, scenario) {
  const {
    treatmentId,
    cost,
    hospital = 'network',
    room = 'within_limit',
    age = 45,
    waitingStatus = 'completed',
    tenureMonths = 36,
    ped = false
  } = scenario;

  const totalBill = Math.round(cost);
  let roomPenalty = 0;
  let copayPercent = 0;
  const nonMedical = Math.round(totalBill * 0.08); // 8% consumables
  const customaryDeduction = hospital === 'non_network' ? Math.round(totalBill * 0.12) : 0;

  // Waiting period evaluation
  const isPreExistingOrSpecific = (treatmentId === 'knee_replacement' || treatmentId === 'cataract' || treatmentId === 'cabg');
  if (waitingStatus === 'partial' || (ped && tenureMonths < (policy.id === 'star' ? 36 : 24)) || (isPreExistingOrSpecific && tenureMonths < 24)) {
    return {
      verdict: "no",
      verdict_label: "CLAIM DISALLOWED",
      confidence: "high",
      lines: [
        { label: "Claim Disallowed", amount: totalBill, kind: "total" }
      ],
      totals: {
        total_cost: totalBill,
        payable: 0,
        out_of_pocket: totalBill,
        deduction_total: totalBill,
        pct: 0
      }
    };
  }

  // Room penalty
  if (room === 'suite') {
    roomPenalty = Math.round(totalBill * 0.38);
  } else if (room === 'exceeds_deluxe') {
    if (policy.id === 'star') {
      roomPenalty = Math.round(totalBill * 0.22);
    } else if (policy.id === 'royal') {
      roomPenalty = Math.round(totalBill * 0.15);
    } else {
      roomPenalty = 0; // HDFC any room except suite
    }
  }

  // Copay
  if (policy.id === 'star' && age >= 60) {
    copayPercent = 0.10;
  }

  // Sub-limits
  let subLimitCap = 0;
  if (treatmentId === 'cataract') {
    if (policy.id === 'star') subLimitCap = 25000;
    else if (policy.id === 'royal') subLimitCap = 50000;
  }

  let allowableBase = totalBill - roomPenalty - nonMedical - customaryDeduction;
  let subLimitDeduction = 0;
  if (subLimitCap > 0 && allowableBase > subLimitCap) {
    subLimitDeduction = allowableBase - subLimitCap;
    allowableBase = subLimitCap;
  }
  if (allowableBase < 0) allowableBase = 0;

  const copayAmount = Math.round(allowableBase * copayPercent);
  let insurerPays = allowableBase - copayAmount;
  if (insurerPays > policy.sum_insured) {
    insurerPays = policy.sum_insured;
  }

  const youPay = totalBill - insurerPays;
  const deductionTotal = totalBill - insurerPays;
  const pct = totalBill > 0 ? Math.round((insurerPays / totalBill) * 100) : 0;

  const lines = [
    { label: "Gross Hospital Estimate", amount: totalBill, kind: "info" }
  ];
  if (roomPenalty > 0) {
    lines.push({ label: "Room Rent Proportionate Penalty", amount: roomPenalty, kind: "sub" });
  }
  if (customaryDeduction > 0) {
    lines.push({ label: "Non-Network Tariff Disallowance", amount: customaryDeduction, kind: "sub" });
  }
  if (nonMedical > 0) {
    lines.push({ label: "Non-Medical Consumables (8%)", amount: nonMedical, kind: "sub" });
  }
  if (subLimitDeduction > 0) {
    lines.push({ label: "Sub-Limit Capping Disallowance", amount: subLimitDeduction, kind: "sub" });
  }
  if (copayAmount > 0) {
    lines.push({ label: `Co-payment (${copayPercent * 100}%)`, amount: copayAmount, kind: "sub" });
  }
  lines.push({ label: "Net Insurer Payable", amount: insurerPays, kind: "total" });

  const verdict = insurerPays === totalBill ? "covered" : (insurerPays > 0 ? "conditional" : "no");
  const verdict_label = insurerPays === totalBill ? "FULLY COVERED" : (insurerPays > 0 ? "COVERED — WITH DEDUCTIONS" : "DISALLOWED");

  return {
    verdict,
    verdict_label,
    confidence: "high",
    lines,
    totals: {
      total_cost: totalBill,
      payable: insurerPays,
      out_of_pocket: youPay,
      deduction_total: deductionTotal,
      pct
    }
  };
}

// Generate >2,000 combinatorial scenarios
const parityVectors = [];
const policyKeys = ['star', 'royal', 'hdfc'];
const treatmentKeys = Object.keys(treatments);
const hospitalTypes = ['network', 'non_network'];
const roomTypes = ['within_limit', 'exceeds_deluxe', 'suite'];
const ages = [35, 62];
const tenures = [0, 8, 25, 41];
const waitingStatuses = ['completed', 'partial'];

for (const pKey of policyKeys) {
  const policy = enrichedPolicies[pKey];
  for (const tKey of treatmentKeys) {
    const t = treatments[tKey];
    const costMultipliers = [0.4, 0.8, 1.0, 1.25];
    for (const mult of costMultipliers) {
      const cost = Math.round(t.average * mult);
      for (const hosp of hospitalTypes) {
        for (const room of roomTypes) {
          for (const age of ages) {
            for (const tenure of tenures) {
              for (const wait of waitingStatuses) {
                const scenario = {
                  policyId: pKey,
                  treatmentId: tKey,
                  cost,
                  hospital: hosp,
                  room,
                  age,
                  tenureMonths: tenure,
                  waitingStatus: wait,
                  ped: tenure < 36
                };
                const expected = evaluateFrontendScenario(policy, scenario);
                parityVectors.push({ scenario, expected });
              }
            }
          }
        }
      }
    }
  }
}

console.log(`Generated ${parityVectors.length} parity verification vectors.`);
const testsDir = path.resolve(rootDir, 'tests');
fs.mkdirSync(testsDir, { recursive: true });
fs.writeFileSync(path.join(testsDir, 'parity_vectors.json'), JSON.stringify(parityVectors, null, 2));
console.log('✓ Wrote tests/parity_vectors.json');
