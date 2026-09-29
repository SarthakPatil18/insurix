import React from 'react';
import { Treatment, CalculationResult } from '@/types/estimate';
import { Policy } from '@/types/policy';
import { Card } from '../ui/Card';
import { Button } from '../ui/Button';
import { PenaltySlab3D } from './PenaltySlab3D';
import { WaitingDial3D } from './WaitingDial3D';
import { formatINR } from '@/utils/money';
import { Calculator, Hospital, Bed, User, Calendar, DollarSign } from 'lucide-react';

interface TreatmentCalculatorProps {
  policy: Policy;
  treatments: Treatment[];
  selectedProcedureId: string;
  hospitalType: 'network' | 'non_network';
  roomCategory: 'general' | 'twin_sharing' | 'single_ac' | 'deluxe' | 'suite';
  patientAge: number;
  tenureMonths: number;
  quotedTotal: number;
  result: CalculationResult | null;
  calculating: boolean;
  onSelectProcedure: (id: string) => void;
  onSelectHospitalType: (type: 'network' | 'non_network') => void;
  onSelectRoomCategory: (room: 'general' | 'twin_sharing' | 'single_ac' | 'deluxe' | 'suite') => void;
  onChangePatientAge: (age: number) => void;
  onChangeTenureMonths: (tenure: number) => void;
  onChangeQuotedTotal: (total: number) => void;
  onRunCalculation: () => void;
}

