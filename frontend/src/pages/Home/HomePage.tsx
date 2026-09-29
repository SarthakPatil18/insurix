import React, { useState } from 'react';
import { Policy } from '@/types/policy';
import { PolicyStack3D } from '@/components/policy/PolicyStack3D';
import { PolicyUploadZone } from '@/components/upload/PolicyUploadZone';
import { Button } from '@/components/ui/Button';
import { ArrowRight, ShieldCheck, Cpu, Scale, Search, CheckCircle2 } from 'lucide-react';

interface HomePageProps {
  activePolicy: Policy;
  onNavigateToStudio: (initialQuery?: string) => void;
  onToast: (msg: string, type?: 'success' | 'error' | 'info') => void;
}

export const HomePage: React.FC<HomePageProps> = ({
  activePolicy,
  onNavigateToStudio,
  onToast,
}) => {
  const [quickQuery, setQuickQuery] = useState('');

  const sampleQuestions = [
    'Is knee replacement covered under Star Health?',
    'What is the cataract sub-limit per eye?',
    'Explain the 36-month pre-existing disease waiting period',
    'Does single A/C room trigger proportionate deductions?',
  ];

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (quickQuery.trim()) {
      onNavigateToStudio(quickQuery.trim());
    } else {
      onNavigateToStudio();
    }
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '32px 20px', display: 'flex', flexDirection: 'column', gap: '48px' }}>
      {/* Hero Section */}
      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '32px', alignItems: 'center' }}>
        <div>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '4px 10px',
              background: 'var(--lime)',
              color: '#111111',
              border: '2px solid var(--ink)',
              fontSize: '0.8125rem',
              fontWeight: 900,
              textTransform: 'uppercase',
              marginBottom: '16px',
              boxShadow: '2px 2px 0 var(--ink)',
            }}
          >
            ★ AI Policy Intelligence Bench
          </div>

          <h1
            style={{
              fontSize: 'clamp(2.5rem, 5vw + 1rem, 4.25rem)',
              fontWeight: 900,
              lineHeight: 1.05,
              letterSpacing: '-0.03em',
              marginBottom: '18px',
            }}
          >
            The Policy, <span style={{ background: 'var(--lime)', padding: '0 4px', border: '3px solid var(--ink)', boxShadow: '4px 4px 0 var(--ink)' }}>Dissected.</span>
          </h1>

          <p style={{ fontSize: '1.125rem', lineHeight: 1.6, opacity: 0.85, marginBottom: '24px', maxWidth: '520px' }}>
            We pull apart dense 60-page Indian health insurance policies on a lab bench. Pin verifiable evidence to the page and project out-of-pocket costs with zero fine-print surprises.
          </p>

          {/* Quick Query Form */}
          <form onSubmit={handleSearchSubmit} style={{ display: 'flex', gap: '8px', maxWidth: '520px', marginBottom: '16px' }}>
            <div style={{ flex: 1, position: 'relative' }}>
              <input
                type="text"
                placeholder="Ask any policy question (e.g. knee replacement coverage)..."
                value={quickQuery}
                onChange={(e) => setQuickQuery(e.target.value)}
                style={{
                  width: '100%',
                  padding: '12px 16px',
                  border: 'var(--bw) solid var(--ink)',
                  background: 'var(--sheet)',
                  fontSize: '0.9375rem',
                  fontWeight: 600,
                  boxShadow: 'var(--shadow-sm)',
                }}
              />
            </div>
            <Button variant="primary" type="submit" icon={<ArrowRight size={18} />}>
              Dissect
            </Button>
          </form>

          {/* Preset Questions Chips */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
            {sampleQuestions.map((q, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => onNavigateToStudio(q)}
                style={{
                  padding: '4px 8px',
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  border: '1.5px solid var(--ink)',
                  background: 'var(--sheet-muted)',
                  color: 'var(--ink)',
                  cursor: 'pointer',
                  textAlign: 'left',
                }}
              >
                {q}
              </button>
            ))}
          </div>
        </div>

        {/* Hero Memorable Object — The Physical Policy Stack */}
        <div>
          <PolicyStack3D
            policyName={activePolicy.policy_name}
            pageCount={60}
            onPageClick={(page) => {
              onToast(`Jumped to Page ${page} landmark clause`, 'info');
              onNavigateToStudio();
            }}
          />
        </div>
      </section>

      {/* 3 Physical Pillars */}
      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px' }}>
        <div className="paper-sheet" style={{ padding: '24px' }}>
          <div style={{ width: '36px', height: '36px', background: 'var(--teal)', border: '2px solid var(--ink)', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '14px', boxShadow: '2px 2px 0 var(--ink)' }}>
            <Search size={20} color="#111111" />
          </div>
          <h3 style={{ fontSize: '1.125rem', fontWeight: 900, marginBottom: '8px' }}>
            Verifiable Evidence Citations
          </h3>
          <p style={{ fontSize: '0.875rem', opacity: 0.8, lineHeight: 1.5 }}>
            Every answer links directly to an exact clause with page and section numbers (e.g. <em>Page 18, §4.2</em>). We strictly enforce: <strong>Cite or don't ship</strong>.
          </p>
        </div>

        <div className="paper-sheet" style={{ padding: '24px' }}>
          <div style={{ width: '36px', height: '36px', background: 'var(--lime)', border: '2px solid var(--ink)', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '14px', boxShadow: '2px 2px 0 var(--ink)' }}>
            <Scale size={20} color="#111111" />
          </div>
          <h3 style={{ fontSize: '1.125rem', fontWeight: 900, marginBottom: '8px' }}>
            14-Rule Deterministic Ledger
          </h3>
          <p style={{ fontSize: '0.875rem', opacity: 0.8, lineHeight: 1.5 }}>
            LLMs are never allowed to perform financial arithmetic. Deductions satisfy the ledger identity: <strong>Total Quoted - Deductions === Payable</strong> down to the exact rupee.
          </p>
        </div>

        <div className="paper-sheet" style={{ padding: '24px' }}>
          <div style={{ width: '36px', height: '36px', background: 'var(--yellow)', border: '2px solid var(--ink)', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '14px', boxShadow: '2px 2px 0 var(--ink)' }}>
            <Cpu size={20} color="#111111" />
          </div>
          <h3 style={{ fontSize: '1.125rem', fontWeight: 900, marginBottom: '8px' }}>
            Proportional Penalty Simulator
          </h3>
          <p style={{ fontSize: '0.875rem', opacity: 0.8, lineHeight: 1.5 }}>
            Taking a deluxe room penalizes your surgeon, doctor, and OT fees. See real-time room rent deduction slabs before hospital admission.
          </p>
        </div>
      </section>

      {/* Upload Callout Section */}
      <section>
        <div style={{ marginBottom: '14px' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 900 }}>Upload Your Insurer PDF</h2>
          <p style={{ fontSize: '0.875rem', opacity: 0.8 }}>
            Drop any Star Health, HDFC ERGO, Care, or Niva Bupa policy wording PDF for immediate clause extraction.
          </p>
        </div>
        <PolicyUploadZone
          onUploadSuccess={() => onNavigateToStudio()}
          onToast={onToast}
        />
      </section>
    </div>
  );
};
