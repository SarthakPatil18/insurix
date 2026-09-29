import { useState, useEffect } from 'react';
import { Policy } from '@/types/policy';
import { policyService } from '@/services/api/policyService';
import { SAMPLE_POLICIES } from '@/services/data/samplePolicies';

export function usePolicy(defaultId: string = 'star') {
  const [activePolicyId, setActivePolicyId] = useState<string>(defaultId);
  const [policies, setPolicies] = useState<Policy[]>(Object.values(SAMPLE_POLICIES));
  const [activePolicy, setActivePolicy] = useState<Policy>(SAMPLE_POLICIES[defaultId]);
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    let mounted = true;
    setLoading(true);
    policyService.getPolicyById(activePolicyId).then((policy) => {
      if (mounted) {
        setActivePolicy(policy);
        setLoading(false);
      }
    });
    return () => {
      mounted = false;
    };
  }, [activePolicyId]);

  const selectPolicy = (id: string) => {
    if (SAMPLE_POLICIES[id]) {
      setActivePolicyId(id);
    }
  };

  return {
    activePolicyId,
    activePolicy,
    policies,
    selectPolicy,
    loading,
  };
}
