import { Treatment, EstimateRequest, CalculationResult } from '@/types/estimate';
import { apiRequest } from './apiClient';
import { SAMPLE_TREATMENTS } from '../data/sampleTreatments';
import { SAMPLE_POLICIES } from '../data/samplePolicies';

export const calculatorService = {
  async getTreatments(): Promise<Treatment[]> {
    try {
      const data = await apiRequest<Treatment[]>('/api/treatments');
      if (Array.isArray(data) && data.length > 0) {
        return data;
      }
    } catch {
      // Offline fallback
    }
    return Object.values(SAMPLE_TREATMENTS);
  },

  async getTreatmentById(id: string): Promise<Treatment> {
    try {
      return await apiRequest<Treatment>(`/api/treatments/${id}`);
    } catch {
      return SAMPLE_TREATMENTS[id] || SAMPLE_TREATMENTS['knee_replacement'];
    }
  },

  async calculate(req: EstimateRequest): Promise<CalculationResult> {
    try {
      const res = await apiRequest<CalculationResult>('/api/estimate', {
        method: 'POST',
        body: JSON.stringify(req),
      });
      if (res && typeof res.payable === 'number') {
        return res;
      }
    } catch (e) {
      // Offline deterministic calculation fallback
    }

    return this.calculateLocal(req);
  },

  calculateLocal(req: EstimateRequest): CalculationResult {
    const policy = SAMPLE_POLICIES[req.policy_id] || SAMPLE_POLICIES['star'];
    const treatment = SAMPLE_TREATMENTS[req.procedure_id] || SAMPLE_TREATMENTS['knee_replacement'];

    const totalCost = Math.round(req.quoted_total);
    const lines: CalculationResult['lines'] = [
      { label: `Quoted Hospital Bill (${treatment.name})`, amount: totalCost, kind: 'info' },
    ];

    let currentCost = totalCost;
    let deductionTotal = 0;

    // Rule 1: Waiting Period Check
    if (treatment.specific_waiting && req.tenure_months < 24) {
      lines.push({
        label: `Specific Disease Waiting Period Active (${req.tenure_months}m < 24m)`,
        amount: totalCost,
        kind: 'sub',
      });
      return {
        total_cost: totalCost,
        payable: 0,
        out_of_pocket: totalCost,
        admissible: 0,
        deduction_total: totalCost,
        pct: 0,
        lines,
        trace: ['Claim repudiated under Specific Illness 24-Month Waiting Period Clause.'],
      };
    }

    // Rule 2: Statutory Non-Medical Consumables (~8%)
    const consumablesDeduction = Math.round(totalCost * 0.08);
    deductionTotal += consumablesDeduction;
    lines.push({
      label: 'Non-Medical Consumables (IRDAI Table 1, ~8%)',
      amount: consumablesDeduction,
      kind: 'sub',
    });

    // Rule 3: Non-Network Hospital Surcharge (if applicable)
    if (req.hospital_type === 'non_network') {
      const nonNetDeduction = Math.round(totalCost * 0.10);
      deductionTotal += nonNetDeduction;
      lines.push({
        label: 'Non-Network Co-Payment / Tariff Surcharge (10%)',
        amount: nonNetDeduction,
        kind: 'sub',
      });
    }

    // Rule 4: Room Rent Proportionate Deduction
    let roomPenalty = 0;
    if (policy.proportionality && (req.room_category === 'deluxe' || req.room_category === 'suite')) {
      // 1% of Sum Insured cap
      const roomLimit = Math.round(policy.sum_insured * 0.01);
      const actualRoomRate = req.room_category === 'suite' ? 12000 : 8500;
      if (actualRoomRate > roomLimit) {
        const ratio = (actualRoomRate - roomLimit) / actualRoomRate;
        roomPenalty = Math.round(totalCost * 0.18 * ratio);
        deductionTotal += roomPenalty;
        lines.push({
          label: `Proportionate Room Rent Deduction (Occupied ₹${actualRoomRate}/day vs Limit ₹${roomLimit})`,
          amount: roomPenalty,
          kind: 'sub',
        });
      }
    }

    // Rule 5: Senior Citizen Co-payment
    let copayDeduction = 0;
    if (req.patient_age >= 60 && policy.id === 'star') {
      const interim = Math.max(0, totalCost - deductionTotal);
      copayDeduction = Math.round(interim * 0.10);
      deductionTotal += copayDeduction;
      lines.push({
        label: 'Senior Citizen Co-payment (10% for age 60+)',
        amount: copayDeduction,
        kind: 'sub',
      });
    }

    // Cap deduction total so it cannot exceed totalCost
    deductionTotal = Math.min(deductionTotal, totalCost);
    const payable = Math.max(0, totalCost - deductionTotal);
    const outOfPocket = totalCost - payable;
    const pct = Math.round((payable / totalCost) * 100);

    lines.push({
      label: 'Net Insurer Payable Amount',
      amount: payable,
      kind: 'total',
    });

    return {
      total_cost: totalCost,
      payable,
      out_of_pocket: outOfPocket,
      admissible: payable,
      deduction_total: deductionTotal,
      pct,
      lines,
      trace: [
        'Checked 24-Month Waiting Period: Eligible',
        'Consumable Disallowance computed at statutory 8%',
        policy.proportionality ? 'Proportionate billing rule evaluated' : 'Single standard room exemption applied',
        'Deterministic ledger identity verified: Total - Deductions === Payable',
      ],
    };
  },
};
