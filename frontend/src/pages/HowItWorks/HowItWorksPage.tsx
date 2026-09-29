import React from 'react';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import {
  FileUp,
  Search,
  Scale,
  Calculator,
  Pin,
  ShieldCheck,
  ArrowRight,
} from 'lucide-react';

interface HowItWorksPageProps {
  onNavigateToStudio: () => void;
}

export const HowItWorksPage: React.FC<HowItWorksPageProps> = ({ onNavigateToStudio }) => {
  const steps = [
    {
      step: '01',
      title: 'Upload or Select a Policy',
      description:
        'Drop a real IRDAI policy PDF or pick one of the three pre-dissected reference policies (Star, Royal Sundaram, HDFC ERGO).',
      icon: <FileUp size={22} />,
      color: 'var(--lime)',
    },
    {
      step: '02',
      title: 'Clause Chunking & Indexing',
      description:
        'Each page is split into semantic clauses (Section, Heading, Verbatim Text, Page Number). Nothing is rephrased — we only index.',
      icon: <Search size={22} />,
      color: 'var(--teal)',
    },
    {
      step: '03',
      title: 'Hybrid Evidence Retrieval',
      description:
        'Hybrid keyword + vector search returns the top 5 most relevant clauses with cosine-distance scores and exact (Page, §Section) pins.',
      icon: <Pin size={22} />,
      color: 'var(--teal)',
    },
    {
      step: '04',
      title: 'Deterministic Coverage Rules',
      description:
        'The rule engine checks four clocks: Initial 30-Day, Specific 24-Month, PED 36-Month, and Room Entitlement. LLM never calculates.',
      icon: <Scale size={22} />,
      color: 'var(--yellow)',
    },
    {
      step: '05',
      title: 'Out-of-Pocket Calculator',
      description:
        'Non-medical 8% consumables, room-rent proportionality, sub-limit caps, senior co-pay, and non-network surcharges are line-itemed.',
      icon: <Calculator size={22} />,
      color: 'var(--lilac)',
    },
    {
      step: '06',
      title: 'Verdict & Uncertainty',
      description:
        'A stamped COVERED / CONDITIONAL / EXCLUDED verdict plus honest Missing Info and a concrete next-step recommendation.',
      icon: <ShieldCheck size={22} />,
      color: 'var(--lime)',
    },
  ];

  return (
    <div
      style={{
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '32px 20px',
        display: 'flex',
        flexDirection: 'column',
        gap: '40px',
      }}
    >
      <div>
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '6px',
            padding: '3px 8px',
            background: 'var(--teal)',
            border: '2px solid var(--ink)',
            fontSize: '0.75rem',
            fontWeight: 900,
            textTransform: 'uppercase',
            marginBottom: '8px',
            color: '#111111',
          }}
        >
          ★ Evidence Pipeline
        </div>
        <h1
          style={{
            fontSize: '2.25rem',
            fontWeight: 900,
            letterSpacing: '-0.02em',
            marginBottom: '8px',
          }}
        >
          How the Dissection Works
        </h1>
        <p style={{ fontSize: '1rem', opacity: 0.8, maxWidth: '640px' }}>
          Six deterministic stages convert a dense health insurance brochure into an evidence-pinned, line-itemed financial forecast.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {steps.map((s, idx) => (
          <Card key={idx} variant="sheet">
            <div
              style={{
                display: 'grid',
                gridTemplateColumns: '80px 48px 1fr',
                gap: '20px',
                alignItems: 'start',
              }}
            >
              <div
                style={{
                  fontSize: '2.25rem',
                  fontWeight: 900,
                  letterSpacing: '-0.04em',
                  opacity: 0.9,
                  fontVariantNumeric: 'tabular-nums',
                }}
              >
                {s.step}
              </div>
              <div
                style={{
                  width: '48px',
                  height: '48px',
                  border: '2px solid var(--ink)',
                  background: s.color,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: '#111111',
                  boxShadow: '3px 3px 0 var(--ink)',
                }}
                aria-hidden="true"
              >
                {s.icon}
              </div>
              <div>
                <h3 style={{ fontSize: '1.125rem', fontWeight: 900, marginBottom: '6px' }}>
                  {s.title}
                </h3>
                <p style={{ fontSize: '0.9375rem', opacity: 0.85, lineHeight: 1.55 }}>
                  {s.description}
                </p>
              </div>
            </div>
          </Card>
        ))}
      </div>

      <Card variant="hero" headerTag="DEVELOPER MODE" tagColor="lilac">
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '16px',
          }}
        >
          <div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 900, marginBottom: '6px' }}>
              Backend runs on FastAPI + pgVector at :8123
            </h3>
            <p style={{ fontSize: '0.875rem', opacity: 0.8 }}>
              Frontend uses a thin Vite proxy at /api → :8123. Every service has a deterministic fallback if the backend is offline.
            </p>
          </div>
          <Button variant="primary" size="lg" onClick={onNavigateToStudio} icon={<ArrowRight size={18} />}>
            Open the Studio Bench
          </Button>
        </div>
      </Card>

      <div
        style={{
          padding: '16px',
          border: '2px dashed var(--ink)',
          fontSize: '0.8125rem',
          fontWeight: 700,
        }}
      >
        Definition of Done for every answer: (1) Verdict Stamp (2) At least 2 evidence pins with Page·§Section (3) Line-item receipt (4) Honest missing-information list.
      </div>
    </div>
  );
};
