import React, { useState, useEffect, useCallback } from 'react';
import { useTheme } from '@/hooks/useTheme';
import { usePolicy } from '@/hooks/usePolicy';
import { Header } from '@/components/navigation/Header';
import { MobileDrawer } from '@/components/navigation/MobileDrawer';
import { HomePage } from '@/pages/Home/HomePage';
import { StudioPage } from '@/pages/Studio/StudioPage';
import { PoliciesPage } from '@/pages/Policies/PoliciesPage';
import { HowItWorksPage } from '@/pages/HowItWorks/HowItWorksPage';
import { Toast } from '@/components/ui/Toast';
import { probeBackendHealth, getCachedBackendStatus } from '@/services/api/apiClient';
import { sanitizeInput } from '@/utils/security';

type View = 'home' | 'studio' | 'policies' | 'how-it-works';

interface ToastState {
  id: number;
  message: string;
  type: 'success' | 'error' | 'info';
}

const App: React.FC = () => {
  const { theme, toggleTheme, isDark } = useTheme();
  const { activePolicyId, activePolicy, policies, selectPolicy } = usePolicy('star');

  const [activeView, setActiveView] = useState<View>('home');
  const [initialQuery, setInitialQuery] = useState<string | undefined>(undefined);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [isBackendOnline, setIsBackendOnline] = useState<boolean | null>(null);
  const [toasts, setToasts] = useState<ToastState[]>([]);

  const addToast = useCallback((message: string, type: 'success' | 'error' | 'info' = 'info') => {
    const safeMessage = sanitizeInput(message);
    const id = Date.now() + Math.random();
    setToasts((prev) => [...prev, { id, message: safeMessage, type }]);
    window.setTimeout(() => {
      setToasts((prev) => prev.filter((t) => t.id !== id));
    }, 4200);
  }, []);

  useEffect(() => {
    let mounted = true;
    probeBackendHealth().then((ok) => {
      if (mounted) {
        setIsBackendOnline(ok);
        if (ok) {
          addToast('FastAPI backend connected on :8123', 'success');
        } else {
          addToast('Backend offline — running in offline deterministic mode', 'info');
        }
      }
    });
    return () => {
      mounted = false;
    };
  }, [addToast]);

  useEffect(() => {
    const interval = window.setInterval(() => {
      probeBackendHealth().then((ok) => {
        setIsBackendOnline((prev) => (prev !== ok ? ok : prev));
      });
    }, 30000);
    return () => window.clearInterval(interval);
  }, []);

  const handleNavigate = useCallback((view: string) => {
    setActiveView(view as View);
    setMobileMenuOpen(false);
    setInitialQuery(undefined);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  const handleNavigateToStudio = useCallback((query?: string) => {
    if (query) {
      setInitialQuery(sanitizeInput(query));
    }
    setActiveView('studio');
    setMobileMenuOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  const handleSelectPolicy = useCallback((id: string) => {
    selectPolicy(id);
  }, [selectPolicy]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setMobileMenuOpen(false);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  return (
    <div
      style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}
      data-theme-applied={theme}
    >
      <Header
        activeView={activeView}
        onNavigate={handleNavigate}
        isDark={isDark}
        onToggleTheme={toggleTheme}
        activePolicyName={activePolicy.policy_name}
        isBackendOnline={isBackendOnline}
        onOpenMobileMenu={() => setMobileMenuOpen(true)}
      />

      <MobileDrawer
        isOpen={mobileMenuOpen}
        onClose={() => setMobileMenuOpen(false)}
        activeView={activeView}
        onNavigate={handleNavigate}
      />

      <main style={{ flex: 1 }}>
        {activeView === 'home' && (
          <HomePage
            activePolicy={activePolicy}
            onNavigateToStudio={handleNavigateToStudio}
            onToast={addToast}
          />
        )}

        {activeView === 'studio' && (
          <StudioPage
            policies={policies}
            activePolicyId={activePolicyId}
            activePolicy={activePolicy}
            onSelectPolicy={handleSelectPolicy}
            onToast={addToast}
            initialQuery={initialQuery}
          />
        )}

        {activeView === 'policies' && (
          <PoliciesPage
            policies={policies}
            activePolicyId={activePolicyId}
            onSelectPolicy={handleSelectPolicy}
            onNavigateToStudio={() => handleNavigateToStudio()}
          />
        )}

        {activeView === 'how-it-works' && (
          <HowItWorksPage onNavigateToStudio={() => handleNavigateToStudio()} />
        )}
      </main>

      <footer
        style={{
          borderTop: 'var(--bw) solid var(--ink)',
          background: 'var(--sheet-muted)',
          padding: '24px',
          marginTop: '32px',
        }}
      >
        <div
          style={{
            maxWidth: '1440px',
            margin: '0 auto',
            display: 'flex',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: '12px',
            fontSize: '0.75rem',
            fontWeight: 700,
          }}
        >
          <div>
            INSURIXX — The Policy, Dissected. Estimates are illustrative, not settlement promises.
          </div>
          <div>
            Backend:{' '}
            <span
              style={{
                padding: '2px 6px',
                border: '1.5px solid var(--ink)',
                background: isBackendOnline ? 'var(--lime)' : 'var(--yellow)',
                color: '#111111',
              }}
            >
              {isBackendOnline ? 'ONLINE (:8123)' : isBackendOnline === false ? 'OFFLINE MODE' : 'PROBING…'}
            </span>
          </div>
        </div>
      </footer>

      <div
        style={{
          position: 'fixed',
          bottom: '16px',
          right: '16px',
          display: 'flex',
          flexDirection: 'column',
          gap: '8px',
          zIndex: 9999,
        }}
        aria-live="polite"
      >
        {toasts.map((t) => (
          <Toast
            key={t.id}
            message={t.message}
            type={t.type}
            onClose={() => setToasts((prev) => prev.filter((x) => x.id !== t.id))}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
