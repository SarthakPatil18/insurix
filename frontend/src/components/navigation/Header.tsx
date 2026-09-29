import React from 'react';
import { Sun, Moon, Shield, Radio, Menu } from 'lucide-react';
import { Button } from '../ui/Button';

interface HeaderProps {
  activeView: string;
  onNavigate: (view: string) => void;
  isDark: boolean;
  onToggleTheme: () => void;
  activePolicyName: string;
  isBackendOnline: boolean | null;
  onOpenMobileMenu?: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  activeView,
  onNavigate,
  isDark,
  onToggleTheme,
  activePolicyName,
  isBackendOnline,
  onOpenMobileMenu,
}) => {
  return (
    <header
      style={{
        borderBottom: 'var(--bw) solid var(--ink)',
        background: 'var(--sheet)',
        padding: '12px 24px',
        position: 'sticky',
        top: 0,
        zIndex: 1000,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        boxShadow: '0 2px 0 var(--ink)',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
        {onOpenMobileMenu && (
          <button
            onClick={onOpenMobileMenu}
            aria-label="Open navigation menu"
            style={{
              display: 'inline-flex',
              padding: '6px',
              border: '2px solid var(--ink)',
              background: 'transparent',
              boxShadow: 'none',
            }}
            className="md:hidden"
          >
            <Menu size={20} />
          </button>
        )}
        <div
          onClick={() => onNavigate('home')}
          style={{ cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px' }}
        >
          <div
            style={{
              width: '32px',
              height: '32px',
              background: 'var(--ink)',
              color: 'var(--lime)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 900,
              fontSize: '1.25rem',
              border: '2px solid var(--ink)',
            }}
          >
            ⚡
          </div>
          <div>
            <div style={{ fontSize: '1.25rem', fontWeight: 900, letterSpacing: '-0.02em', lineHeight: 1 }}>
              INSURIXX
            </div>
            <div style={{ fontSize: '0.625rem', fontWeight: 700, letterSpacing: '0.08em', opacity: 0.75, textTransform: 'uppercase' }}>
              The Policy, Dissected
            </div>
          </div>
        </div>

        {/* Desktop Nav Links */}
        <nav style={{ display: 'flex', gap: '8px', marginLeft: '16px' }}>
          {[
            { id: 'home', label: 'Home' },
            { id: 'studio', label: 'Studio Workbench' },
            { id: 'policies', label: 'Policies' },
            { id: 'how-it-works', label: 'How It Works' },
          ].map((item) => (
            <button
              key={item.id}
              onClick={() => onNavigate(item.id)}
              style={{
                padding: '6px 14px',
                fontSize: '0.875rem',
                fontWeight: 700,
                border: '2px solid var(--ink)',
                background: activeView === item.id ? 'var(--lime)' : 'transparent',
                color: activeView === item.id ? '#111111' : 'var(--ink)',
                boxShadow: activeView === item.id ? '2px 2px 0 var(--ink)' : 'none',
                transform: activeView === item.id ? 'translate(-1px, -1px)' : 'none',
              }}
            >
              {item.label}
            </button>
          ))}
        </nav>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        {/* Active Policy Status Pill */}
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '6px',
            padding: '4px 10px',
            background: 'var(--sheet-muted)',
            border: '2px solid var(--ink)',
            fontSize: '0.8125rem',
            fontWeight: 700,
          }}
          title="Current Active Policy"
        >
          <Shield size={14} color="var(--ink)" />
          <span style={{ maxWidth: '160px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
            {activePolicyName}
          </span>
        </div>

        {/* Backend Live Indicator */}
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '6px',
            padding: '4px 8px',
            background: isBackendOnline ? 'var(--lime)' : 'var(--yellow)',
            color: '#111111',
            border: '2px solid var(--ink)',
            fontSize: '0.75rem',
            fontWeight: 800,
            textTransform: 'uppercase',
          }}
          title={isBackendOnline ? 'FastAPI Backend Online on :8123' : 'Running in Offline Deterministic Mode'}
        >
          <Radio size={12} />
          <span>{isBackendOnline ? 'API Connected' : 'Local Engine'}</span>
        </div>

        {/* Theme Toggle Button */}
        <Button
          variant="secondary"
          size="sm"
          onClick={onToggleTheme}
          aria-label={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
          title={isDark ? 'Switch to Light Lab Mode' : 'Switch to Night Lab Mode'}
          style={{ padding: '6px' }}
        >
          {isDark ? <Sun size={18} /> : <Moon size={18} />}
        </Button>
      </div>
    </header>
  );
};