export const TreatmentCalculator: React.FC<TreatmentCalculatorProps> = ({
  policy,
  treatments,
  selectedProcedureId,
  hospitalType,
  roomCategory,
  patientAge,
  tenureMonths,
  quotedTotal,
  result,
  calculating,
  onSelectProcedure,
  onSelectHospitalType,
  onSelectRoomCategory,
  onChangePatientAge,
  onChangeTenureMonths,
  onChangeQuotedTotal,
  onRunCalculation,
}) => {
  const roomRates: Record<string, number> = {
    general: 2500,
    twin_sharing: 4000,
    single_ac: 6000,
    deluxe: 9000,
    suite: 14000,
  };

  const roomLimit = Math.round(policy.sum_insured * 0.01);
  const actualRoomRate = roomRates[roomCategory] || 6000;
  const currentTreatment = treatments.find((t) => t.id === selectedProcedureId) || treatments[0];

  return (
    <Card headerTag="WHAT WILL I PAY? — CALCULATOR" tagColor="lime">
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {/* Procedure Selector */}
        <div>
          <label style={{ display: 'block', fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', marginBottom: '6px' }}>
            1. Select Medical Procedure / Surgery
          </label>
          <select
            value={selectedProcedureId}
            onChange={(e) => onSelectProcedure(e.target.value)}
            style={{
              width: '100%',
              padding: '10px 12px',
              border: 'var(--bw) solid var(--ink)',
              background: 'var(--sheet)',
              fontSize: '0.9375rem',
              fontWeight: 700,
              boxShadow: 'var(--shadow-sm)',
            }}
          >
            {treatments.map((t) => (
              <option key={t.id} value={t.id}>
                {t.name} (ICD: {t.icd}) — Avg {formatINR(t.average)}
              </option>
            ))}
          </select>
        </div>

        {/* Hospital Type & Room Category */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '12px' }}>
          <div>
            <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', marginBottom: '6px' }}>
              <Hospital size={14} /> 2. Hospital Type
            </label>
            <div style={{ display: 'flex', gap: '6px' }}>
              {(['network', 'non_network'] as const).map((type) => (
                <button
                  key={type}
                  type="button"
                  onClick={() => onSelectHospitalType(type)}
                  style={{
                    flex: 1,
                    padding: '8px 10px',
                    fontSize: '0.8125rem',
                    fontWeight: 800,
                    border: '2px solid var(--ink)',
                    background: hospitalType === type ? 'var(--lime)' : 'var(--sheet-muted)',
                    color: hospitalType === type ? '#111111' : 'var(--ink)',
                    boxShadow: hospitalType === type ? '2px 2px 0 var(--ink)' : 'none',
                  }}
                >
                  {type === 'network' ? 'Cashless Network' : 'Non-Network (10%)'}
                </button>
              ))}
            </div>
          </div>

          <div>
            <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', marginBottom: '6px' }}>
              <Bed size={14} /> 3. Room Category
            </label>
            <select
              value={roomCategory}
              onChange={(e) => onSelectRoomCategory(e.target.value as any)}
              style={{
                width: '100%',
                padding: '8px 10px',
                border: 'var(--bw) solid var(--ink)',
                background: 'var(--sheet)',
                fontSize: '0.875rem',
                fontWeight: 700,
              }}
            >
              <option value="general">General Ward (~₹2,500/day)</option>
              <option value="twin_sharing">Twin Sharing (~₹4,000/day)</option>
              <option value="single_ac">Single Standard A/C (~₹6,000/day)</option>
              <option value="deluxe">Deluxe Room (~₹9,000/day)</option>
              <option value="suite">Suite (~₹14,000/day)</option>
            </select>
          </div>
        </div>

        {/* Patient Age & Policy Tenure Sliders */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '12px' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
              <label style={{ fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', display: 'flex', alignItems: 'center', gap: '4px' }}>
                <User size={14} /> Patient Age: <strong>{patientAge} yrs</strong>
              </label>
              {patientAge >= 60 && (
                <span style={{ fontSize: '0.6875rem', fontWeight: 800, color: 'var(--red)' }}>
                  10% Copay (60+)
                </span>
              )}
            </div>
            <input
              type="range"
              min={18}
              max={85}
              value={patientAge}
              onChange={(e) => onChangePatientAge(Number(e.target.value))}
              style={{ width: '100%', accentColor: 'var(--ink)' }}
            />
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
              <label style={{ fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', display: 'flex', alignItems: 'center', gap: '4px' }}>
                <Calendar size={14} /> Policy Tenure: <strong>{tenureMonths} mos</strong>
              </label>
              <span style={{ fontSize: '0.6875rem', fontWeight: 800, color: tenureMonths >= 24 ? 'var(--lime)' : 'var(--red)' }}>
                {tenureMonths >= 24 ? 'Past 24m' : 'Under 24m'}
              </span>
            </div>
            <input
              type="range"
              min={1}
              max={60}
              value={tenureMonths}
              onChange={(e) => onChangeTenureMonths(Number(e.target.value))}
              style={{ width: '100%', accentColor: 'var(--ink)' }}
            />
          </div>
        </div>

        {/* Quoted Total Bill Input */}
        <div>
          <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8125rem', fontWeight: 800, textTransform: 'uppercase', marginBottom: '6px' }}>
            <DollarSign size={14} /> 4. Quoted Hospital Total Bill (₹)
          </label>
          <input
            type="number"
            step="1000"
            value={quotedTotal}
            onChange={(e) => onChangeQuotedTotal(Number(e.target.value))}
            style={{
              width: '100%',
              padding: '10px 14px',
              border: 'var(--bw) solid var(--ink)',
              background: 'var(--sheet)',
              fontSize: '1.125rem',
              fontWeight: 900,
              fontFamily: 'var(--font-display)',
              boxShadow: 'var(--shadow-sm)',
            }}
          />
        </div>

        {/* Embedded Interactive Visual Proofs */}
        <PenaltySlab3D
          roomLimit={roomLimit}
          actualRate={actualRoomRate}
          proportionalDeduction={result ? Math.round(result.total_cost * 0.18 * ((actualRoomRate - roomLimit) / actualRoomRate)) : 0}
          roomCategory={roomCategory}
        />

        {currentTreatment.specific_waiting && (
          <WaitingDial3D
            tenureMonths={tenureMonths}
            requiredMonths={24}
            label={`${currentTreatment.name} Clock`}
          />
        )}

        <Button
          variant="primary"
          size="lg"
          onClick={onRunCalculation}
          disabled={calculating}
          icon={<Calculator size={18} />}
          style={{ width: '100%', marginTop: '4px' }}
        >
          {calculating ? 'Dissecting Policy Deductions...' : 'Recalculate Out-of-Pocket Liability'}
        </Button>
      </div>
    </Card>
  );
};
