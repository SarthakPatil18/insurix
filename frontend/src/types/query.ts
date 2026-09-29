import { CalculationResult } from './estimate';

export interface EvidenceCitation {
  text: string;
  page: number;
  section: string;
  score?: number;
  policy_id: string;
}

export type VerdictType = 'covered' | 'excluded' | 'conditional' | 'uncertain';

export interface UncertaintyDetails {
  confidence: 'high' | 'medium' | 'low';
  missing_info: string[];
  recommendation: string;
}

export interface QueryResponse {
  answer: string;
  verdict: VerdictType;
  verdict_label: string;
  confidence: 'high' | 'medium' | 'low';
  evidence: EvidenceCitation[];
  cost_estimate?: CalculationResult;
  uncertainty?: UncertaintyDetails;
  disclaimer: string;
  trace?: string[];
  llm?: string;
}
