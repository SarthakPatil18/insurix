export interface CostHeads {
  surgeon: number;
  ot: number;
  anaesthesia: number;
  implant: number;
  medicines: number;
  diagnostics: number;
  room: number;
  icu: number;
  [key: string]: number;
}

export interface Treatment {
  id: string;
  name: string;
  category: string;
  icd: string;
  specific_waiting: boolean;
  excluded: boolean;
  exclusion_code: string | null;
  day_care: boolean;
  cost_range: {
    min: number;
    avg: number;
    max: number;
  };
  average: number;
  room_rate: number;
  icu_rate: number;
  icu_days: number;
  default_days: number;
  heads: CostHeads;
}

export interface EstimateRequest {
  policy_id: string;
  procedure_id: string;
  hospital_type: 'network' | 'non_network';
  room_category: 'general' | 'twin_sharing' | 'single_ac' | 'deluxe' | 'suite';
  patient_age: number;
  tenure_months: number;
  quoted_total: number;
}

export interface DeductionLine {
  label: string;
  amount: number;
  kind: 'info' | 'sub' | 'total' | 'accent';
}

export interface EstimateTotals {
  total_cost: number;
  payable: number;
  out_of_pocket: number;
  admissible: number;
  deduction_total: number;
  pct: number;
}

export interface CalculationResult {
  total_cost: number;
  payable: number;
  out_of_pocket: number;
  admissible: number;
  deduction_total: number;
  pct: number;
  lines: DeductionLine[];
  trace?: string[];
}
