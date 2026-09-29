import React, { useState } from 'react';
import { Policy, Clause } from '@/types/policy';
import { PolicySelector } from '@/components/policy/PolicySelector';
import { PolicySummaryCard } from '@/components/policy/PolicySummaryCard';
import { ClauseViewer } from '@/components/policy/ClauseViewer';
import { TreatmentCalculator } from '@/components/calculator/TreatmentCalculator';
import { CostReceipt } from '@/components/receipt/CostReceipt';
import { EvidencePanel } from '@/components/evidence/EvidencePanel';
import { RedStringBoard } from '@/components/evidence/RedStringBoard';
import { VerdictStamp } from '@/components/ui/VerdictStamp';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { useCalculator } from '@/hooks/useCalculator';
import { useChat } from '@/hooks/useChat';
import { Send, AlertCircle, MessageSquare } from 'lucide-react';

interface StudioPageProps {
  policies: Policy[];
  activePolicyId: string;
  activePolicy: Policy;
  onSelectPolicy: (id: string) => void;
  onToast: (msg: string, type?: 'success' | 'error' | 'info') => void;
  initialQuery?: string;
}

export const StudioPage: React.FC<StudioPageProps> = ({
  policies,
  activePolicyId,
  activePolicy,
  onSelectPolicy,
  onToast,
  initialQuery,
}) => {
  const [inputQuery, setInputQuery] = useState(initialQuery || '');
  const [selectedClause, setSelectedClause] = useState<Clause | null>(null);
  const [isClauseModalOpen, setIsClauseModalOpen] = useState(false);

  // Chat Hook
  const { messages, loading: chatLoading, sendMessage } = useChat(activePolicyId);

  // Calculator Hook
  const {
    treatments,
    selectedProcedureId,
    hospitalType,
    roomCategory,
    patientAge,
    tenureMonths,
    quotedTotal,
    result,
    calculating,
    setSelectedProcedureId,
    setHospitalType,
    setRoomCategory,
    setPatientAge,
    setTenureMonths,
    setQuotedTotal,
    calculate,
  } = useCalculator(activePolicyId);

  const handleSendChat = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputQuery.trim()) {
      sendMessage(inputQuery.trim());
      setInputQuery('');
    }
  };

  const handleCitationClick = (citation: { page: number; section: string; text: string }) => {
    const fullClause = activePolicy.clauses.find((c) => c.page === citation.page) || {
      page: citation.page,
      section: citation.section,
      heading: 'Policy Clause',
      text: citation.text,
    };
    setSelectedClause(fullClause);
    setIsClauseModalOpen(true);
  };

  const presetQuestions = [
    'Is knee replacement covered?',
    'What is the cataract sub-limit?',
    'Does deluxe room have proportionate deductions?',
    'What is the pre-existing disease waiting period?',
  ];

  return (
    <div style={{ maxWidth: '1440px', margin: '0 auto', padding: '24px 20px', display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Policy Selector Banner */}
      <PolicySelector
        policies={policies}
        activePolicyId={activePolicyId}
        onSelectPolicy={(id) => {
          onSelectPolicy(id);
          onToast(`Switched active policy to ${policies.find((p) => p.id === id)?.policy_name}`, 'info');
        }}
      />

      {/* Policy Schedule Summary */}
      <PolicySummaryCard policy={activePolicy} />

      {/* Main Two-Panel Studio Workbench */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(420px, 1fr))', gap: '24px', alignItems: 'start' }}>
        {/* ========================================================
            LEFT PANEL: ASK THE POLICY
            ======================================================== */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <Card headerTag="ASK THE POLICY — EVIDENCE CHAT" tagColor="teal">
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {/* Chat Thread */}
              <div
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '16px',
                  maxHeight: '480px',
                  overflowY: 'auto',
                  paddingRight: '6px',
                }}
              >
                {messages.map((msg) => (
                  <div
                    key={msg.id}
                    style={{
                      display: 'flex',
                      flexDirection: 'column',
                      alignItems: msg.sender === 'user' ? 'flex-end' : 'flex-start',
                    }}
                  >
                    {msg.sender === 'user' ? (
                      <div
                        style={{
                          background: 'var(--sheet-muted)',
                          border: '2px solid var(--ink)',
                          padding: '10px 14px',
                          fontWeight: 700,
                          fontSize: '0.9375rem',
                          maxWidth: '85%',
                          boxShadow: '2px 2px 0 var(--ink)',
                        }}
                      >
                        {msg.text}
                      </div>
                    ) : (
                      <div
                        style={{
                          background: 'var(--sheet)',
                          border: '2px solid var(--ink)',
                          padding: '16px',
                          maxWidth: '100%',
                          boxShadow: 'var(--shadow-sm)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '12px',
                        }}
                      >
                        {msg.response && (
                          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '8px' }}>
                            <VerdictStamp verdict={msg.response.verdict} label={msg.response.verdict_label} />
                            <span
                              style={{
                                fontSize: '0.6875rem',
                                fontWeight: 800,
                                textTransform: 'uppercase',
                                padding: '2px 6px',
                                background: 'var(--sheet-muted)',
                                border: '1px solid var(--ink)',
                              }}
                            >
                              Evidence Match: {msg.response.confidence}
                            </span>
                          </div>
                        )}

                        <div style={{ fontSize: '0.9375rem', lineHeight: 1.5, fontWeight: 500 }}>
                          {msg.text}
                        </div>

                        {/* Evidence Panel with Verbatim Citations */}
                        {msg.response?.evidence && msg.response.evidence.length > 0 && (
                          <EvidencePanel
                            evidence={msg.response.evidence}
                            onSelectCitation={handleCitationClick}
                          />
                        )}

                        {/* Red String Board Trace */}
                        {msg.response?.evidence && msg.response.evidence.length > 0 && (
                          <RedStringBoard
                            evidence={msg.response.evidence}
                            verdictLabel={msg.response.verdict_label}
                            totalCost={msg.response.cost_estimate?.total_cost}
                            payable={msg.response.cost_estimate?.payable}
                          />
                        )}

                        {/* Missing Information / Uncertainty Box */}
                        {msg.response?.uncertainty?.missing_info && msg.response.uncertainty.missing_info.length > 0 && (
                          <div style={{ padding: '10px', background: 'rgba(184, 146, 255, 0.1)', border: '2px dashed var(--ink)' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.75rem', fontWeight: 800, color: 'var(--ink)' }}>
                              <AlertCircle size={14} />
                              UNCERTAINTY DETECTED — MISSING CLAUSE DETAILS:
                            </div>
                            <ul style={{ margin: '4px 0 0 16px', fontSize: '0.75rem', opacity: 0.85 }}>
                              {msg.response.uncertainty.missing_info.map((item, idx) => (
                                <li key={idx}>{item}</li>
                              ))}
                            </ul>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                ))}

                {chatLoading && (
                  <div style={{ padding: '12px', background: 'var(--sheet)', border: '2px dashed var(--ink)', fontStyle: 'italic', fontSize: '0.875rem' }}>
                    Scanning {activePolicy.policy_name} wording & retrieving IRDAI clauses...
                  </div>
                )}
              </div>

              {/* Preset Buttons */}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                {presetQuestions.map((q, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => {
                      setInputQuery(q);
                      sendMessage(q);
                    }}
                    style={{
                      padding: '4px 8px',
                      fontSize: '0.75rem',
                      fontWeight: 700,
                      border: '1.5px solid var(--ink)',
                      background: 'var(--sheet-muted)',
                      cursor: 'pointer',
                    }}
                  >
                    {q}
                  </button>
                ))}
              </div>

              {/* Chat Form Input */}
              <form onSubmit={handleSendChat} style={{ display: 'flex', gap: '8px', marginTop: '6px' }}>
                <input
                  type="text"
                  placeholder="Ask policy query (e.g. cataract surgery waiting period)..."
                  value={inputQuery}
                  onChange={(e) => setInputQuery(e.target.value)}
                  style={{
                    flex: 1,
                    padding: '10px 14px',
                    border: 'var(--bw) solid var(--ink)',
                    background: 'var(--sheet)',
                    fontSize: '0.9375rem',
                    fontWeight: 600,
                    boxShadow: 'var(--shadow-sm)',
                  }}
                />
                <Button
                  variant="primary"
                  type="submit"
                  disabled={chatLoading || !inputQuery.trim()}
                  icon={<Send size={16} />}
                >
                  Ask
                </Button>
              </form>
            </div>
          </Card>
        </div>

        {/* ========================================================
            RIGHT PANEL: WHAT WILL I PAY?
            ======================================================== */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <TreatmentCalculator
            policy={activePolicy}
            treatments={treatments}
            selectedProcedureId={selectedProcedureId}
            hospitalType={hospitalType}
            roomCategory={roomCategory}
            patientAge={patientAge}
            tenureMonths={tenureMonths}
            quotedTotal={quotedTotal}
            result={result}
            calculating={calculating}
            onSelectProcedure={setSelectedProcedureId}
            onSelectHospitalType={setHospitalType}
            onSelectRoomCategory={setRoomCategory}
            onChangePatientAge={setPatientAge}
            onChangeTenureMonths={setTenureMonths}
            onChangeQuotedTotal={setQuotedTotal}
            onRunCalculation={calculate}
          />

          <CostReceipt result={result} policyName={activePolicy.policy_name} />
        </div>
      </div>

      {/* Verbatim Clause Viewer Modal */}
      <ClauseViewer
        clause={selectedClause}
        isOpen={isClauseModalOpen}
        onClose={() => setIsClauseModalOpen(false)}
        policyName={activePolicy.policy_name}
      />
    </div>
  );
};
