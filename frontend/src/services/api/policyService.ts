import { Policy } from '@/types/policy';
import { apiRequest } from './apiClient';
import { SAMPLE_POLICIES } from '../data/samplePolicies';

export const policyService = {
  async getAllPolicies(): Promise<Policy[]> {
    return Object.values(SAMPLE_POLICIES);
  },

  async getPolicyById(id: string): Promise<Policy> {
    try {
      const summary = await apiRequest<any>(`/api/policy/${id}/summary`);
      if (summary && summary.id) {
        // Merge with local clauses if summary is lightweight
        const base = SAMPLE_POLICIES[id] || SAMPLE_POLICIES['star'];
        return {
          ...base,
          ...summary,
        };
      }
    } catch {
      // Offline fallback
    }
    return SAMPLE_POLICIES[id] || SAMPLE_POLICIES['star'];
  },

  async getCoverage(id: string): Promise<any[]> {
    try {
      return await apiRequest<any[]>(`/api/policy/${id}/coverage`);
    } catch {
      const pol = SAMPLE_POLICIES[id] || SAMPLE_POLICIES['star'];
      return pol.clauses;
    }
  },

  async getExclusions(id: string): Promise<any[]> {
    try {
      return await apiRequest<any[]>(`/api/policy/${id}/exclusions`);
    } catch {
      return [
        { category: 'Cosmetic & Aesthetic', description: 'Cosmetic, aesthetic or plastic surgery unless necessitated by accidental trauma.' },
        { category: 'Substance Abuse', description: 'Treatment directly or indirectly resulting from alcoholism or drug abuse.' },
        { category: 'Non-Prescription Consumables', description: 'Non-medical consumables, toiletries and convenience charges (IRDAI Table 1).' },
      ];
    }
  },
};
