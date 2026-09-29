export interface Clause {
  page: number;
  section: string;
  heading: string;
  text: string;
}

export interface WaitingPeriods {
  initial: string;
  pre_existing: string;
  specific_diseases: string;
}

export interface SubLimits {
  cataract: string;
  knee_replacement: string;
  dialysis: string;
  [key: string]: string;
}

export interface ImplantCaps {
  intraocular_lens: number;
  knee_joint_prosthesis: number;
  [key: string]: number;
}

export interface Policy {
  id: string;
  insurer: string;
  policy_name: string;
  sum_insured: number;
  policy_period: string;
  waiting_periods: WaitingPeriods;
  room_rent_limit: string;
  icu_limit: string;
  co_payment: string;
  sub_limits: SubLimits;
  tag: string;
  short_desc: string;
  proportionality: boolean;
  deductible: number;
  non_network_copay_pct: number;
  implant_caps: ImplantCaps;
  clauses: Clause[];
}
