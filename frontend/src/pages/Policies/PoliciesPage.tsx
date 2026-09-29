import React, { useState } from 'react';
import { Policy, Clause } from '@/types/policy';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { Button } from '@/components/ui/Button';
import { ClauseViewer } from '@/components/policy/ClauseViewer';
import { Shield, BookOpen, Layers } from 'lucide-react';
import { formatLakhs } from '@/utils/money';

interface PoliciesPageProps {
  policies: Policy[];
  activePolicyId: string;
  onSelectPolicy: (id: string) => void;
  onNavigateToStudio: () => void;
}

export const PoliciesPage: React.FC<PoliciesPageProps> = ({
  policies,
  activePolicyId,
  onSelectPolicy,
  onNavigateToStudio,
}) => {
  const [selectedClause, setSelectedClause] = useState<Clause | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const activePolicy = policies.find((p) => p.id === activePolicyId) || policies[0];

  const handleOpenClause = (clause: Clause) => {
    setSelectedClause(clause);
    setIsModalOpen(true);
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '32px 20px', display: 'flex', flexDirection: 'column', gap: '32px' }}>
      <div>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '3px 8px', background: 'var(--lime)', border: '2px solid var(--ink)', fontSize: '0.75rem', fontWeight: 900, textTransform: 'uppercase', marginBottom: '8px' }}>
          ★ Policy Clause Archive
        </div>
        <h1 style={{ fontSize: '2.25rem', fontWeight: 900, letterSpacing: '-0.02em', marginBottom: '8px' }}>
          Filed IRDAI Policy Wordings
        </h1>
        <p style={{ fontSize: '1rem', opacity: 0.8, maxWidth: '640px' }}>
          Browse official wordings, schedules, sub-limit tables, and verified section clauses across preloaded insurers.
        </p>
      </div>

      {/* Insurer Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: 'var(--bw) solid var(--ink)', paddingBottom: '4px' }}>
        {policies.map((p) => {
          const isActive = p.id === activePolicy.id;
          return (
            <button
              key={p.id}
              onClick={() => onSelectPolicy(p.id)}
              style={{
                padding: '8px 18px',
                fontSize: '0.9375rem',
                fontWeight: 800,
                border: '2px solid var(--ink)',
                background: isActive ? 'var(--lime)' : 'var(--sheet)',
                color: isActive ? '#111111' : 'var(--ink)',
                boxShadow: isActive ? '3px 3px 0 var(--ink)' : 'none',
                transform: isActive ? 'translate(-1px, -1px)' : 'none',
              }}
            >
              {p.insurer} ({formatLakhs(p.sum_insured)})
            </button>
          );
        })}
      </div>

      {/* Policy Details */}
      <Card headerTag="OFFICIAL POLICY CLAUSES" tagColor="teal">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 900 }}>{activePolicy.policy_name}</h2>
            <div style={{ fontSize: '0.875rem', opacity: 0.75 }}>
              Standard 1-Year Tenure • IRDAI Registered Product Schedule
            </div>
          </div>
          <Button variant="primary" onClick={onNavigateToStudio}>
            Dissect in Studio Workbench →
          </Button>
        </div>

        {/* Clause List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
          {activePolicy.clauses.map((clause, idx) => (
            <div
              key={idx}
              className="paper-sheet"
              style={{
                padding: '16px 20px',
                border: '2px solid var(--ink)',
                background: 'var(--sheet-muted)',
                cursor: 'pointer',
              }}
              onClick={() => handleOpenClause(clause)}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <span style={{ fontWeight: 800, fontSize: '1rem', color: 'var(--ink)' }}>
                  {clause.heading}
                </span>
                <div style={{ display: 'flex', gap: '6px' }}>
                  <Badge color="teal">Page {clause.page}</Badge>
                  <Badge color="neutral">§{clause.section}</Badge>
                </div>
              </div>
              <p className="clause-quote" style={{ fontSize: '0.9375rem', margin: 0, opacity: 0.9 }}>
                "{clause.text}"
              </p>
              <div style={{ marginTop: '8px', fontSize: '0.75rem', fontWeight: 700, color: 'var(--ink)', textDecoration: 'underline' }}>
                Click to inspect full clause context ↗
              </div>
            </div>
          ))}
        </div>
      </Card>

      <ClauseViewer
        clause={selectedClause}
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        policyName={activePolicy.policy_name}
      />
    </div>
  );
};
