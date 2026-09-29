import { useState, useEffect } from 'react';
import { Treatment, CalculationResult, EstimateRequest } from '@/types/estimate';
import { calculatorService } from '@/services/api/calculatorService';
import { SAMPLE_TREATMENTS } from '@/services/data/sampleTreatments';

export function useCalculator(activePolicyId: string) {
  const [treatments, setTreatments] = useState<Treatment[]>(Object.values(SAMPLE_TREATMENTS));
  const [selectedProcedureId, setSelectedProcedureId] = useState<string>('knee_replacement');
  const [hospitalType, setHospitalType] = useState<'network' | 'non_network'>('network');
  const [roomCategory, setRoomCategory] = useState<'general' | 'twin_sharing' | 'single_ac' | 'deluxe' | 'suite'>('single_ac');
  const [patientAge, setPatientAge] = useState<number>(45);
  const [tenureMonths, setTenureMonths] = useState<number>(36);
  const [quotedTotal, setQuotedTotal] = useState<number>(280000);
  const [result, setResult] = useState<CalculationResult | null>(null);
  const [calculating, setCalculating] = useState<boolean>(false);

  useEffect(() => {
    calculatorService.getTreatments().then((data) => {
      if (data && data.length > 0) {
        setTreatments(data);
      }
    });
  }, []);

  // Update quoted total when procedure changes
  const handleProcedureChange = (procId: string) => {
    setSelectedProcedureId(procId);
    const proc = treatments.find((t) => t.id === procId) || SAMPLE_TREATMENTS[procId];
    if (proc) {
      setQuotedTotal(proc.average);
    }
  };

  const calculate = async () => {
    setCalculating(true);
    const req: EstimateRequest = {
      policy_id: activePolicyId,
      procedure_id: selectedProcedureId,
      hospital_type: hospitalType,
      room_category: roomCategory,
      patient_age: patientAge,
      tenure_months: tenureMonths,
      quoted_total: quotedTotal,
    };

    try {
      const res = await calculatorService.calculate(req);
      setResult(res);
    } catch {
      const fallback = calculatorService.calculateLocal(req);
      setResult(fallback);
    } finally {
      setCalculating(false);
    }
  };

  // Initial calculation on mount
  useEffect(() => {
    calculate();
  }, [activePolicyId, selectedProcedureId, hospitalType, roomCategory, patientAge, tenureMonths, quotedTotal]);

  return {
    treatments,
    selectedProcedureId,
    hospitalType,
    roomCategory,
    patientAge,
    tenureMonths,
    quotedTotal,
    result,
    calculating,
    setSelectedProcedureId: handleProcedureChange,
    setHospitalType,
    setRoomCategory,
    setPatientAge,
    setTenureMonths,
    setQuotedTotal,
    calculate,
  };
}
