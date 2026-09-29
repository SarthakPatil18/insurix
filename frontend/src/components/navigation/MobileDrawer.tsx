import React from 'react';
import { X, Shield, FileText, Activity, HelpCircle, Upload } from 'lucide-react';
import { Button } from '../ui/Button';

interface MobileDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  activeView: string;
  onNavigate: (view: string) => void;
}

export const MobileDrawer: React.FC<MobileDrawerProps> = ({
  isOpen,
  onClose,
  activeView,
  onNavigate,
}) => {
  if (!isOpen) return null;

  const navItems = [
    { id: 'home', label: 'Home Page', icon: <FileText size={18} /> },
    { id: 'studio', label: 'Studio Workbench', icon: <Activity size={18} /> },
    { id: 'policies', label: 'Policy Clauses', icon: <Shield size={18} /> },
    { id: 'how-it-works', label: 'How It Works', icon: <HelpCircle size={18} /> },
  ];

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(17, 17, 17, 0.65)',
        zIndex: 10000,
        display: 'flex',
      }}
      onClick={onClose}
    >
      <div
        className="paper-sheet"
        style={{
          width: '280px',
          height: '100%',
          background: 'var(--sheet)',
          display: 'flex',
          flexDirection: 'column',
          boxShadow: 'var(--shadow-xl)',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '16px 20px',
            borderBottom: 'var(--bw) solid var(--ink)',
            background: 'var(--lime)',
            color: '#111111',
          }}
        >
          <span style={{ fontWeight: 900, fontSize: '1.125rem' }}>NAVIGATION</span>
          <Button variant="ghost" size="sm" onClick={onClose} style={{ padding: '4px' }}>
            <X size={20} />
          </Button>
        </div>

        <nav style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {navItems.map((item) => (
            <button
              key={item.id}
              onClick={() => {
                onNavigate(item.id);
                onClose();
              }}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '12px 16px',
                fontSize: '1rem',
                fontWeight: 700,
                border: '2px solid var(--ink)',
                background: activeView === item.id ? 'var(--lime)' : 'var(--sheet)',
                color: activeView === item.id ? '#111111' : 'var(--ink)',
                boxShadow: activeView === item.id ? '3px 3px 0 var(--ink)' : 'none',
                textAlign: 'left',
              }}
            >
              {item.icon}
              {item.label}
            </button>
          ))}
        </nav>
      </div>
    </div>
  );
};
