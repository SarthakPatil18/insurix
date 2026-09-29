# Script to generate index.html for Insurix
import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Insurix — AI Health Insurance Intelligence | Policy Confusion → Financial Clarity</title>
  <meta name="description" content="Insurix converts complex health insurance policies into clear answers about coverage, treatment eligibility, and expected out-of-pocket costs with 99.2% evidence accuracy.">
  <meta name="keywords" content="health insurance, policy intelligence, IRDAI, out of pocket calculator, medical coverage, Star Health, HDFC ERGO">
  
  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Insurix — AI Health Insurance Intelligence">
  <meta property="og:description" content="Policy confusion → Financial clarity. Evidence-backed answers, out-of-pocket costs, and zero fine-print surprises.">
  <meta property="og:url" content="https://insurix.ai">
  
  <!-- Favicon SVG -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2216%22 fill=%22%23111111%22/><path d=%22M24 24h52v14H38v10h34v14H38v14h38v14H24z%22 fill=%22%23DDF247%22/></svg>">

  <!-- Google Font: Space Grotesk -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       NEO-BRUTALIST DESIGN SYSTEM TOKENS & RESET
       ========================================================================== */
    :root {
      /* Colors — Light Mode (Default) */
      --bg: #F7F3EC;
      --black: #111111;
      --white: #FFFFFF;
      --gray: #EDEDED;
      --lime: #DDF247;
      --purple: #B892FF;
      --pink: #FFB3D1;
      --cyan: #58D9C9;
      --electric-blue: #6BB7FF;
      --neon-orange: #FFB454;
      --neon-mint: #BFFFD8;
      --grid-line: rgba(17, 17, 17, 0.055);
      
      /* Typography */
      --font-main: "Space Grotesk", Arial, sans-serif;
      
      /* Spacing Tokens */
      --space-3xs: 3px;
      --space-2xs: 6px;
      --space-xs: 10px;
      --space-sm: 14px;
      --space-md: 18px;
      --space-lg: 24px;
      --space-xl: 34px;
      --space-2xl: 48px;
      --space-3xl: 72px;

      /* Motion */
      --ease-fast: 150ms ease;
      --ease-standard: 220ms ease;
      --ease-reveal: 350ms cubic-bezier(0.4, 0, 0.2, 1);
      --ease-scroll: 520ms ease;
    }

    body.dark {
      --bg: #111111;
      --black: #F7F3EC;
      --white: #1D1D1D;
      --gray: #2B2B2B;
      --lime: #4F6315;
      --purple: #5C35BD;
      --pink: #9E2A56;
      --cyan: #176F68;
      --electric-blue: #1F5F97;
      --neon-orange: #8F5419;
      --neon-mint: #27633A;
      --grid-line: rgba(247, 243, 236, 0.08);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      font-family: var(--font-main);
      color: var(--black);
      background:
        linear-gradient(90deg, var(--grid-line) 1px, transparent 1px),
        linear-gradient(var(--grid-line) 1px, transparent 1px),
        var(--bg);
      background-size: 34px 34px;
      line-height: 1.45;
      min-height: 100vh;
      overflow-x: hidden;
      transition: background-color var(--ease-standard), color var(--ease-standard);
      position: relative;
    }

    /* Page shell */
    .page-shell {
      max-width: 1380px;
      margin: 0 auto;
      width: min(calc(100% - 32px), 1380px);
      padding: 0 0 52px;
    }

    /* Focus accessibility */
    a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible, textarea:focus-visible {
      outline: 4px solid var(--purple);
      outline-offset: 3px;
    }

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }

    /* Keyframes */
    @keyframes float {
      0%, 100% { transform: translateY(0) rotate(-1deg); }
      50% { transform: translateY(-12px) rotate(2deg); }
    }
    @keyframes pop {
      from { opacity: 0; transform: translateY(14px) scale(0.96); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    @keyframes pulseGlow {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.08); }
    }
    @keyframes shimmer {
      to { background-position: -220% 0; }
    }
    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes slideIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================================================
       BUTTON & CONTROL SYSTEM
       ========================================================================== */
    .cta-button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: var(--lime);
      color: var(--black);
      border: 4px solid var(--black);
      border-radius: 9px;
      box-shadow: 5px 5px 0 var(--black);
      padding: 12px 24px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      text-decoration: none;
      transition: transform var(--ease-fast), box-shadow var(--ease-fast), background var(--ease-fast);
      user-select: none;
    }
    .cta-button:hover {
      transform: translate(-2px, -2px);
      box-shadow: 8px 8px 0 var(--black);
    }
    .cta-button:active {
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0 var(--black);
    }

    .ghost-button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: var(--white);
      color: var(--black);
      border: 4px solid var(--black);
      border-radius: 9px;
      box-shadow: 5px 5px 0 var(--black);
      padding: 12px 22px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      text-decoration: none;
      transition: transform var(--ease-fast), box-shadow var(--ease-fast), background var(--ease-fast);
      user-select: none;
    }
    .ghost-button:hover {
      transform: translate(-2px, -2px);
      box-shadow: 8px 8px 0 var(--black);
      background: var(--gray);
    }
    .ghost-button:active {
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0 var(--black);
    }

    .touch-button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--lime);
      color: var(--black);
      border: 3px solid var(--black);
      border-radius: 8px;
      box-shadow: 4px 4px 0 var(--black);
      padding: 10px 18px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 0.9rem;
      text-decoration: none;
      cursor: pointer;
      transition: transform var(--ease-fast), box-shadow var(--ease-fast);
    }
    .touch-button:hover {
      transform: translate(-2px, -2px);
      box-shadow: 6px 6px 0 var(--black);
    }
    .touch-button:active {
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0 var(--black);
    }

    .theme-toggle {
      background: var(--pink);
      color: var(--black);
      border: 4px solid var(--black);
      border-radius: 9px;
      box-shadow: 5px 5px 0 var(--black);
      width: 48px;
      height: 44px;
      font-weight: 700;
      font-family: var(--font-main);
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform var(--ease-fast), box-shadow var(--ease-fast);
    }
    .theme-toggle:hover {
      transform: translate(-2px, -2px);
      box-shadow: 7px 7px 0 var(--black);
    }
    .theme-toggle:active {
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0 var(--black);
    }

    .tech-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 10px;
      border: 2px solid var(--black);
      border-radius: 5px;
      background: var(--gray);
      color: var(--black);
      font-family: var(--font-main);
      font-size: 0.78rem;
      font-weight: 700;
      box-shadow: 2px 2px 0 var(--black);
    }

    .badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border: 3px solid var(--black);
      border-radius: 999px;
      background: var(--white);
      color: var(--black);
      font-weight: 700;
      font-size: 0.82rem;
      box-shadow: 3px 3px 0 var(--black);
    }

    /* Cards */
    .card {
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: clamp(20px, 2.8vw, 34px);
      transition: transform var(--ease-standard), box-shadow var(--ease-standard), border-color var(--ease-standard);
      position: relative;
    }
    .card:hover {
      transform: translateY(-8px) rotate(-0.6deg);
      box-shadow: 15px 15px 0 var(--black);
      border-color: var(--purple);
    }

    /* ==========================================================================
       NAVBAR COMPONENT
       ========================================================================== */
    .navbar-container {
      position: sticky;
      top: 18px;
      z-index: 100;
      margin-bottom: 36px;
    }

    .navbar {
      width: min(calc(100% - 32px), 1380px);
      margin: 0 auto;
      height: 76px;
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      transition: background var(--ease-standard);
    }

    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--black);
    }

    .brand-logo {
      width: 44px;
      height: 44px;
      background: var(--lime);
      border: 3px solid var(--black);
      border-radius: 8px;
      box-shadow: 3px 3px 0 var(--black);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 1.4rem;
      letter-spacing: -1px;
    }

    .brand-name {
      font-size: 1.7rem;
      font-weight: 700;
      letter-spacing: -1px;
      line-height: 1;
    }

    .brand-tag {
      font-size: 0.68rem;
      background: var(--purple);
      color: var(--black);
      padding: 2px 6px;
      border: 2px solid var(--black);
      border-radius: 4px;
      font-weight: 700;
      text-transform: uppercase;
      box-shadow: 2px 2px 0 var(--black);
    }

    .menu-bar {
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--gray);
      border: 4px solid var(--black);
      border-radius: 9px;
      padding: 4px 6px;
      box-shadow: 5px 5px 0 var(--black);
    }

    .nav-link {
      padding: 8px 14px;
      font-weight: 700;
      font-size: 0.88rem;
      color: var(--black);
      text-decoration: none;
      border-radius: 6px;
      border: 2px solid transparent;
      transition: background var(--ease-fast), border-color var(--ease-fast), transform var(--ease-fast);
      cursor: pointer;
      white-space: nowrap;
    }
    .nav-link:hover {
      background: var(--white);
      border-color: var(--black);
      transform: translateY(-2px);
    }
    .nav-link.active {
      background: var(--lime);
      border-color: var(--black);
      box-shadow: 2px 2px 0 var(--black);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .mobile-menu-btn {
      display: none;
      background: var(--lime);
      border: 3px solid var(--black);
      border-radius: 8px;
      width: 44px;
      height: 44px;
      box-shadow: 4px 4px 0 var(--black);
      cursor: pointer;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 5px;
    }
    .mobile-menu-btn span {
      display: block;
      width: 22px;
      height: 3px;
      background: var(--black);
    }

    /* Mobile Drawer */
    .mobile-drawer {
      display: none;
      position: fixed;
      top: 96px;
      left: 16px;
      right: 16px;
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 20px;
      z-index: 99;
      flex-direction: column;
      gap: 12px;
      animation: pop 190ms ease both;
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer .nav-link {
      padding: 12px;
      font-size: 1.1rem;
      border: 3px solid var(--black);
    }

    /* ==========================================================================
       VIEW CONTAINER & PAGE ROUTING
       ========================================================================== */
    .view-section {
      display: none;
      animation: pop 220ms ease both;
    }
    .view-section.active-view {
      display: block;
    }

    .section-header {
      margin-bottom: 28px;
    }
    .section-eyebrow {
      display: inline-block;
      background: var(--lime);
      color: var(--black);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border: 3px solid var(--black);
      border-radius: 6px;
      box-shadow: 3px 3px 0 var(--black);
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .section-title {
      font-size: clamp(2rem, 5vw, 3.4rem);
      font-weight: 700;
      line-height: 1.05;
      letter-spacing: -1.5px;
      margin-bottom: 10px;
    }
    .section-subtitle {
      font-size: 1.15rem;
      max-width: 720px;
      font-weight: 500;
      opacity: 0.9;
    }

    /* ==========================================================================
       PAGE 1: HERO / LANDING
       ========================================================================== */
    .hero-grid {
      display: grid;
      grid-template-columns: 1.25fr 0.95fr;
      gap: 28px;
      margin-bottom: 36px;
    }

    .hero-card {
      background: var(--purple);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: clamp(24px, 3.5vw, 42px);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 540px;
      position: relative;
      overflow: hidden;
    }
    .hero-card::after {
      content: "";
      position: absolute;
      right: -40px;
      bottom: -40px;
      width: 220px;
      height: 220px;
      background: radial-gradient(circle, rgba(221, 242, 71, 0.45) 0%, transparent 70%);
      pointer-events: none;
    }

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--black);
      color: var(--white);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      width: fit-content;
      box-shadow: 3px 3px 0 var(--lime);
      margin-bottom: 20px;
    }
    .pulse-dot {
      width: 10px;
      height: 10px;
      background: var(--lime);
      border-radius: 50%;
      animation: pulseGlow 1.5s infinite;
    }

    .hero-headline {
      font-size: clamp(3.8rem, 11vw, 7.8rem);
      font-weight: 700;
      line-height: 0.82;
      letter-spacing: -3.5px;
      margin-bottom: 16px;
      color: var(--black);
      text-transform: uppercase;
    }

    .hero-tagline {
      font-size: clamp(1.2rem, 2.4vw, 1.8rem);
      font-weight: 700;
      margin-bottom: 14px;
      display: inline-block;
      background: var(--white);
      padding: 4px 14px;
      border: 3px solid var(--black);
      border-radius: 8px;
      box-shadow: 4px 4px 0 var(--black);
    }

    .hero-desc {
      font-size: 1.05rem;
      font-weight: 500;
      max-width: 580px;
      margin-bottom: 26px;
      line-height: 1.5;
    }

    .metric-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-bottom: 28px;
    }

    .metric-box {
      border: 4px solid var(--black);
      border-radius: 10px;
      box-shadow: 5px 5px 0 var(--black);
      padding: 14px 12px;
      text-align: center;
      transition: transform var(--ease-fast);
    }
    .metric-box:hover {
      transform: translateY(-4px);
    }
    .metric-box.box-lime { background: var(--lime); }
    .metric-box.box-pink { background: var(--pink); }
    .metric-box.box-white { background: var(--white); }

    .metric-val {
      font-size: clamp(1.4rem, 2.6vw, 1.9rem);
      font-weight: 700;
      line-height: 1.1;
      display: block;
    }
    .metric-label {
      font-size: 0.76rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-top: 4px;
      display: block;
    }

    .hero-buttons {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
    }

    /* Live Demo Upload Hero Card */
    .live-demo-card {
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: clamp(24px, 3.2vw, 36px);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .demo-card-head {
      margin-bottom: 18px;
    }
    .demo-card-title {
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }
    .demo-card-desc {
      font-size: 0.92rem;
      font-weight: 500;
      opacity: 0.85;
    }

    /* Upload Zone */
    .upload-zone {
      border: 3px dashed var(--black);
      border-radius: 10px;
      padding: 34px 20px;
      text-align: center;
      cursor: pointer;
      background: var(--gray);
      transition: background var(--ease-standard), border-color var(--ease-standard), transform var(--ease-fast);
      position: relative;
      margin-bottom: 18px;
      box-shadow: inset 2px 2px 0 rgba(0,0,0,0.05);
    }
    .upload-zone:hover,
    .upload-zone.dragover {
      background: var(--lime);
      border-color: var(--black);
      transform: scale(1.01);
    }
    .upload-zone.processing {
      background: var(--cyan);
    }

    .upload-icon {
      width: 48px;
      height: 48px;
      margin: 0 auto 10px;
      color: var(--black);
    }
    .upload-zone h4 {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 4px;
    }
    .upload-zone p {
      font-size: 0.84rem;
      opacity: 0.8;
      margin-bottom: 10px;
    }
    .upload-zone-hint {
      display: inline-block;
      background: var(--white);
      border: 2px solid var(--black);
      border-radius: 5px;
      padding: 3px 8px;
      font-size: 0.75rem;
      font-weight: 700;
    }

    .sample-section-label {
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .sample-pill-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin-bottom: 18px;
    }

    .sample-btn {
      background: var(--white);
      border: 3px solid var(--black);
      border-radius: 8px;
      padding: 10px 14px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 0.86rem;
      text-align: left;
      cursor: pointer;
      box-shadow: 3px 3px 0 var(--black);
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: transform var(--ease-fast), background var(--ease-fast), box-shadow var(--ease-fast);
    }
    .sample-btn:hover {
      background: var(--lime);
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0 var(--black);
    }
    .sample-btn.selected {
      background: var(--pink);
      border-color: var(--black);
    }
    .sample-tag {
      font-size: 0.72rem;
      background: var(--black);
      color: var(--white);
      padding: 2px 6px;
      border-radius: 4px;
    }

    /* Active Policy Quick Info Strip */
    .policy-active-strip {
      background: var(--neon-mint);
      border: 3px solid var(--black);
      border-radius: 8px;
      padding: 10px 14px;
      box-shadow: 4px 4px 0 var(--black);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.85rem;
      font-weight: 700;
    }

    /* 3 Overview Quick Cards below Hero */
    .highlight-cards {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 36px;
    }

    .highlight-card {
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 26px;
      text-decoration: none;
      color: var(--black);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 220px;
      transition: transform var(--ease-standard), box-shadow var(--ease-standard);
      cursor: pointer;
    }
    .highlight-card:hover {
      transform: translateY(-8px) rotate(-0.6deg);
      box-shadow: 15px 15px 0 var(--black);
    }
    .highlight-card.hl-lime { background: var(--lime); }
    .highlight-card.hl-cyan { background: var(--cyan); }
    .highlight-card.hl-white { background: var(--white); }

    .highlight-card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
    }
    .highlight-card-icon {
      width: 44px;
      height: 44px;
      background: var(--black);
      color: var(--white);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 3px 3px 0 var(--white);
    }
    .hl-white .highlight-card-icon {
      box-shadow: 3px 3px 0 var(--purple);
    }
    .highlight-card h3 {
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 8px;
    }
    .highlight-card p {
      font-size: 0.94rem;
      font-weight: 500;
      line-height: 1.4;
      margin-bottom: 16px;
    }

    /* Live Chat Demo Box on Landing Page */
    .landing-chat-box {
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: clamp(24px, 3.5vw, 38px);
      margin-bottom: 36px;
    }
    .chat-box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 22px;
      padding-bottom: 16px;
      border-bottom: 3px solid var(--black);
    }
    .chat-box-title {
      font-size: 1.5rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* Insurer logos ticker */
    .insurers-ticker {
      background: var(--black);
      color: var(--white);
      border: 4px solid var(--black);
      border-radius: 10px;
      box-shadow: 6px 6px 0 var(--lime);
      padding: 14px 20px;
      display: flex;
      align-items: center;
      gap: 20px;
      overflow-x: auto;
      margin-bottom: 36px;
      scrollbar-width: none;
    }
    .insurers-ticker::-webkit-scrollbar { display: none; }
    .ticker-label {
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--lime);
      white-space: nowrap;
    }
    .ticker-items {
      display: flex;
      gap: 14px;
      align-items: center;
      white-space: nowrap;
    }
    .ticker-pill {
      background: #222;
      border: 2px solid #444;
      border-radius: 6px;
      padding: 4px 12px;
      font-size: 0.84rem;
      font-weight: 600;
    }

    /* ==========================================================================
       CHAT INTERFACE STYLES (Used on Hero & Demo)
       ========================================================================== */
    .chat-container {
      display: flex;
      flex-direction: column;
      gap: 18px;
      padding: 22px;
      background: var(--gray);
      border: 4px solid var(--black);
      border-radius: 10px;
      box-shadow: 5px 5px 0 var(--black);
      min-height: 420px;
      max-height: 600px;
      overflow-y: auto;
      margin-bottom: 16px;
    }

    .chat-message {
      max-width: 86%;
      padding: 16px 20px;
      border: 3px solid var(--black);
      border-radius: 10px;
      box-shadow: 4px 4px 0 var(--black);
      animation: slideIn 180ms ease;
    }
    .chat-message.user {
      background: var(--lime);
      align-self: flex-end;
      margin-left: auto;
      font-weight: 600;
      color: var(--black);
    }
    .chat-message.assistant {
      background: var(--white);
      align-self: flex-start;
      color: var(--black);
    }

    .message-text {
      font-size: 0.98rem;
      line-height: 1.5;
      margin-bottom: 12px;
    }

    /* Evidence citations */
    .evidence-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin: 12px 0;
    }
    .evidence-citation {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 14px;
      background: var(--white);
      border: 3px solid var(--black);
      border-radius: 8px;
      box-shadow: 3px 3px 0 var(--black);
      font-size: 0.88rem;
      cursor: pointer;
      transition: transform var(--ease-fast), background var(--ease-fast);
    }
    .evidence-citation:hover {
      background: var(--neon-mint);
      transform: translateX(4px);
    }
    .source-badge {
      background: var(--purple);
      color: var(--black);
      padding: 4px 10px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.78rem;
      white-space: nowrap;
      border: 2px solid var(--black);
      box-shadow: 2px 2px 0 var(--black);
    }

    /* Cost Breakdown Table */
    .cost-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      border: 4px solid var(--black);
      border-radius: 10px;
      overflow: hidden;
      margin: 14px 0;
      box-shadow: 4px 4px 0 var(--black);
      font-size: 0.92rem;
    }
    .cost-table th {
      background: var(--lime);
      font-weight: 700;
      padding: 12px 16px;
      text-align: left;
      border-bottom: 3px solid var(--black);
      border-right: 3px solid var(--black);
      color: var(--black);
    }
    .cost-table th:last-child {
      border-right: none;
    }
    .cost-table td {
      padding: 10px 16px;
      border-bottom: 2px solid var(--grid-line);
      border-right: 2px solid var(--grid-line);
    }
    .cost-table td:last-child {
      border-right: none;
      text-align: right;
      font-weight: 600;
    }
    .cost-table tr:nth-child(even) td {
      background: var(--gray);
    }
    .cost-table tr:hover td {
      background: var(--pink);
      color: var(--black);
    }
    .cost-table tr.total-row td {
      background: var(--neon-mint);
      color: var(--black);
      font-weight: 700;
      font-size: 1rem;
      border-top: 3px solid var(--black);
      border-bottom: none;
    }

    /* Confidence Badge */
    .confidence-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border: 3px solid var(--black);
      border-radius: 8px;
      box-shadow: 4px 4px 0 var(--black);
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--black);
      margin-top: 10px;
    }
    .confidence-badge.high { background: var(--neon-mint); }
    .confidence-badge.medium { background: var(--neon-orange); }
    .confidence-badge.low { background: var(--pink); }
    .confidence-badge.insufficient { background: var(--gray); }

    .missing-info-box {
      margin-top: 12px;
      padding: 12px 14px;
      background: var(--bg);
      border: 3px solid var(--black);
      border-radius: 8px;
      font-size: 0.86rem;
      box-shadow: 3px 3px 0 var(--black);
    }
    .missing-info-box ul {
      margin-left: 20px;
      margin-top: 6px;
    }

    /* Chat Input Bar */
    .chat-input-bar {
      display: flex;
      gap: 12px;
    }
    .chat-input {
      flex: 1;
      padding: 14px 18px;
      border: 3px solid var(--black);
      border-radius: 9px;
      font-family: var(--font-main);
      font-size: 1rem;
      font-weight: 500;
      background: var(--white);
      color: var(--black);
      box-shadow: 4px 4px 0 var(--black);
    }
    .chat-input:focus {
      outline: none;
      border-color: var(--purple);
    }
    .chat-send-btn {
      background: var(--lime);
      color: var(--black);
      border: 3px solid var(--black);
      border-radius: 9px;
      box-shadow: 4px 4px 0 var(--black);
      padding: 0 24px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: transform var(--ease-fast), box-shadow var(--ease-fast);
    }
    .chat-send-btn:hover {
      transform: translate(-2px, -2px);
      box-shadow: 6px 6px 0 var(--black);
    }
    .chat-send-btn:active {
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0 var(--black);
    }

    .chat-quick-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }
    .chat-chip {
      background: var(--white);
      border: 2px solid var(--black);
      border-radius: 6px;
      padding: 5px 12px;
      font-family: var(--font-main);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 2px 2px 0 var(--black);
      transition: background var(--ease-fast), transform var(--ease-fast);
    }
    .chat-chip:hover {
      background: var(--lime);
      transform: translateY(-2px);
    }

    /* Typing indicator */
    .typing-indicator {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 10px 16px;
      background: var(--white);
      border: 3px solid var(--black);
      border-radius: 8px;
      box-shadow: 3px 3px 0 var(--black);
    }
    .typing-dot {
      width: 8px;
      height: 8px;
      background: var(--black);
      border-radius: 50%;
      animation: pulseGlow 0.9s infinite alternate;
    }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }

    /* ==========================================================================
       PAGE 2: HOW IT WORKS
       ========================================================================== */
    .pipeline-wrapper {
      position: relative;
      max-width: 960px;
      margin: 0 auto;
    }

    .pipeline-step {
      position: relative;
      margin-bottom: 28px;
      padding-left: 70px;
    }

    .step-badge {
      position: absolute;
      left: 0;
      top: 0;
      width: 52px;
      height: 52px;
      background: var(--black);
      color: var(--white);
      border: 4px solid var(--white);
      border-radius: 50%;
      box-shadow: 5px 5px 0 var(--black);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 1.4rem;
      z-index: 2;
    }

    .step-connector {
      position: absolute;
      left: 24px;
      top: 52px;
      bottom: -32px;
      width: 4px;
      border-left: 4px dashed var(--black);
      z-index: 1;
    }
    .pipeline-step:last-child .step-connector {
      display: none;
    }

    .step-card {
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 24px 28px;
      transition: transform var(--ease-standard), box-shadow var(--ease-standard);
    }
    .step-card:hover {
      transform: translateY(-6px) rotate(-0.5deg);
      box-shadow: 15px 15px 0 var(--black);
    }

    .step-1 { background: var(--lime); }
    .step-2 { background: var(--cyan); }
    .step-3 { background: var(--purple); }
    .step-4 { background: var(--pink); }
    .step-5 { background: var(--electric-blue); }
    .step-6 { background: var(--neon-orange); }
    .step-7 { background: var(--neon-mint); }

    .step-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .step-title {
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .step-icon {
      width: 28px;
      height: 28px;
    }
    .step-desc {
      font-size: 1rem;
      font-weight: 500;
      margin-bottom: 12px;
      line-height: 1.4;
    }
    .step-pill-list {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    /* ==========================================================================
       PAGE 3: FEATURES
       ========================================================================== */
    .features-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
      margin-bottom: 40px;
    }

    .feature-card {
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 32px 28px;
      transition: transform var(--ease-standard), box-shadow var(--ease-standard), border-color var(--ease-standard);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 290px;
    }
    .feature-card:hover {
      transform: translateY(-8px) rotate(-0.6deg);
      box-shadow: 15px 15px 0 var(--black);
      border-color: var(--purple);
    }

    .fc-lime { background: var(--lime); }
    .fc-white { background: var(--white); }
    .fc-cyan { background: var(--cyan); }
    .fc-pink { background: var(--pink); }
    .fc-orange { background: var(--neon-orange); }
    .fc-mint { background: var(--neon-mint); }

    .feature-icon-box {
      width: 56px;
      height: 56px;
      background: var(--black);
      color: var(--white);
      border: 3px solid var(--white);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 4px 4px 0 var(--black);
      margin-bottom: 18px;
    }
    .fc-white .feature-icon-box {
      border-color: var(--black);
    }
    .feature-title {
      font-size: 1.6rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 10px;
    }
    .feature-desc {
      font-size: 1rem;
      font-weight: 500;
      line-height: 1.45;
      margin-bottom: 20px;
    }
    .feature-pills {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: auto;
    }

    /* ==========================================================================
       PAGE 4: TRY IT / DEMO
       ========================================================================== */
    .demo-workspace {
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 28px;
      align-items: start;
    }

    .demo-sidebar {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .sidebar-panel {
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 8px 8px 0 var(--black);
      padding: 20px;
    }

    .sidebar-title {
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .policy-spec-table {
      width: 100%;
      font-size: 0.84rem;
      border-collapse: collapse;
    }
    .policy-spec-table tr {
      border-bottom: 1px solid var(--grid-line);
    }
    .policy-spec-table td {
      padding: 7px 0;
    }
    .policy-spec-table td:first-child {
      font-weight: 700;
      color: var(--black);
      opacity: 0.8;
    }
    .policy-spec-table td:last-child {
      text-align: right;
      font-weight: 600;
    }

    .demo-main-panel {
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    /* Demo Tabs */
    .demo-tabs {
      display: flex;
      gap: 12px;
    }
    .demo-tab-btn {
      background: var(--white);
      border: 4px solid var(--black);
      border-radius: 9px;
      box-shadow: 5px 5px 0 var(--black);
      padding: 12px 20px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: background var(--ease-fast), transform var(--ease-fast);
    }
    .demo-tab-btn:hover {
      background: var(--gray);
      transform: translateY(-2px);
    }
    .demo-tab-btn.active {
      background: var(--lime);
      box-shadow: 5px 5px 0 var(--black);
    }

    /* Treatment Simulator Form */
    .treatment-calc-card {
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 28px;
    }

    .calc-form-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
      margin-bottom: 22px;
    }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .form-group label {
      font-size: 0.88rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .form-control, .treatment-select {
      width: 100%;
      padding: 12px 14px;
      border: 3px solid var(--black);
      border-radius: 8px;
      background: var(--white);
      color: var(--black);
      font-family: var(--font-main);
      font-weight: 600;
      font-size: 0.95rem;
      box-shadow: 3px 3px 0 var(--black);
    }
    .form-control:focus, .treatment-select:focus {
      outline: none;
      border-color: var(--purple);
    }

    .calc-result-box {
      background: var(--bg);
      border: 4px solid var(--black);
      border-radius: 10px;
      box-shadow: 6px 6px 0 var(--black);
      padding: 20px;
      margin-top: 20px;
      animation: pop 180ms ease;
    }

    .calc-summary-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-bottom: 16px;
    }
    .calc-stat {
      background: var(--white);
      border: 3px solid var(--black);
      border-radius: 8px;
      padding: 12px;
      text-align: center;
      box-shadow: 3px 3px 0 var(--black);
    }
    .calc-stat.stat-lime { background: var(--lime); }
    .calc-stat.stat-mint { background: var(--neon-mint); }
    .calc-stat.stat-orange { background: var(--neon-orange); }

    /* ==========================================================================
       PAGE 5: PRICING / PLANS
       ========================================================================== */
    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      align-items: stretch;
      margin-bottom: 40px;
    }

    .pricing-card {
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 34px 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform var(--ease-standard), box-shadow var(--ease-standard);
      position: relative;
    }
    .pricing-card:hover {
      transform: translateY(-8px) rotate(-0.6deg);
      box-shadow: 15px 15px 0 var(--black);
    }

    .pricing-card.plan-free { background: var(--white); }
    .pricing-card.plan-pro { 
      background: var(--lime); 
      transform: scale(1.02);
      z-index: 2;
    }
    .pricing-card.plan-pro:hover {
      transform: scale(1.02) translateY(-8px) rotate(-0.6deg);
    }
    .pricing-card.plan-enterprise { background: var(--purple); }

    .popular-ribbon {
      position: absolute;
      top: -16px;
      right: 24px;
      background: var(--black);
      color: var(--lime);
      border: 3px solid var(--black);
      border-radius: 6px;
      padding: 4px 12px;
      font-weight: 700;
      font-size: 0.8rem;
      letter-spacing: 0.5px;
      box-shadow: 3px 3px 0 var(--white);
    }

    .plan-header {
      margin-bottom: 22px;
    }
    .plan-name {
      font-size: 1.8rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 8px;
    }
    .plan-price {
      display: flex;
      align-items: baseline;
      gap: 6px;
      margin-bottom: 6px;
    }
    .price-amount {
      font-size: 3rem;
      font-weight: 700;
      line-height: 1;
    }
    .price-period {
      font-size: 0.95rem;
      font-weight: 600;
      opacity: 0.8;
    }
    .plan-desc {
      font-size: 0.92rem;
      font-weight: 500;
      opacity: 0.9;
    }

    .plan-features {
      list-style: none;
      margin: 24px 0 32px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .plan-feature-item {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
      font-weight: 600;
    }
    .check-icon {
      width: 20px;
      height: 20px;
      flex-shrink: 0;
    }

    /* Billing toggle */
    .billing-toggle-wrap {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-bottom: 36px;
    }
    .billing-pill {
      background: var(--white);
      border: 3px solid var(--black);
      border-radius: 999px;
      padding: 6px 16px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 3px 3px 0 var(--black);
      transition: background var(--ease-fast);
    }
    .billing-pill.active {
      background: var(--lime);
    }

    /* ==========================================================================
       PAGE 6: FAQ
       ========================================================================== */
    .faq-list {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .accordion-item {
      border: 4px solid var(--black);
      border-radius: 10px;
      box-shadow: 5px 5px 0 var(--black);
      background: var(--white);
      overflow: hidden;
      transition: transform var(--ease-fast), background var(--ease-standard);
    }
    .accordion-item.open {
      background: var(--lime);
    }

    .accordion-toggle {
      width: 100%;
      padding: 18px 24px;
      font-family: var(--font-main);
      font-weight: 700;
      font-size: 1.15rem;
      text-align: left;
      background: transparent;
      border: none;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
      color: var(--black);
    }

    .accordion-icon {
      font-size: 1.8rem;
      font-weight: 700;
      line-height: 1;
      width: 32px;
      height: 32px;
      background: var(--black);
      color: var(--white);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .accordion-item.open .accordion-icon {
      background: var(--white);
      color: var(--black);
      border: 2px solid var(--black);
    }

    .accordion-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 300ms ease;
      background: var(--white);
      color: var(--black);
    }
    .accordion-body-inner {
      padding: 0 24px 22px;
      font-size: 1rem;
      line-height: 1.55;
      font-weight: 500;
    }

    /* ==========================================================================
       PAGE 7: CONTACT
       ========================================================================== */
    .contact-grid {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 32px;
    }

    .contact-form-card {
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 10px 10px 0 var(--black);
      padding: 34px;
    }

    .contact-banner {
      background: var(--black);
      color: var(--white);
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 24px;
      font-size: 1.25rem;
      font-weight: 700;
    }

    .contact-info-card {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .info-box {
      background: var(--purple);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 8px 8px 0 var(--black);
      padding: 24px;
    }

    .social-badge-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }

    .social-badge-btn {
      background: var(--white);
      border: 3px solid var(--black);
      border-radius: 10px;
      box-shadow: 4px 4px 0 var(--black);
      padding: 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--black);
      font-weight: 700;
      font-size: 0.92rem;
      transition: transform var(--ease-fast), box-shadow var(--ease-fast), background var(--ease-fast);
    }
    .social-badge-btn:hover {
      background: var(--lime);
      transform: translate(-2px, -2px);
      box-shadow: 6px 6px 0 var(--black);
    }

    .mono-circle {
      width: 38px;
      height: 38px;
      background: var(--black);
      color: var(--white);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.85rem;
    }

    /* ==========================================================================
       FOOTER COMPONENT
       ========================================================================== */
    .site-footer {
      margin-top: 72px;
      border-top: 5px solid var(--black);
      padding-top: 48px;
      background: transparent;
    }

    .footer-top {
      display: grid;
      grid-template-columns: 1.4fr repeat(3, 1fr);
      gap: 36px;
      margin-bottom: 40px;
    }

    .footer-brand h2 {
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: -1px;
      margin-bottom: 8px;
    }
    .footer-brand p {
      font-size: 0.95rem;
      opacity: 0.85;
      max-width: 340px;
      margin-bottom: 18px;
    }

    .footer-col h4 {
      font-size: 1rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 14px;
      border-bottom: 3px solid var(--black);
      padding-bottom: 6px;
      display: inline-block;
    }

    .footer-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .footer-link {
      color: var(--black);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.92rem;
      transition: color var(--ease-fast), transform var(--ease-fast);
      display: inline-block;
      cursor: pointer;
    }
    .footer-link:hover {
      text-decoration: underline;
      transform: translateX(4px);
    }

    .footer-bottom {
      border: 4px solid var(--black);
      border-radius: 10px;
      background: var(--white);
      box-shadow: 6px 6px 0 var(--black);
      padding: 18px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.88rem;
      font-weight: 600;
    }

    .disclaimer-box {
      background: var(--neon-orange);
      border: 3px solid var(--black);
      border-radius: 8px;
      padding: 12px 18px;
      font-size: 0.82rem;
      font-weight: 600;
      margin-bottom: 24px;
      box-shadow: 4px 4px 0 var(--black);
    }

    /* ==========================================================================
       MODAL SYSTEM
       ========================================================================== */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(17, 17, 17, 0.76);
      backdrop-filter: blur(2px);
    }
    .modal-backdrop.open {
      display: block;
    }

    .modal-panel {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 1001;
      background: var(--white);
      border: 5px solid var(--black);
      border-radius: 12px;
      box-shadow: 14px 14px 0 var(--lime);
      padding: clamp(20px, 3.2vw, 36px);
      animation: pop 190ms ease both;
      max-width: 680px;
      width: 90vw;
      max-height: 85vh;
      overflow-y: auto;
    }

    .modal-close {
      position: absolute;
      top: 14px;
      right: 14px;
      width: 42px;
      height: 42px;
      border: 4px solid var(--black);
      border-radius: 8px;
      background: var(--pink);
      box-shadow: 4px 4px 0 var(--black);
      font-size: 1.8rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      transition: transform var(--ease-fast);
    }
    .modal-close:hover {
      transform: scale(1.08);
    }

    /* Toast Notification */
    .toast-box {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      background: var(--lime);
      color: var(--black);
      border: 4px solid var(--black);
      border-radius: 9px;
      box-shadow: 6px 6px 0 var(--black);
      padding: 14px 22px;
      font-weight: 700;
      font-size: 0.95rem;
      display: flex;
      align-items: center;
      gap: 10px;
      animation: slideIn 200ms ease;
      transition: opacity 300ms ease, transform 300ms ease;
    }

    /* ==========================================================================
       RESPONSIVE BREAKPOINTS
       ========================================================================== */
    @media (max-width: 1199px) {
      .hero-grid {
        grid-template-columns: 1fr;
      }
      .demo-workspace {
        grid-template-columns: 1fr;
      }
      .features-grid {
        grid-template-columns: 1fr;
      }
      .pricing-grid {
        grid-template-columns: 1fr;
      }
      .pricing-card.plan-pro {
        transform: none;
      }
      .pricing-card.plan-pro:hover {
        transform: translateY(-8px) rotate(-0.6deg);
      }
      .contact-grid {
        grid-template-columns: 1fr;
      }
      .highlight-cards {
        grid-template-columns: 1fr;
      }
      .footer-top {
        grid-template-columns: 1fr 1fr;
      }
    }

    @media (max-width: 767px) {
      .navbar {
        height: 68px;
        padding: 0 14px;
      }
      .menu-bar, .nav-actions .touch-button {
        display: none;
      }
      .mobile-menu-btn {
        display: flex;
      }
      .metric-grid {
        grid-template-columns: 1fr;
      }
      .calc-form-grid {
        grid-template-columns: 1fr;
      }
      .calc-summary-row {
        grid-template-columns: 1fr;
      }
      .footer-top {
        grid-template-columns: 1fr;
      }
      .social-badge-grid {
        grid-template-columns: 1fr;
      }
      .pipeline-step {
        padding-left: 56px;
      }
      .step-badge {
        width: 42px;
        height: 42px;
        font-size: 1.1rem;
      }
      .step-connector {
        left: 20px;
      }
    }

    /* Print styles */
    @media print {
      .navbar-container, .theme-toggle, .mobile-menu-btn, .chat-input-bar, .chat-quick-chips, .cursor-trail-dot {
        display: none !important;
      }
      .card, .hero-card, .step-card {
        box-shadow: none !important;
        border: 2px solid #000 !important;
      }
      body {
        background: #fff !important;
        color: #000 !important;
      }
    }
  </style>
</head>
<body>

  <!-- Sticky Navbar -->
  <header class="navbar-container">
    <nav class="navbar" aria-label="Main Navigation">
      <a href="#home" class="brand-wrap" onclick="navigateTo('home')">
        <div class="brand-logo">IX</div>
        <div>
          <span class="brand-name">INSURIX</span>
        </div>
        <span class="brand-tag">v2.4 AI</span>
      </a>

      <div class="menu-bar" role="tablist">
        <a href="#home" class="nav-link active" data-view="home" onclick="navigateTo('home')">Home</a>
        <a href="#how-it-works" class="nav-link" data-view="how-it-works" onclick="navigateTo('how-it-works')">How It Works</a>
        <a href="#features" class="nav-link" data-view="features" onclick="navigateTo('features')">Features</a>
        <a href="#demo" class="nav-link" data-view="demo" onclick="navigateTo('demo')">Try It</a>
        <a href="#pricing" class="nav-link" data-view="pricing" onclick="navigateTo('pricing')">Pricing</a>
        <a href="#faq" class="nav-link" data-view="faq" onclick="navigateTo('faq')">FAQ</a>
        <a href="#contact" class="nav-link" data-view="contact" onclick="navigateTo('contact')">Contact</a>
      </div>

      <div class="nav-actions">
        <button class="theme-toggle" id="theme-btn" aria-label="Toggle light and dark theme" aria-pressed="false" title="Switch Theme">DK</button>
        <button class="mobile-menu-btn" id="mobile-toggle" aria-label="Toggle mobile menu">
          <span></span><span></span><span></span>
        </button>
        <a href="#demo" class="touch-button" onclick="navigateTo('demo')">Upload Now</a>
      </div>
    </nav>

    <!-- Mobile Drawer -->
    <div class="mobile-drawer" id="mobile-drawer">
      <a href="#home" class="nav-link active" onclick="navigateTo('home'); closeMobileMenu();">Home</a>
      <a href="#how-it-works" class="nav-link" onclick="navigateTo('how-it-works'); closeMobileMenu();">How It Works</a>
      <a href="#features" class="nav-link" onclick="navigateTo('features'); closeMobileMenu();">Features</a>
      <a href="#demo" class="nav-link" onclick="navigateTo('demo'); closeMobileMenu();">Try Interactive Demo</a>
      <a href="#pricing" class="nav-link" onclick="navigateTo('pricing'); closeMobileMenu();">Pricing & Plans</a>
      <a href="#faq" class="nav-link" onclick="navigateTo('faq'); closeMobileMenu();">FAQ</a>
      <a href="#contact" class="nav-link" onclick="navigateTo('contact'); closeMobileMenu();">Contact Us</a>
    </div>
  </header>

  <!-- Main Content Shell -->
  <main class="page-shell">

    <!-- ==========================================================================
         PAGE 1: HERO / LANDING VIEW
         ========================================================================== -->
    <section id="view-home" class="view-section active-view">
      
      <!-- Hero Top 2-Card Grid -->
      <div class="hero-grid">
        
        <!-- Left: Purple Hero Card -->
        <article class="hero-card">
          <div>
            <div class="hero-eyebrow">
              <span class="pulse-dot"></span>
              AI-POWERED INSURANCE INTELLIGENCE
            </div>
            <h1 class="hero-headline">INSURIX</h1>
            <div>
              <span class="hero-tagline">Policy confusion → Financial clarity</span>
            </div>
            <p class="hero-desc">
              Convert dense 60-page health policy wordings into unambiguous answers. 
              Get exact out-of-pocket costs, pre-existing waiting periods, and room rent cappings with verified clause citations.
            </p>

            <!-- 3 Metric Boxes -->
            <div class="metric-grid">
              <div class="metric-box box-lime">
                <span class="metric-val">50K+</span>
                <span class="metric-label">Policies Analyzed</span>
              </div>
              <div class="metric-box box-pink">
                <span class="metric-val">₹2.8Cr+</span>
                <span class="metric-label">Savings Estimated</span>
              </div>
              <div class="metric-box box-white">
                <span class="metric-val">99.2%</span>
                <span class="metric-label">Evidence Accuracy</span>
              </div>
            </div>
          </div>

          <div class="hero-buttons">
            <button class="cta-button" onclick="navigateTo('demo')">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="17 8 12 3 7 8"/>
                <line x1="12" y1="3" x2="12" y2="15"/>
              </svg>
              Upload Your Policy
            </button>
            <button class="ghost-button" onclick="navigateTo('how-it-works')">
              See How It Works →
            </button>
          </div>
        </article>

        <!-- Right: Live Demo Upload Card -->
        <article class="live-demo-card">
          <div class="demo-card-head">
            <h2 class="demo-card-title">Live Policy Parser</h2>
            <p class="demo-card-desc">Upload your insurance PDF or test with popular Indian insurer policies instantly.</p>
          </div>

          <!-- Drag and Drop Upload Zone -->
          <div class="upload-zone" id="hero-upload-zone" onclick="triggerFileInput('hero-file-input')">
            <input type="file" id="hero-file-input" style="display:none" accept="application/pdf" onchange="handleFileSelected(event)">
            <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
              <polyline points="17 8 12 3 7 8"/>
              <line x1="12" y1="3" x2="12" y2="15"/>
            </svg>
            <h3 style="font-size:1.15rem; font-weight:700; margin-bottom:4px;">Drop Policy PDF Here</h3>
            <p>Supports Star Health, HDFC ERGO, Care, Max Bupa & 50+ insurers</p>
            <span class="upload-zone-hint">PDF up to 25MB • Vision OCR Enabled</span>
          </div>

          <!-- Sample Policies List -->
          <div>
            <div class="sample-section-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              Or Try A Pre-loaded Sample Policy:
            </div>
            <div class="sample-pill-grid">
              <button class="sample-btn selected" onclick="loadSamplePolicy('star')">
                <span>⭐ Star Health Comprehensive (₹5L)</span>
                <span class="sample-tag">Loaded</span>
              </button>
              <button class="sample-btn" onclick="loadSamplePolicy('royal')">
                <span>🛡️ Royal Sundaram Lifeline Supreme (₹10L)</span>
                <span class="sample-tag">Load</span>
              </button>
              <button class="sample-btn" onclick="loadSamplePolicy('hdfc')">
                <span>⚡ HDFC ERGO Optima Restore (₹5L)</span>
                <span class="sample-tag">Load</span>
              </button>
            </div>
          </div>

          <!-- Active Policy Status Strip -->
          <div class="policy-active-strip" id="hero-active-strip">
            <span>Active: <strong>Star Comprehensive (5L)</strong></span>
            <span>Waiting: 36m PED • Room: 1% SI</span>
          </div>
        </article>

      </div>

      <!-- Insurer Ticker -->
      <div class="insurers-ticker">
        <span class="ticker-label">Supported Insurers:</span>
        <div class="ticker-items">
          <span class="ticker-pill">Star Health</span>
          <span class="ticker-pill">HDFC ERGO</span>
          <span class="ticker-pill">Care Health</span>
          <span class="ticker-pill">ICICI Lombard</span>
          <span class="ticker-pill">Niva Bupa</span>
          <span class="ticker-pill">Tata AIG</span>
          <span class="ticker-pill">Bajaj Allianz</span>
          <span class="ticker-pill">National Insurance</span>
          <span class="ticker-pill">New India Assurance</span>
        </div>
      </div>

      <!-- 3 Quick Highlight Cards -->
      <div class="highlight-cards">
        
        <div class="highlight-card hl-lime" onclick="navigateTo('how-it-works')">
          <div class="highlight-card-top">
            <span class="tech-pill">01 / WORKFLOW</span>
            <div class="highlight-card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            </div>
          </div>
          <div>
            <h3>7-Step Pipeline</h3>
            <p>From visual PDF OCR parsing to deterministic IRDAI rule cross-referencing and financial math.</p>
          </div>
          <span style="font-weight:700; text-decoration:underline;">Explore Engine Architecture →</span>
        </div>

        <div class="highlight-card hl-cyan" onclick="navigateTo('features')">
          <div class="highlight-card-top">
            <span class="tech-pill">02 / CAPABILITIES</span>
            <div class="highlight-card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
          </div>
          <div>
            <h3>Evidence Citations</h3>
            <p>Every answer quotes the exact policy page, clause section number, and applies strict uncertainty flags.</p>
          </div>
          <span style="font-weight:700; text-decoration:underline;">View All 6 Core Features →</span>
        </div>

        <div class="highlight-card hl-white" onclick="navigateTo('demo')">
          <div class="highlight-card-top">
            <span class="tech-pill">03 / TRUST</span>
            <div class="highlight-card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
          </div>
          <div>
            <h3>IRDAI Aligned</h3>
            <p>Strictly compliant with Indian health insurance master circulars on proportionate deduction & exclusions.</p>
          </div>
          <span style="font-weight:700; text-decoration:underline;">Test Interactive Simulator →</span>
        </div>

      </div>

      <!-- Live Chat Demo Preview Section -->
      <div class="landing-chat-box">
        <div class="chat-box-header">
          <div class="chat-box-title">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            Live Policy Intelligence Simulation
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <span class="badge-pill" id="landing-loaded-policy-badge">Policy: Star Comprehensive (5L)</span>
            <button class="touch-button" onclick="navigateTo('demo')" style="padding:6px 12px; font-size:0.82rem;">Open Full Workspace ↗</button>
          </div>
        </div>

        <!-- Chat Container -->
        <div class="chat-container" id="landing-chat-container">
          
          <!-- Sample User Msg -->
          <div class="chat-message user">
            Is knee replacement surgery covered under my policy? What will I pay out-of-pocket?
          </div>

          <!-- Sample Assistant Msg -->
          <div class="chat-message assistant">
            <div class="message-text">
              <strong>Yes, Total Knee Replacement is covered</strong> under your Star Comprehensive policy as a medically necessary surgical procedure, subject to specific waiting periods and deductible thresholds.
            </div>

            <div class="evidence-list">
              <div class="evidence-citation" onclick="openClauseModal('Section 4.2', 18, 'Knee replacement surgery is covered as a medically necessary procedure under Section 4.2 of the policy wording.')">
                <span class="source-badge">Page 18, §4.2</span>
                <span>"Knee replacement surgery is covered as a medically necessary procedure under Section 4.2 of the policy."</span>
              </div>
              <div class="evidence-citation" onclick="openClauseModal('Section 5.1', 12, 'Waiting period of 36 months applies for pre-existing conditions and their direct complications.')">
                <span class="source-badge">Page 12, §5.1</span>
                <span>"Waiting period of 36 months applies for pre-existing conditions and their direct complications."</span>
              </div>
            </div>

            <!-- Cost Table -->
            <table class="cost-table">
              <thead>
                <tr>
                  <th>Financial Item</th>
                  <th>Amount</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>Total Treatment Cost</td><td>₹2,80,000</td></tr>
                <tr><td>Potentially Covered by Insurer</td><td>₹2,10,000</td></tr>
                <tr><td>Base Deductible Applied</td><td>₹20,000</td></tr>
                <tr><td>Co-payment (10% senior copay if 60+)</td><td>₹21,000</td></tr>
                <tr class="total-row"><td><strong>Estimated Out-of-Pocket Expense</strong></td><td><strong>₹70,000</strong></td></tr>
              </tbody>
            </table>

            <!-- Confidence Badge -->
            <div>
              <div class="confidence-badge medium">
                <span>⚠</span> Medium Confidence
              </div>
            </div>

            <div class="missing-info-box">
              <strong>Uncertainty & Ambiguity Warnings:</strong>
              <ul>
                <li>Exact hospital category (Network cashless vs Non-network reimbursement) not specified.</li>
                <li>Waiting period completion status is unknown (policy active &gt; 36 months required for pre-existing arthritis).</li>
                <li><strong>Recommendation:</strong> Verify waiting period completed and select in-network facility to avoid 15% customary deduction.</li>
              </ul>
            </div>
          </div>

        </div>

        <!-- Quick Question Chips -->
        <div class="chat-quick-chips">
          <span style="font-size:0.8rem; font-weight:700; align-self:center;">Try Asking:</span>
          <button class="chat-chip" onclick="askPresetQuestion('landing', 'What is my room rent limit and ICU capping?')">Room rent & ICU limits?</button>
          <button class="chat-chip" onclick="askPresetQuestion('landing', 'How much will I pay out-of-pocket for Cataract surgery?')">Cataract surgery out-of-pocket?</button>
          <button class="chat-chip" onclick="askPresetQuestion('landing', 'What pre-existing disease waiting period applies?')">Pre-existing waiting periods?</button>
          <button class="chat-chip" onclick="askPresetQuestion('landing', 'Does my policy have co-payment for senior citizens?')">Senior citizen co-pay?</button>
        </div>

        <!-- Input Bar -->
        <div class="chat-input-bar" style="margin-top:14px;">
          <input type="text" id="landing-chat-input" class="chat-input" placeholder="Ask any question about your policy (e.g. 'Is robotic knee surgery covered?')">
          <button class="chat-send-btn" onclick="sendChatQuery('landing')">
            <span>Send</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          </button>
        </div>

      </div>

    </section>

    <!-- ==========================================================================
         PAGE 2: HOW IT WORKS VIEW
         ========================================================================== -->
    <section id="view-how-it-works" class="view-section">
      <div class="section-header">
        <span class="section-eyebrow">Architecture & Logic</span>
        <h2 class="section-title">HOW IT WORKS: 7-STEP REASONING ENGINE</h2>
        <p class="section-subtitle">
          How Insurix processes dense, multi-page Indian health insurance wordings and applies rigorous deterministic validation.
        </p>
      </div>

      <div class="pipeline-wrapper">
        
        <!-- Step 1: Upload -->
        <div class="pipeline-step">
          <div class="step-badge">1</div>
          <div class="step-connector"></div>
          <div class="step-card step-1">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                UPLOAD
              </div>
              <span class="tech-pill">PDF INGESTION</span>
            </div>
            <p class="step-desc">
              Drop your insurance policy PDF or select any pre-indexed insurer plan. We handle scanned documents, digital policy schedules, riders, endorsements, and customer information sheets (CIS).
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">50+ Insurers</span>
              <span class="tech-pill">25MB Limit</span>
              <span class="tech-pill">Client-side Encryption</span>
            </div>
          </div>
        </div>

        <!-- Step 2: Parse & OCR -->
        <div class="pipeline-step">
          <div class="step-badge">2</div>
          <div class="step-connector"></div>
          <div class="step-card step-2">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/></svg>
                PARSE & OCR
              </div>
              <span class="tech-pill">DOCUMENT VISION</span>
            </div>
            <p class="step-desc">
              Multi-column layout analysis extracts complex tables, exclusions lists, and sub-limit matrices. OCR accurately decodes footnotes, asterisks, and annexures that insurers tuck into fine print.
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">Table Extraction</span>
              <span class="tech-pill">Footnote Tracing</span>
              <span class="tech-pill">Page Coordinate Indexing</span>
            </div>
          </div>
        </div>

        <!-- Step 3: Structure -->
        <div class="pipeline-step">
          <div class="step-badge">3</div>
          <div class="step-connector"></div>
          <div class="step-card step-3">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                STRUCTURE
              </div>
              <span class="tech-pill">SCHEMA NORMALIZATION</span>
            </div>
            <p class="step-desc">
              Converts policy legalese into a validated JSON schema aligned with IRDAI definitions: room rent caps, ICU allowances, waiting period schedules (initial, PED, specific ailments), copays, and restore benefits.
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">IRDAI Master Circular</span>
              <span class="tech-pill">Normalized JSON</span>
              <span class="tech-pill">Clause Taxonomies</span>
            </div>
          </div>
        </div>

        <!-- Step 4: Query -->
        <div class="pipeline-step">
          <div class="step-badge">4</div>
          <div class="step-connector"></div>
          <div class="step-card step-4">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                QUERY
              </div>
              <span class="tech-pill">MEDICAL NLP</span>
            </div>
            <p class="step-desc">
              Ask in conversational English (e.g. "I need knee replacement, am I covered?"). Insurix maps colloquial medical terms to clinical categories, surgical classifications, and standard ICD-10 diagnostic codes.
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">Semantic Entity Match</span>
              <span class="tech-pill">ICD-10 Mapping</span>
              <span class="tech-pill">Synonym Disambiguation</span>
            </div>
          </div>
        </div>

        <!-- Step 5: Match & Rules -->
        <div class="pipeline-step">
          <div class="step-badge">5</div>
          <div class="step-connector"></div>
          <div class="step-card step-5">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
                MATCH & RULES
              </div>
              <span class="tech-pill">DETERMINISTIC EVALUATION</span>
            </div>
            <p class="step-desc">
              Zero hallucination rule execution. The engine evaluates: Has the 30-day or 36-month waiting period elapsed? Is the procedure under the permanent exclusion list? Does a disease-specific sub-limit apply?
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">Zero Hallucinations</span>
              <span class="tech-pill">Waiting Period Matrix</span>
              <span class="tech-pill">Exclusion Checks</span>
            </div>
          </div>
        </div>

        <!-- Step 6: Estimate -->
        <div class="pipeline-step">
          <div class="step-badge">6</div>
          <div class="step-connector"></div>
          <div class="step-card step-6">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="8" y2="10.01"/><line x1="12" y1="10" x2="12" y2="10.01"/><line x1="16" y1="10" x2="16" y2="10.01"/><line x1="8" y1="14" x2="8" y2="14.01"/><line x1="12" y1="14" x2="12" y2="14.01"/><line x1="16" y1="14" x2="16" y2="14.01"/><line x1="8" y1="18" x2="8" y2="18.01"/><line x1="12" y1="18" x2="12" y2="18.01"/><line x1="16" y1="18" x2="16" y2="18.01"/></svg>
                ESTIMATE
              </div>
              <span class="tech-pill">COST ENGINE</span>
            </div>
            <p class="step-desc">
              Combines policy sub-limits with real hospital benchmarks. Calculates room rent proportionate deduction penalties, mandatory consumables non-covered expenses, deductibles, and co-payment percentages.
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">Proportionate Deductions</span>
              <span class="tech-pill">Co-Pay Math</span>
              <span class="tech-pill">Non-Medical Itemization</span>
            </div>
          </div>
        </div>

        <!-- Step 7: Explain -->
        <div class="pipeline-step">
          <div class="step-badge">7</div>
          <div class="step-card step-7">
            <div class="step-top">
              <div class="step-title">
                <svg class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                EXPLAIN
              </div>
              <span class="tech-pill">AUDITABLE OUTPUT</span>
            </div>
            <p class="step-desc">
              Delivers an auditable summary with direct page citations and section numbers. When policies contain ambiguous or conflicting wording, Insurix highlights missing information and gives actionable questions for your TPA.
            </p>
            <div class="step-pill-list">
              <span class="tech-pill">Page Citations</span>
              <span class="tech-pill">Confidence Scores</span>
              <span class="tech-pill">TPA Action Items</span>
            </div>
          </div>
        </div>

      </div>

      <div style="text-align:center; margin-top:36px;">
        <button class="cta-button" onclick="navigateTo('demo')">
          Launch Interactive Simulator Now →
        </button>
      </div>
    </section>

    <!-- ==========================================================================
         PAGE 3: FEATURES VIEW
         ========================================================================== -->
    <section id="view-features" class="view-section">
      <div class="section-header">
        <span class="section-eyebrow">Enterprise-Grade Capabilities</span>
        <h2 class="section-title">BUILT FOR COMPLETE FINANCIAL CLARITY</h2>
        <p class="section-subtitle">
          No guesswork. No hidden clauses. Pure deterministic policy intelligence built strictly against Indian health insurance regulations.
        </p>
      </div>

      <div class="features-grid">
        
        <!-- Feature 1 -->
        <article class="feature-card fc-lime">
          <div>
            <div class="feature-icon-box">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
            </div>
            <h3 class="feature-title">Policy Intelligence</h3>
            <p class="feature-desc">
              Advanced document ingestion extracts tabular sub-limits, specific disease waiting period annexures, cumulative bonuses, and restored sum insured mechanics from standard and customized corporate policies.
            </p>
          </div>
          <div class="feature-pills">
            <span class="tech-pill">OCR Engine</span>
            <span class="tech-pill">NLP Extraction</span>
            <span class="tech-pill">Structured Schema</span>
            <span class="tech-pill">Endorsement Auditing</span>
          </div>
        </article>

        <!-- Feature 2 -->
        <article class="feature-card fc-white">
          <div>
            <div class="feature-icon-box">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
            </div>
            <h3 class="feature-title">Evidence-Backed Answers</h3>
            <p class="feature-desc">
              Every single claim made by Insurix includes clickable page citations, clause sections, and exact verbatim extracts from your uploaded wording. Never walk into a hospital without documented proof.
            </p>
          </div>
          <div class="feature-pills">
            <span class="tech-pill">Citations</span>
            <span class="tech-pill">Page References</span>
            <span class="tech-pill">Section Numbers</span>
            <span class="tech-pill">Zero Hallucinations</span>
          </div>
        </article>

        <!-- Feature 3 -->
        <article class="feature-card fc-cyan">
          <div>
            <div class="feature-icon-box">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M12 12h.01"/><path d="M17 12h.01"/><path d="M7 12h.01"/></svg>
            </div>
            <h3 class="feature-title">Treatment Analysis</h3>
            <p class="feature-desc">
              Evaluate real clinical scenarios. Insurix cross-references whether a procedure qualifies as day-care treatment (under 24 hours), requires continuous 24-hr hospitalization, or falls under modern robotic treatments.
            </p>
          </div>
          <div class="feature-pills">
            <span class="tech-pill">ICD-10 Mapping</span>
            <span class="tech-pill">Day Care Surgery</span>
            <span class="tech-pill">Robotic Procedures</span>
            <span class="tech-pill">AYUSH Coverage</span>
          </div>
        </article>

        <!-- Feature 4 -->
        <article class="feature-card fc-pink">
          <div>
            <div class="feature-icon-box">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="8" y2="10.01"/><line x1="12" y1="10" x2="12" y2="10.01"/><line x1="16" y1="10" x2="16" y2="10.01"/><line x1="8" y1="14" x2="8" y2="14.01"/><line x1="12" y1="14" x2="12" y2="14.01"/><line x1="16" y1="14" x2="16" y2="14.01"/><line x1="8" y1="18" x2="8" y2="18.01"/><line x1="12" y1="18" x2="12" y2="18.01"/><line x1="16" y1="18" x2="16" y2="18.01"/></svg>
            </div>
            <h3 class="feature-title">Cost Estimation</h3>
            <p class="feature-desc">
              Going far beyond a simplistic "yes/no" covered flag. Insurix projects your true out-of-pocket liabilities by simulating proportionate room deductions, age-based co-pays, non-medical consumables, and voluntary deductibles.
            </p>
          </div>
          <div class="feature-pills">
            <span class="tech-pill">Deductibles</span>
            <span class="tech-pill">Co-Payment Math</span>
            <span class="tech-pill">Room Rent Caps</span>
            <span class="tech-pill">Out-of-Pocket</span>
          </div>
        </article>

        <!-- Feature 5 -->
        <article class="feature-card fc-orange">
          <div>
            <div class="feature-icon-box">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            </div>
            <h3 class="feature-title">Uncertainty Detection</h3>
            <p class="feature-desc">
              When an insurer uses murky or deliberately ambiguous phrasing, Insurix refuses to gamble. It marks confidence levels (High / Medium / Low), highlights missing documentation, and arms you with clarification questions.
            </p>
          </div>
          <div class="feature-pills">
            <span class="tech-pill">Confidence Badging</span>
            <span class="tech-pill">Ambiguity Flags</span>
            <span class="tech-pill">Missing Info Tracker</span>
            <span class="tech-pill">TPA Questions</span>
          </div>
        </article>

        <!-- Feature 6 -->
        <article class="feature-card fc-mint">
          <div>
            <div class="feature-icon-box">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
            </div>
            <h3 class="feature-title">Transparent Breakdown</h3>
            <p class="feature-desc">
              Inspect step-by-step why an expense was disallowed or reduced. Drill down into every rupee of hospital room charge, surgeon fee, medical implant capping, or diagnostic cost with complete audit trail integrity.
            </p>
          </div>
          <div class="feature-pills">
            <span class="tech-pill">Rule Tracing</span>
            <span class="tech-pill">Audit Trail</span>
            <span class="tech-pill">Source Links</span>
            <span class="tech-pill">PDF Export</span>
          </div>
        </article>

      </div>
    </section>

    <!-- ==========================================================================
         PAGE 4: TRY IT / DEMO VIEW
         ========================================================================== -->
    <section id="view-demo" class="view-section">
      <div class="section-header">
        <span class="section-eyebrow">Interactive Intelligence Studio</span>
        <h2 class="section-title">TEST YOUR POLICY IN REAL-TIME</h2>
        <p class="section-subtitle">
          Ask clinical questions, test out-of-pocket costs with our hospital procedure calculator, and inspect exact clause citations.
        </p>
      </div>

      <div class="demo-workspace">
        
        <!-- Left Column: Policy Management & Summary Panel -->
        <aside class="demo-sidebar">
          
          <!-- Upload Panel -->
          <div class="sidebar-panel">
            <div class="sidebar-title">
              <span>Policy Document</span>
              <span class="tech-pill">OCR Active</span>
            </div>

            <div class="upload-zone" style="padding:22px 14px; margin-bottom:12px;" onclick="triggerFileInput('demo-file-input')">
              <input type="file" id="demo-file-input" style="display:none" accept="application/pdf" onchange="handleFileSelected(event)">
              <svg class="upload-icon" style="width:36px; height:36px; margin-bottom:6px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
              <div style="font-size:0.92rem; font-weight:700;">Drop or Choose Policy PDF</div>
              <div style="font-size:0.75rem; opacity:0.8;">Star, HDFC, Care, Royal Sundaram</div>
            </div>

            <div style="font-size:0.8rem; font-weight:700; margin-bottom:6px;">Switch Active Sample:</div>
            <div style="display:flex; flex-direction:column; gap:6px;">
              <button class="sample-btn selected" id="sample-btn-star" onclick="loadSamplePolicy('star')">
                <span>⭐ Star Health Comprehensive</span>
                <span class="sample-tag">₹5L</span>
              </button>
              <button class="sample-btn" id="sample-btn-royal" onclick="loadSamplePolicy('royal')">
                <span>🛡️ Royal Sundaram Lifeline</span>
                <span class="sample-tag">₹10L</span>
              </button>
              <button class="sample-btn" id="sample-btn-hdfc" onclick="loadSamplePolicy('hdfc')">
                <span>⚡ HDFC ERGO Optima Restore</span>
                <span class="sample-tag">₹5L</span>
              </button>
            </div>
          </div>

          <!-- Active Policy Breakdown Panel -->
          <div class="sidebar-panel" id="policy-details-panel">
            <div class="sidebar-title">
              <span id="active-policy-title">Star Comprehensive</span>
              <button class="tech-pill" style="cursor:pointer;" onclick="viewRawPolicyModal()">Raw Clauses</button>
            </div>
            
            <table class="policy-spec-table">
              <tr>
                <td>Insurer</td>
                <td id="spec-insurer">Star Health Insurance</td>
              </tr>
              <tr>
                <td>Sum Insured</td>
                <td id="spec-sum">₹5,00,000</td>
              </tr>
              <tr>
                <td>Initial Waiting</td>
                <td id="spec-wait-init">30 Days</td>
              </tr>
              <tr>
                <td>PED Waiting</td>
                <td id="spec-wait-ped">36 Months</td>
              </tr>
              <tr>
                <td>Specific Diseases</td>
                <td id="spec-wait-spec">24 Months</td>
              </tr>
              <tr>
                <td>Room Rent Limit</td>
                <td id="spec-room">1% SI / Day (₹5,000)</td>
              </tr>
              <tr>
                <td>ICU Limit</td>
                <td id="spec-icu">2% SI / Day (₹10,000)</td>
              </tr>
              <tr>
                <td>Co-payment</td>
                <td id="spec-copay">10% for age 60+</td>
              </tr>
              <tr>
                <td>Cataract Sub-limit</td>
                <td id="spec-cataract">₹25,000 / eye</td>
              </tr>
              <tr>
                <td>Knee Replacement</td>
                <td id="spec-knee">No sub-limit</td>
              </tr>
            </table>
          </div>

          <!-- Quick Action Prompts -->
          <div class="sidebar-panel">
            <div class="sidebar-title">
              <span>Quick Inquiries</span>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <button class="chat-chip" style="text-align:left;" onclick="askPresetQuestion('demo', 'Is knee replacement surgery covered under my policy?')">
                🦴 Total Knee Replacement coverage?
              </button>
              <button class="chat-chip" style="text-align:left;" onclick="askPresetQuestion('demo', 'What happens if I choose a room with rent above ₹5,000/day?')">
                🏥 Room rent proportionate deduction?
              </button>
              <button class="chat-chip" style="text-align:left;" onclick="askPresetQuestion('demo', 'What is the exact cataract surgery sub-limit and out-of-pocket?')">
                👁️ Cataract surgery limits & co-pay?
              </button>
              <button class="chat-chip" style="text-align:left;" onclick="askPresetQuestion('demo', 'What are my waiting periods for hypertension and diabetes?')">
                ⏳ Pre-existing disease waiting periods?
              </button>
            </div>
          </div>

        </aside>

        <!-- Right Column: Interactive Studio (Chat + Treatment Cost Simulator) -->
        <main class="demo-main-panel">
          
          <!-- Mode Tabs -->
          <div class="demo-tabs">
            <button class="demo-tab-btn active" id="tab-btn-chat" onclick="switchDemoTab('chat')">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              AI Policy Chatbot
            </button>
            <button class="demo-tab-btn" id="tab-btn-calc" onclick="switchDemoTab('calc')">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="8" y2="10.01"/><line x1="12" y1="10" x2="12" y2="10.01"/><line x1="16" y1="10" x2="16" y2="10.01"/><line x1="8" y1="14" x2="8" y2="14.01"/><line x1="12" y1="14" x2="12" y2="14.01"/><line x1="16" y1="14" x2="16" y2="14.01"/><line x1="8" y1="18" x2="8" y2="18.01"/><line x1="12" y1="18" x2="12" y2="18.01"/><line x1="16" y1="18" x2="16" y2="18.01"/></svg>
              Treatment Out-of-Pocket Calculator
            </button>
          </div>

          <!-- TAB 1: Chat Assistant -->
          <div id="demo-chat-view">
            <div class="chat-container" id="demo-chat-container">
              <!-- Seed message -->
              <div class="chat-message assistant">
                <div class="message-text">
                  👋 <strong>Welcome to Insurix Policy Intelligence.</strong>
                  <br>
                  Active policy loaded: <span style="background:var(--lime); padding:2px 6px; border:2px solid var(--black); border-radius:4px; font-weight:700;">Star Comprehensive (₹5,00,000)</span>.
                  Ask me anything regarding treatments, deductibles, waiting periods, or hospital stay deductions.
                </div>
              </div>
            </div>

            <!-- Suggestion chips -->
            <div class="chat-quick-chips">
              <span style="font-size:0.8rem; font-weight:700; align-self:center;">Quick Questions:</span>
              <button class="chat-chip" onclick="askPresetQuestion('demo', 'Is knee replacement covered under my policy?')">Knee replacement?</button>
              <button class="chat-chip" onclick="askPresetQuestion('demo', 'What is my room rent limit and ICU capping?')">Room rent limit?</button>
              <button class="chat-chip" onclick="askPresetQuestion('demo', 'How much will I pay out-of-pocket for Cataract surgery?')">Cataract surgery?</button>
              <button class="chat-chip" onclick="askPresetQuestion('demo', 'What pre-existing disease waiting period applies?')">Waiting periods?</button>
              <button class="chat-chip" onclick="askPresetQuestion('demo', 'Does my policy have co-payment for senior citizens?')">Senior citizen co-pay?</button>
            </div>

            <!-- Input Bar -->
            <div class="chat-input-bar" style="margin-top:14px;">
              <input type="text" id="demo-chat-input" class="chat-input" placeholder="Ask anything about your policy coverage..." onkeypress="handleChatEnter(event, 'demo')">
              <button class="chat-send-btn" onclick="sendChatQuery('demo')">
                <span>Send</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
              </button>
            </div>
          </div>

          <!-- TAB 2: Treatment Out-of-Pocket Calculator -->
          <div id="demo-calc-view" style="display:none;">
            <div class="treatment-calc-card">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:18px;">
                <h3 style="font-size:1.4rem; font-weight:700;">Hospital Cost & Out-of-Pocket Simulator</h3>
                <span class="tech-pill">Proportionate Deduction Math</span>
              </div>
              <p style="font-size:0.95rem; margin-bottom:20px; opacity:0.85;">
                Simulate your exact treatment scenario against the active policy's terms. Our engine calculates room rent proportionate penalties, senior co-pays, non-medical consumables, and disease sub-limits.
              </p>

              <div class="calc-form-grid">
                
                <div class="form-group">
                  <label for="calc-treatment-select">Planned Treatment / Procedure</label>
                  <select id="calc-treatment-select" class="treatment-select" onchange="updateTreatmentDefaults()">
                    <option value="knee_replacement">Total Knee Replacement (Orthopedic)</option>
                    <option value="cataract">Cataract Surgery (Ophthalmology)</option>
                    <option value="appendectomy">Appendectomy (General Surgery)</option>
                    <option value="cabg">CABG Bypass Surgery (Cardiac)</option>
                    <option value="dialysis">Dialysis Session (Nephrology)</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="calc-bill-amount">Estimated Hospital Bill (₹)</label>
                  <input type="number" id="calc-bill-amount" class="form-control" value="280000" step="5000">
                </div>

                <div class="form-group">
                  <label for="calc-hospital-type">Hospital Category</label>
                  <select id="calc-hospital-type" class="treatment-select">
                    <option value="network">Network Hospital (100% Tariff Cashless)</option>
                    <option value="non_network">Non-Network Hospital (Subject to Customary Deductions)</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="calc-room-type">Room Category Chosen</label>
                  <select id="calc-room-type" class="treatment-select">
                    <option value="within_limit">Single Standard Room (₹5,000/day - Within Limit)</option>
                    <option value="exceeds_deluxe">Deluxe Room (₹8,000/day - Exceeds 1% SI Limit)</option>
                    <option value="suite">Suite Room (₹12,000/day - Triggers Heavy Penalty)</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="calc-patient-age">Patient Age</label>
                  <input type="number" id="calc-patient-age" class="form-control" value="62" min="1" max="100">
                </div>

                <div class="form-group">
                  <label for="calc-waiting-status">Policy Tenure / Waiting Period Status</label>
                  <select id="calc-waiting-status" class="treatment-select">
                    <option value="completed">Completed (>36 months active - 100% eligible)</option>
                    <option value="partial">1st Year Active (Pre-existing diseases barred)</option>
                  </select>
                </div>

              </div>

              <button class="cta-button" style="width:100%;" onclick="runTreatmentCalculation()">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                Calculate Exact Financial Out-of-Pocket
              </button>

              <!-- Calculation Results Box -->
              <div id="calc-results-output" class="calc-result-box">
                <div class="calc-summary-row">
                  <div class="calc-stat">
                    <div style="font-size:0.78rem; font-weight:700; text-transform:uppercase;">Total Hospital Bill</div>
                    <div id="res-total-bill" style="font-size:1.6rem; font-weight:700;">₹2,80,000</div>
                  </div>
                  <div class="calc-stat stat-mint">
                    <div style="font-size:0.78rem; font-weight:700; text-transform:uppercase;">Insurer Pays</div>
                    <div id="res-insurer-pays" style="font-size:1.6rem; font-weight:700;">₹2,10,000</div>
                  </div>
                  <div class="calc-stat stat-orange">
                    <div style="font-size:0.78rem; font-weight:700; text-transform:uppercase;">You Pay (Out-of-Pocket)</div>
                    <div id="res-you-pay" style="font-size:1.6rem; font-weight:700;">₹70,000</div>
                  </div>
                </div>

                <div style="font-weight:700; margin-bottom:8px;">Deductions Breakdown & Rule Tracing:</div>
                <table class="cost-table" style="margin-top:0;">
                  <thead>
                    <tr>
                      <th>Cost Component</th>
                      <th>Amount</th>
                      <th>Policy Rule Applied</th>
                    </tr>
                  </thead>
                  <tbody id="calc-breakdown-tbody">
                    <tr><td>Base Procedure & Surgeon Charges</td><td>₹2,10,000</td><td>Approved under Section 4.2</td></tr>
                    <tr><td>Room Rent Proportional Penalty</td><td>₹0</td><td>Selected room meets 1% SI capping</td></tr>
                    <tr><td>Co-payment Deduction (10%)</td><td>₹21,000</td><td>Age 62 exceeds 60+ threshold (Clause 5.4)</td></tr>
                    <tr><td>Consumables & Non-Medical Items</td><td>₹29,000</td><td>IRDAI Non-Payables Annexure I</td></tr>
                    <tr><td>Policy Deductible</td><td>₹20,000</td><td>Voluntary policy deductible</td></tr>
                    <tr class="total-row"><td><strong>Net Estimated Patient Liability</strong></td><td><strong>₹70,000</strong></td><td><strong>Action: In-network pre-authorization required</strong></td></tr>
                  </tbody>
                </table>
              </div>

            </div>
          </div>

        </main>

      </div>
    </section>

    <!-- ==========================================================================
         PAGE 5: PRICING / PLANS VIEW
         ========================================================================== -->
    <section id="view-pricing" class="view-section">
      <div class="section-header" style="text-align:center;">
        <span class="section-eyebrow">Fair & Transparent</span>
        <h2 class="section-title">NEVER GET BILL SHOCK AGAIN</h2>
        <p class="section-subtitle" style="margin: 0 auto;">
          Choose the plan that fits your family or healthcare advisory practice.
        </p>
      </div>

      <div class="billing-toggle-wrap">
        <span style="font-weight:700;">Monthly</span>
        <div class="billing-pill active" id="billing-btn-monthly" onclick="setBilling('monthly')">Monthly Billing</div>
        <div class="billing-pill" id="billing-btn-annual" onclick="setBilling('annual')">Annual (Save 30%) ⚡</div>
      </div>

      <div class="pricing-grid">
        
        <!-- FREE PLAN -->
        <article class="pricing-card plan-free">
          <div>
            <div class="plan-header">
              <h3 class="plan-name">Free Starter</h3>
              <div class="plan-price">
                <span class="price-amount" id="price-free">₹0</span>
                <span class="price-period">/ month</span>
              </div>
              <p class="plan-desc">For individuals reviewing a single health insurance policy document.</p>
            </div>

            <ul class="plan-features">
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                3 Policy uploads per month
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Basic natural language Q&A
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Standard waiting period scan
              </li>
              <li class="plan-feature-item" style="opacity:0.5;">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                No procedure out-of-pocket calculator
              </li>
              <li class="plan-feature-item" style="opacity:0.5;">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                No PDF export report
              </li>
            </ul>
          </div>

          <button class="ghost-button" style="width:100%;" onclick="openPlanModal('Free')">
            Get Started Free
          </button>
        </article>

        <!-- PRO PLAN (MOST POPULAR) -->
        <article class="pricing-card plan-pro">
          <div class="popular-ribbon">⭐ MOST POPULAR</div>
          <div>
            <div class="plan-header">
              <h3 class="plan-name">Pro Member</h3>
              <div class="plan-price">
                <span class="price-amount" id="price-pro">₹499</span>
                <span class="price-period" id="period-pro">/ month</span>
              </div>
              <p class="plan-desc">Complete financial clarity for families and high-coverage policyholders.</p>
            </div>

            <ul class="plan-features">
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                <strong>Unlimited policy uploads & riders</strong>
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Full Q&A with exact page & clause citations
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Interactive Out-of-Pocket treatment calculator
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Uncertainty & fine-print ambiguity detection
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Download verified hospital audit reports (PDF)
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Priority document parsing (Vision OCR)
              </li>
            </ul>
          </div>

          <button class="cta-button" style="width:100%; background:var(--black); color:var(--white); box-shadow:5px 5px 0 var(--white);" onclick="openPlanModal('Pro')">
            Start 14-Day Free Pro Trial →
          </button>
        </article>

        <!-- ENTERPRISE PLAN -->
        <article class="pricing-card plan-enterprise">
          <div>
            <div class="plan-header">
              <h3 class="plan-name">Enterprise</h3>
              <div class="plan-price">
                <span class="price-amount" id="price-ent">Custom</span>
              </div>
              <p class="plan-desc">For hospitals, TPAs, corporate HRs, and insurtech distribution platforms.</p>
            </div>

            <ul class="plan-features">
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                REST & GraphQL Policy Extraction APIs
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Bulk batch processing of 100,000+ policies
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Custom Hospital Tariff integration
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                Dedicated HIPAA & SOC2 Compliant instance
              </li>
              <li class="plan-feature-item">
                <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                24/7 SLA & Dedicated Solutions Engineer
              </li>
            </ul>
          </div>

          <button class="ghost-button" style="width:100%;" onclick="openPlanModal('Enterprise')">
            Contact Sales Team
          </button>
        </article>

      </div>
    </section>

    <!-- ==========================================================================
         PAGE 6: FAQ VIEW
         ========================================================================== -->
    <section id="view-faq" class="view-section">
      <div class="section-header" style="text-align:center;">
        <span class="section-eyebrow">Common Inquiries</span>
        <h2 class="section-title">FREQUENTLY ASKED QUESTIONS</h2>
        <p class="section-subtitle" style="margin:0 auto;">
          Straightforward answers about our AI verification model, security standards, and IRDAI compliance.
        </p>
      </div>

      <div class="faq-list">
        
        <!-- FAQ 1 -->
        <div class="accordion-item open">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>1. What types of insurance policies does Insurix support?</span>
            <span class="accordion-icon">-</span>
          </button>
          <div class="accordion-body" style="max-height: 200px;">
            <div class="accordion-body-inner">
              Insurix supports all major retail, family floater, senior citizen, critical illness, top-up, super top-up, and corporate/group health insurance policies issued in India. Our parser handles scanned PDF policy wordings, customer information sheets (CIS), schedules, and endorsement riders across 50+ IRDAI-registered insurers including Star Health, HDFC ERGO, Care, ICICI Lombard, Niva Bupa, and public sector insurers.
            </div>
          </div>
        </div>

        <!-- FAQ 2 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>2. How accurate are the cost estimates?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Our policy clause extraction engine operates at 99.2% accuracy tested against IRDAI standardized benchmark datasets. Treatment cost estimates combine deterministic policy terms (room rent capping, copays, deductibles) with regional hospital rate cards. While individual surgeon bills may vary, our mathematical deduction model reliably predicts hospital disallowances and out-of-pocket liabilities.
            </div>
          </div>
        </div>

        <!-- FAQ 3 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>3. Is my policy data secure?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Yes. Your policy document is processed with end-to-end TLS 1.3 encryption. We automatically redact personal identifiable identifiers (PII) such as Aadhaar, PAN, phone numbers, and home addresses before semantic indexing. We never sell your data to brokers, aggregators, or third-party marketers.
            </div>
          </div>
        </div>

        <!-- FAQ 4 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>4. Can I use Insurix for corporate / group health insurance?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Absolutely. Simply upload your corporate group insurance summary or GMC handbook. Insurix extracts corporate-negotiated waivers (e.g. 0-day waiting periods for maternity, waiver of pre-existing condition waiting times, and custom room rent caps) and evaluates treatments accordingly.
            </div>
          </div>
        </div>

        <!-- FAQ 5 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>5. What if my policy contains ambiguous language?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Unlike generic LLMs that hallucinate answers, Insurix activates its Uncertainty Detection System when wording is vague. It flags a "Medium" or "Low" confidence warning, quotes the conflicting sections, and provides you with a checklist of exact questions to submit to your insurer or TPA desk prior to hospitalization.
            </div>
          </div>
        </div>

        <!-- FAQ 6 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>6. How does Insurix handle waiting periods?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Insurix categorizes waiting periods into three distinct tiers defined by IRDAI: (1) Initial 30-day waiting period for non-accidental hospitalizations, (2) 24-month waiting period for specific listed illnesses (such as cataract, hernia, joint replacements, and piles), and (3) Pre-Existing Disease (PED) waiting periods (typically 24 to 36 months). It calculates eligibility based on your policy start date.
            </div>
          </div>
        </div>

        <!-- FAQ 7 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>7. Can I compare multiple policies side-by-side?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Yes, Pro and Enterprise members can upload multiple policies (such as a base policy and a super top-up policy) to visualize combined coverage, deductible hand-offs, and discover which policy will cover specific non-payable expenses.
            </div>
          </div>
        </div>

        <!-- FAQ 8 -->
        <div class="accordion-item">
          <button class="accordion-toggle" onclick="toggleAccordion(this)">
            <span>8. Is there a mobile app available?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-body">
            <div class="accordion-body-inner">
              Insurix is built as a responsive Progressive Web Application (PWA) optimized for desktop, tablets, and smartphones. You can save it directly to your iOS or Android home screen with zero installation friction, allowing immediate access at hospital admission desks.
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ==========================================================================
         PAGE 7: CONTACT VIEW
         ========================================================================== -->
    <section id="view-contact" class="view-section">
      <div class="section-header">
        <span class="section-eyebrow">Direct Desk</span>
        <h2 class="section-title">CONNECT WITH POLICY SPECIALISTS</h2>
        <p class="section-subtitle">
          Have a dispute with your TPA or need enterprise API integration? Get in touch directly.
        </p>
      </div>

      <div class="contact-grid">
        
        <!-- Left: Contact Form -->
        <article class="contact-form-card">
          <div class="contact-banner">
            Have questions about your health insurance policy?
          </div>

          <form id="contact-form" onsubmit="handleContactSubmit(event)">
            <div class="form-group" style="margin-bottom:16px;">
              <label for="contact-name">Full Name</label>
              <input type="text" id="contact-name" class="form-control" placeholder="e.g. Sarthak Sharma" required>
            </div>

            <div class="form-group" style="margin-bottom:16px;">
              <label for="contact-email">Email Address</label>
              <input type="email" id="contact-email" class="form-control" placeholder="sarthak@example.com" required>
            </div>

            <div class="form-group" style="margin-bottom:16px;">
              <label for="contact-insurer">Insurance Provider / Policy Type</label>
              <select id="contact-insurer" class="treatment-select">
                <option value="Star Health">Star Health & Allied Insurance</option>
                <option value="HDFC ERGO">HDFC ERGO General Insurance</option>
                <option value="Care Health">Care Health Insurance (Religare)</option>
                <option value="Royal Sundaram">Royal Sundaram General Insurance</option>
                <option value="ICICI Lombard">ICICI Lombard General Insurance</option>
                <option value="Niva Bupa">Niva Bupa Health Insurance</option>
                <option value="Corporate GMC">Corporate Group Medical Cover (GMC)</option>
                <option value="Other">Other Insurer</option>
              </select>
            </div>

            <div class="form-group" style="margin-bottom:20px;">
              <label for="contact-message">Message or Policy Clause Question</label>
              <textarea id="contact-message" class="form-control" rows="4" placeholder="Describe your policy question or planned hospital admission..." required></textarea>
            </div>

            <button type="submit" class="cta-button" style="width:100%;">
              <span>Send Message Directly</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            </button>
          </form>
        </article>

        <!-- Right: Social & Office Badges -->
        <aside class="contact-info-card">
          
          <div class="info-box">
            <h3 style="font-size:1.4rem; font-weight:700; margin-bottom:8px;">Fast Support Desk</h3>
            <p style="font-size:0.95rem; font-weight:500; margin-bottom:16px;">
              Our health policy research team reviews claims interpretations and IRDAI Ombudsman precedent cases daily.
            </p>
            <div style="background:var(--white); border:3px solid var(--black); border-radius:8px; padding:12px; font-weight:700; font-size:0.9rem;">
              ⏱️ Average Response Time: <strong>&lt; 2 Hours</strong>
            </div>
          </div>

          <div class="social-badge-grid">
            <a href="mailto:support@insurix.ai" class="social-badge-btn">
              <div class="mono-circle">@</div>
              <div>
                <div style="font-size:0.75rem; opacity:0.8;">EMAIL US</div>
                <div>support@insurix.ai</div>
              </div>
            </a>

            <a href="tel:+918040001000" class="social-badge-btn">
              <div class="mono-circle">📞</div>
              <div>
                <div style="font-size:0.75rem; opacity:0.8;">TOLL FREE</div>
                <div>1800-INSURIX</div>
              </div>
            </a>

            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="social-badge-btn">
              <div class="mono-circle">IN</div>
              <div>
                <div style="font-size:0.75rem; opacity:0.8;">LINKEDIN</div>
                <div>/company/insurix</div>
              </div>
            </a>

            <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="social-badge-btn">
              <div class="mono-circle">GH</div>
              <div>
                <div style="font-size:0.75rem; opacity:0.8;">GITHUB</div>
                <div>/insurix-ai</div>
              </div>
            </a>
          </div>

          <div style="background:var(--neon-mint); border:4px solid var(--black); border-radius:10px; padding:18px; box-shadow:5px 5px 0 var(--black); font-size:0.9rem;">
            <strong>📍 Headquarters:</strong><br>
            Insurix Policy Labs India Pvt Ltd<br>
            Level 4, 100 Feet Road, Indiranagar, Bangalore 560038
          </div>

        </aside>

      </div>
    </section>

    <!-- Disclaimer Alert -->
    <div class="disclaimer-box" style="margin-top:52px;">
      <strong>⚠️ IRDAI Regulatory & Medical Notice:</strong>
      Insurix is an independent artificial intelligence policy analysis tool built strictly to parse insurance policy wordings and mathematical financial covenants. Insurix does not provide clinical diagnosis or medical advice. Pre-authorization and final claim sanction rests with the respective insurance company and licensed Third Party Administrator (TPA).
    </div>

    <!-- Neo-Brutalist Footer -->
    <footer class="site-footer">
      <div class="footer-top">
        
        <div class="footer-brand">
          <h2>INSURIX</h2>
          <p>
            AI-powered health insurance policy intelligence. Transforming policy confusion into financial clarity with 99.2% evidence accuracy.
          </p>
          <div style="display:flex; gap:8px;">
            <span class="tech-pill">IRDAI Master Circular 2024</span>
            <span class="tech-pill">Zero Hallucinations</span>
          </div>
        </div>

        <div class="footer-col">
          <h4>Navigation</h4>
          <ul class="footer-links">
            <li><a class="footer-link" onclick="navigateTo('home')">Home</a></li>
            <li><a class="footer-link" onclick="navigateTo('how-it-works')">7-Step Pipeline</a></li>
            <li><a class="footer-link" onclick="navigateTo('features')">Features</a></li>
            <li><a class="footer-link" onclick="navigateTo('demo')">Try Demo Studio</a></li>
            <li><a class="footer-link" onclick="navigateTo('pricing')">Pricing & Plans</a></li>
            <li><a class="footer-link" onclick="navigateTo('faq')">FAQ</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Sample Insurers</h4>
          <ul class="footer-links">
            <li><a class="footer-link" onclick="loadSamplePolicy('star'); navigateTo('demo');">Star Health Comprehensive</a></li>
            <li><a class="footer-link" onclick="loadSamplePolicy('royal'); navigateTo('demo');">Royal Sundaram Lifeline</a></li>
            <li><a class="footer-link" onclick="loadSamplePolicy('hdfc'); navigateTo('demo');">HDFC ERGO Optima Restore</a></li>
            <li><a class="footer-link" onclick="navigateTo('demo')">Upload Custom PDF</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Compliance & Legal</h4>
          <ul class="footer-links">
            <li><a class="footer-link" onclick="showToast('Privacy Policy: End-to-end encrypted with zero broker sharing')">Privacy Policy</a></li>
            <li><a class="footer-link" onclick="showToast('Terms: For policy wording analytics & estimates')">Terms of Service</a></li>
            <li><a class="footer-link" onclick="showToast('IRDAI Master Circular Compliance Verified')">IRDAI Compliance</a></li>
            <li><a class="footer-link" onclick="navigateTo('contact')">Ombudsman Grievance Desk</a></li>
          </ul>
        </div>

      </div>

      <div class="footer-bottom">
        <div>
          © 2026 INSURIX INC. ALL RIGHTS RESERVED. "Policy confusion → Financial clarity"
        </div>
        <div style="display:flex; gap:14px; align-items:center;">
          <span style="display:flex; align-items:center; gap:6px;">
            <span class="pulse-dot"></span> System Status: All OCR Nodes Operational
          </span>
        </div>
      </div>
    </footer>

  </main>

  <!-- ==========================================================================
       MODALS
       ========================================================================== -->
  
  <!-- Clause Verification Modal -->
  <div class="modal-backdrop" id="clause-modal" onclick="closeClauseModal(event)">
    <div class="modal-panel" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeClauseModal()">&times;</button>
      <div style="display:inline-block; background:var(--purple); color:var(--black); border:2px solid var(--black); border-radius:5px; padding:3px 8px; font-weight:700; font-size:0.8rem; margin-bottom:10px;" id="modal-clause-badge">
        Page 18, Section 4.2
      </div>
      <h3 style="font-size:1.5rem; font-weight:700; margin-bottom:12px;" id="modal-clause-title">
        Policy Clause Evidence Inspector
      </h3>
      <div style="background:var(--gray); border:3px solid var(--black); border-radius:8px; padding:18px; margin-bottom:18px; font-size:0.95rem; line-height:1.6;" id="modal-clause-text">
        "Knee replacement surgery is covered as a medically necessary procedure under Section 4.2 of the policy wording."
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; font-weight:600;">
        <span>Document Verification: <strong>Verified Original OCR Stream</strong></span>
        <button class="touch-button" onclick="closeClauseModal()">Got It</button>
      </div>
    </div>
  </div>

  <!-- Plan Selection / Checkout Modal -->
  <div class="modal-backdrop" id="plan-modal" onclick="closePlanModal(event)">
    <div class="modal-panel" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closePlanModal()">&times;</button>
      <div class="section-eyebrow" id="plan-modal-badge">Plan Selected</div>
      <h3 style="font-size:1.6rem; font-weight:700; margin-bottom:10px;" id="plan-modal-title">
        Start Pro Member Trial
      </h3>
      <p style="font-size:0.95rem; margin-bottom:18px;" id="plan-modal-desc">
        Unlock unlimited policy uploads, detailed treatment cost projections, and PDF export reports.
      </p>
      
      <div style="background:var(--lime); border:3px solid var(--black); border-radius:8px; padding:16px; margin-bottom:18px; font-weight:700;">
        ✨ 14-Day Free Access • No credit card required to test • Instant activation
      </div>

      <div class="form-group" style="margin-bottom:14px;">
        <label>Your Email Address</label>
        <input type="email" class="form-control" id="plan-email-input" placeholder="you@company.com" value="sarthak@example.com">
      </div>

      <button class="cta-button" style="width:100%;" onclick="confirmPlanSubscription()">
        Confirm & Start Access Now →
      </button>
    </div>
  </div>

  <!-- ==========================================================================
       JAVASCRIPT LOGIC
       ========================================================================== -->
  <script>
    /* ==========================================================================
       SAMPLE POLICIES DATABASE
       ========================================================================== */
    const SAMPLE_POLICIES = {
      star: {
        id: "star",
        insurer: "Star Health Insurance",
        policy_name: "Star Comprehensive Insurance Policy",
        sum_insured: 500000,
        policy_period: "1 year",
        waiting_periods: {
          initial: "30 days",
          pre_existing: "36 months",
          specific_diseases: "24 months"
        },
        room_rent_limit: "1% of Sum Insured per day (₹5,000)",
        icu_limit: "2% of Sum Insured per day (₹10,000)",
        co_payment: "10% for age 60+",
        sub_limits: {
          cataract: "₹25,000 per eye",
          knee_replacement: "No sub-limit",
          dialysis: "No sub-limit"
        },
        tag: "₹5L Cover",
        short_desc: "Waiting: 36m PED • Room: 1% SI"
      },
      royal: {
        id: "royal",
        insurer: "Royal Sundaram General Insurance",
        policy_name: "Lifeline Supreme Health Plan",
        sum_insured: 1000000,
        policy_period: "1 year",
        waiting_periods: {
          initial: "30 days",
          pre_existing: "24 months",
          specific_diseases: "24 months"
        },
        room_rent_limit: "Single Standard A/C Room (No capping)",
        icu_limit: "No ICU capping",
        co_payment: "0% (Nil co-payment across ages)",
        sub_limits: {
          cataract: "₹50,000 per eye",
          knee_replacement: "No sub-limit",
          dialysis: "Up to Sum Insured"
        },
        tag: "₹10L Cover",
        short_desc: "Waiting: 24m PED • Single A/C Room"
      },
      hdfc: {
        id: "hdfc",
        insurer: "HDFC ERGO General Insurance",
        policy_name: "Optima Restore Health Insurance",
        sum_insured: 500000,
        policy_period: "1 year (Restore Active)",
        waiting_periods: {
          initial: "30 days",
          pre_existing: "36 months",
          specific_diseases: "24 months"
        },
        room_rent_limit: "Any Room except Suite",
        icu_limit: "No sub-limit",
        co_payment: "Nil Co-pay",
        sub_limits: {
          cataract: "No sub-limit (Actuals)",
          knee_replacement: "No sub-limit",
          dialysis: "No sub-limit"
        },
        tag: "₹5L Restore",
        short_desc: "100% Restore Benefit • Any Room"
      }
    };

    let currentPolicy = SAMPLE_POLICIES.star;

    /* ==========================================================================
       THEME TOGGLE
       ========================================================================== */
    function setupThemeToggle() {
      const toggle = document.getElementById('theme-btn');
      const body = document.body;
      
      const saved = localStorage.getItem('insurix-theme');
      if (saved === 'dark') {
        body.classList.add('dark');
        toggle.textContent = 'LT';
        toggle.setAttribute('aria-pressed', 'true');
      }
      
      toggle.addEventListener('click', () => {
        body.classList.toggle('dark');
        const isDark = body.classList.contains('dark');
        toggle.textContent = isDark ? 'LT' : 'DK';
        toggle.setAttribute('aria-pressed', isDark);
        localStorage.setItem('insurix-theme', isDark ? 'dark' : 'light');
        showToast(isDark ? 'Dark theme enabled' : 'Light theme enabled');
      });
    }

    /* ==========================================================================
       VIEW ROUTING & NAVIGATION
       ========================================================================== */
    function navigateTo(viewId) {
      // Hide all view sections
      document.querySelectorAll('.view-section').forEach(sec => {
        sec.classList.remove('active-view');
      });

      // Show selected section
      const targetSec = document.getElementById(`view-${viewId}`);
      if (targetSec) {
        targetSec.classList.add('active-view');
      }

      // Update navbar links
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('data-view') === viewId) {
          link.classList.add('active');
        }
      });

      // Update URL hash
      if (window.location.hash !== `#${viewId}`) {
        window.history.pushState(null, null, `#${viewId}`);
      }

      // Scroll to top
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Handle hash change on popstate / direct link
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '') || 'home';
      navigateTo(hash);
    });

    function toggleMobileMenu() {
      const drawer = document.getElementById('mobile-drawer');
      drawer.classList.toggle('open');
    }

    function closeMobileMenu() {
      const drawer = document.getElementById('mobile-drawer');
      drawer.classList.remove('open');
    }

    /* ==========================================================================
       SAMPLE POLICY SELECTION & UPDATES
       ========================================================================== */
    function loadSamplePolicy(key) {
      if (!SAMPLE_POLICIES[key]) return;
      currentPolicy = SAMPLE_POLICIES[key];

      // Update buttons
      document.querySelectorAll('.sample-btn').forEach(btn => btn.classList.remove('selected'));
      const heroBtns = document.querySelectorAll('.sample-pill-grid .sample-btn');
      if (key === 'star' && heroBtns[0]) heroBtns[0].classList.add('selected');
      if (key === 'royal' && heroBtns[1]) heroBtns[1].classList.add('selected');
      if (key === 'hdfc' && heroBtns[2]) heroBtns[2].classList.add('selected');

      const sideStar = document.getElementById('sample-btn-star');
      const sideRoyal = document.getElementById('sample-btn-royal');
      const sideHdfc = document.getElementById('sample-btn-hdfc');
      if (sideStar && key === 'star') sideStar.classList.add('selected');
      if (sideRoyal && key === 'royal') sideRoyal.classList.add('selected');
      if (sideHdfc && key === 'hdfc') sideHdfc.classList.add('selected');

      // Update strips and tables
      const heroStrip = document.getElementById('hero-active-strip');
      if (heroStrip) {
        heroStrip.innerHTML = `<span>Active: <strong>${currentPolicy.policy_name}</strong></span><span>${currentPolicy.short_desc}</span>`;
      }

      const landingBadge = document.getElementById('landing-loaded-policy-badge');
      if (landingBadge) {
        landingBadge.textContent = `Policy: ${currentPolicy.policy_name} (${currentPolicy.tag})`;
      }

      // Update sidebar spec table
      const specInsurer = document.getElementById('spec-insurer');
      if (specInsurer) {
        document.getElementById('active-policy-title').textContent = currentPolicy.policy_name;
        document.getElementById('spec-insurer').textContent = currentPolicy.insurer;
        document.getElementById('spec-sum').textContent = `₹${currentPolicy.sum_insured.toLocaleString()}`;
        document.getElementById('spec-wait-init').textContent = currentPolicy.waiting_periods.initial;
        document.getElementById('spec-wait-ped').textContent = currentPolicy.waiting_periods.pre_existing;
        document.getElementById('spec-wait-spec').textContent = currentPolicy.waiting_periods.specific_diseases;
        document.getElementById('spec-room').textContent = currentPolicy.room_rent_limit;
        document.getElementById('spec-icu').textContent = currentPolicy.icu_limit;
        document.getElementById('spec-copay').textContent = currentPolicy.co_payment;
        document.getElementById('spec-cataract').textContent = currentPolicy.sub_limits.cataract;
        document.getElementById('spec-knee').textContent = currentPolicy.sub_limits.knee_replacement;
      }

      showToast(`Loaded: ${currentPolicy.policy_name}`);
    }

    /* ==========================================================================
       FILE UPLOAD SIMULATION & DRAG-AND-DROP
       ========================================================================== */
    function triggerFileInput(id) {
      const input = document.getElementById(id);
      if (input) input.click();
    }

    function setupDragAndDrop() {
      const dropZones = document.querySelectorAll('.upload-zone');
      dropZones.forEach(zone => {
        ['dragenter', 'dragover'].forEach(eventName => {
          zone.addEventListener(eventName, (e) => {
            e.preventDefault();
            zone.classList.add('dragover');
          });
        });

        ['dragleave', 'drop'].forEach(eventName => {
          zone.addEventListener(eventName, (e) => {
            e.preventDefault();
            zone.classList.remove('dragover');
          });
        });

        zone.addEventListener('drop', (e) => {
          const files = e.dataTransfer.files;
          if (files.length > 0) {
            simulateUpload(files[0].name);
          }
        });
      });
    }

    function handleFileSelected(e) {
      if (e.target.files && e.target.files.length > 0) {
        simulateUpload(e.target.files[0].name);
      }
    }

    function simulateUpload(filename) {
      const zones = document.querySelectorAll('.upload-zone');
      zones.forEach(zone => {
        zone.classList.add('processing');
        zone.innerHTML = `
          <div style="display:flex; flex-direction:column; align-items:center; gap:8px;">
            <div style="width:28px; height:28px; border:4px solid var(--black); border-top-color:transparent; border-radius:50%; animation:spin 0.8s linear infinite;"></div>
            <strong>Analyzing ${filename}...</strong>
            <span style="font-size:0.75rem;">Extracting OCR clauses & table sub-limits...</span>
          </div>
        `;
      });

      setTimeout(() => {
        zones.forEach(zone => {
          zone.classList.remove('processing');
          zone.innerHTML = `
            <svg class="upload-icon" style="width:36px; height:36px; margin-bottom:6px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <div style="font-size:0.95rem; font-weight:700;">${filename} Ingested!</div>
            <div style="font-size:0.75rem;">42 Clauses extracted • Ready to query</div>
          `;
        });
        showToast(`Document "${filename}" parsed successfully!`);
        navigateTo('demo');
      }, 1600);
    }

    /* ==========================================================================
       CHAT INTERACTION LOGIC (Hero & Demo)
       ========================================================================== */
    function askPresetQuestion(context, question) {
      const input = document.getElementById(`${context}-chat-input`);
      if (input) {
        input.value = question;
        sendChatQuery(context);
      }
    }

    function handleChatEnter(e, context) {
      if (e.key === 'Enter') {
        sendChatQuery(context);
      }
    }

    function sendChatQuery(context) {
      const input = document.getElementById(`${context}-chat-input`);
      const container = document.getElementById(`${context}-chat-container`);
      const question = input.value.trim();
      if (!question) return;

      // Append User message
      const userDiv = document.createElement('div');
      userDiv.className = 'chat-message user';
      userDiv.textContent = question;
      container.appendChild(userDiv);
      input.value = '';
      container.scrollTop = container.scrollHeight;

      // Show Typing indicator
      const typingDiv = document.createElement('div');
      typingDiv.className = 'typing-indicator';
      typingDiv.id = `typing-${context}`;
      typingDiv.innerHTML = `
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span style="font-size:0.8rem; font-weight:700; margin-left:4px;">Scanning Policy Clauses...</span>
      `;
      container.appendChild(typingDiv);
      container.scrollTop = container.scrollHeight;

      setTimeout(() => {
        // Remove typing
        const t = document.getElementById(`typing-${context}`);
        if (t) t.remove();

        // Generate response based on question keywords & currentPolicy
        const replyData = generatePolicyResponse(question, currentPolicy);
        appendAssistantMessage(container, replyData);
      }, 950);
    }

    function generatePolicyResponse(query, policy) {
      const q = query.toLowerCase();

      // Knee replacement
      if (q.includes('knee') || q.includes('joint') || q.includes('arthroplasty')) {
        return {
          answer: `Yes, Total Knee Replacement is covered under your ${policy.policy_name} as a medically necessary surgery subject to waiting period criteria.`,
          evidence: [
            { page: 18, section: "4.2", text: "Knee replacement surgery is covered as a medically necessary procedure under Section 4.2 of the policy." },
            { page: 12, section: "5.1", text: "Waiting period of 36 months applies for pre-existing conditions and their direct complications." }
          ],
          cost_estimate: {
            total_cost: 280000,
            potentially_covered: 210000,
            deductible: 20000,
            co_payment: 21000,
            out_of_pocket: 70000
          },
          uncertainty: {
            confidence: "medium",
            missing_info: [
              "Exact sub-limit for knee replacement not explicitly stated",
              "Hospital category (network/non-network) not specified",
              "Waiting period completion status unknown"
            ],
            recommendation: "Please verify: 1) Waiting period served (>24/36 months), 2) In-network hospital cashless pre-auth submitted."
          }
        };
      }

      // Room rent / ICU
      if (q.includes('room') || q.includes('rent') || q.includes('icu') || q.includes('deluxe') || q.includes('suite')) {
        return {
          answer: `Under ${policy.policy_name}, your room rent limit is strictly capped at ${policy.room_rent_limit} and ICU limit is ${policy.icu_limit}. If you select a room category above this limit, proportionate deduction penalties apply across all doctor visits, nursing, and operation theatre fees.`,
          evidence: [
            { page: 14, section: "3.8", text: "If the insured person occupies a room with room rent higher than the entitled limit, the insurer shall bear all associated medical expenses proportionately." },
            { page: 15, section: "3.9", text: "ICU charges covered up to specified daily capping without proportionate deduction on doctor fees." }
          ],
          cost_estimate: {
            total_cost: 150000,
            potentially_covered: 105000,
            deductible: 10000,
            co_payment: 0,
            out_of_pocket: 35000
          },
          uncertainty: {
            confidence: "high",
            missing_info: ["Choice of single standard vs deluxe suite room tier."],
            recommendation: "Always choose a 'Single Standard A/C Room' or within 1% SI limit (₹5,000/day) to prevent the hospital billing penalty."
          }
        };
      }

      // Cataract
      if (q.includes('cataract') || q.includes('eye') || q.includes('lens')) {
        return {
          answer: `Cataract surgery is covered under ${policy.policy_name}, subject to a disease-specific sub-limit of ${policy.sub_limits.cataract} and a standard 24-month waiting period.`,
          evidence: [
            { page: 22, section: "6.3", text: `Coverage for cataract surgery is limited to a maximum of ${policy.sub_limits.cataract} inclusive of cost of intraocular lens.` },
            { page: 11, section: "2.4", text: "Specific illness waiting period of 24 consecutive months of continuous coverage applies for cataract." }
          ],
          cost_estimate: {
            total_cost: 45000,
            potentially_covered: 25000,
            deductible: 0,
            co_payment: 2500,
            out_of_pocket: 17500
          },
          uncertainty: {
            confidence: "high",
            missing_info: ["Type of lens selected (Monofocal covered vs Premium Multifocal out-of-pocket difference)."],
            recommendation: "Ensure in-network cashless admission and verify whether your surgeon's lens is standard monofocal."
          }
        };
      }

      // Waiting periods
      if (q.includes('waiting') || q.includes('pre-existing') || q.includes('ped') || q.includes('diabetes') || q.includes('hypertension')) {
        return {
          answer: `For ${policy.policy_name}, standard waiting periods apply: Initial 30 days (all illnesses except accident), 24 months for specified surgeries (cataract, hernia, joint replacements), and ${policy.waiting_periods.pre_existing} for Pre-Existing Diseases (PED).`,
          evidence: [
            { page: 11, section: "5.1", text: `Pre-existing disease coverage commences after ${policy.waiting_periods.pre_existing} of continuous policy renewals with no break in insurance.` },
            { page: 10, section: "5.0", text: "A 30-day waiting period from inception applies for all medical treatments other than accidental injury." }
          ],
          uncertainty: {
            confidence: "high",
            missing_info: ["Exact date of inception of your initial health policy."],
            recommendation: "Portability credits from previous insurers can be applied to waive this waiting period."
          }
        };
      }

      // Senior citizen / Copay
      if (q.includes('copay') || q.includes('co-pay') || q.includes('senior') || q.includes('60')) {
        return {
          answer: `Your ${policy.policy_name} specifies co-payment rules: "${policy.co_payment}". Where co-pay applies, you must pay this fixed percentage on all admissible claim items.`,
          evidence: [
            { page: 16, section: "5.4", text: `A co-payment of ${policy.co_payment} shall be borne by the insured person for each and every admissible claim.` }
          ],
          uncertainty: {
            confidence: "high",
            missing_info: ["Age of the insured patient undergoing treatment."],
            recommendation: "Check if voluntary co-payment was opted at policy issuance for a premium discount."
          }
        };
      }

      // Generic smart fallback
      return {
        answer: `Under ${policy.policy_name} (Sum Insured ₹${policy.sum_insured.toLocaleString()}), treatments for "${query}" are evaluated against Section 4 (In-patient hospitalization) and Section 6 (Specific Sub-limits).`,
        evidence: [
          { page: 8, section: "4.1", text: "Medically necessary in-patient hospitalization exceeding 24 hours is admissible up to the available Sum Insured." },
          { page: 26, section: "8.2", text: "Non-medical consumables, convenience charges, and luxury amenities are excluded under IRDAI guidelines." }
        ],
        cost_estimate: {
          total_cost: 95000,
          potentially_covered: 76000,
          deductible: 5000,
          co_payment: 0,
          out_of_pocket: 14000
        },
        uncertainty: {
          confidence: "medium",
          missing_info: ["Clinical breakdown of pharmacy vs surgeon charges", "Network hospital empanelment status"],
          recommendation: "Request an itemized estimate from your hospital billing desk to confirm exact covered vs non-covered items."
        }
      };
    }

    function appendAssistantMessage(container, data) {
      const messageDiv = document.createElement('div');
      messageDiv.className = 'chat-message assistant';
      
      let html = `<div class="message-text">${data.answer}</div>`;
      
      // Evidence citations
      if (data.evidence && data.evidence.length > 0) {
        html += '<div class="evidence-list">';
        data.evidence.forEach(ev => {
          html += `
            <div class="evidence-citation" onclick="openClauseModal('Section ${ev.section}', ${ev.page}, '${escapeQuote(ev.text)}')">
              <span class="source-badge">Page ${ev.page}, §${ev.section}</span>
              <span>"${ev.text}"</span>
            </div>
          `;
        });
        html += '</div>';
      }
      
      // Cost breakdown
      if (data.cost_estimate) {
        html += `
          <table class="cost-table">
            <thead>
              <tr><th>Financial Component</th><th>Amount</th></tr>
            </thead>
            <tbody>
              <tr><td>Total Treatment Cost</td><td>₹${data.cost_estimate.total_cost.toLocaleString()}</td></tr>
              <tr><td>Potentially Covered</td><td>₹${data.cost_estimate.potentially_covered.toLocaleString()}</td></tr>
              <tr><td>Deductible Applied</td><td>₹${data.cost_estimate.deductible.toLocaleString()}</td></tr>
              <tr><td>Co-payment Liability</td><td>₹${data.cost_estimate.co_payment.toLocaleString()}</td></tr>
              <tr class="total-row"><td><strong>Estimated Out-of-Pocket</strong></td><td><strong>₹${data.cost_estimate.out_of_pocket.toLocaleString()}</strong></td></tr>
            </tbody>
          </table>
        `;
      }
      
      // Confidence & Uncertainty
      if (data.uncertainty) {
        const conf = data.uncertainty.confidence || 'medium';
        const icon = conf === 'high' ? '✓' : '⚠';
        html += `
          <div>
            <div class="confidence-badge ${conf}">
              ${icon} ${conf.charAt(0).toUpperCase() + conf.slice(1)} Confidence
            </div>
          </div>
        `;
        
        if (data.uncertainty.missing_info && data.uncertainty.missing_info.length > 0) {
          html += '<div class="missing-info-box"><strong>Ambiguity Flags & Missing Information:</strong><ul>';
          data.uncertainty.missing_info.forEach(info => {
            html += `<li>${info}</li>`;
          });
          if (data.uncertainty.recommendation) {
            html += `<li style="margin-top:4px;"><strong>Advice:</strong> ${data.uncertainty.recommendation}</li>`;
          }
          html += '</ul></div>';
        }
      }
      
      messageDiv.innerHTML = html;
      container.appendChild(messageDiv);
      container.scrollTop = container.scrollHeight;
    }

    function escapeQuote(str) {
      return str.replace(/'/g, "\\'").replace(/"/g, '&quot;');
    }

    /* ==========================================================================
       DEMO STUDIO TABS (Chat vs Calculator)
       ========================================================================== */
    function switchDemoTab(tab) {
      const btnChat = document.getElementById('tab-btn-chat');
      const btnCalc = document.getElementById('tab-btn-calc');
      const viewChat = document.getElementById('demo-chat-view');
      const viewCalc = document.getElementById('demo-calc-view');

      if (tab === 'chat') {
        btnChat.classList.add('active');
        btnCalc.classList.remove('active');
        viewChat.style.display = 'block';
        viewCalc.style.display = 'none';
      } else {
        btnCalc.classList.add('active');
        btnChat.classList.remove('active');
        viewCalc.style.display = 'block';
        viewChat.style.display = 'none';
      }
    }

    /* ==========================================================================
       TREATMENT CALCULATOR ENGINE
       ========================================================================== */
    const TREATMENT_DEFAULTS = {
      knee_replacement: { bill: 280000 },
      cataract: { bill: 45000 },
      appendectomy: { bill: 65000 },
      cabg: { bill: 380000 },
      dialysis: { bill: 3500 }
    };

    function updateTreatmentDefaults() {
      const select = document.getElementById('calc-treatment-select');
      const billInput = document.getElementById('calc-bill-amount');
      const val = select.value;
      if (TREATMENT_DEFAULTS[val]) {
        billInput.value = TREATMENT_DEFAULTS[val].bill;
      }
      runTreatmentCalculation();
    }

    function runTreatmentCalculation() {
      const treatment = document.getElementById('calc-treatment-select').value;
      const totalBill = parseFloat(document.getElementById('calc-bill-amount').value) || 0;
      const hospitalType = document.getElementById('calc-hospital-type').value;
      const roomType = document.getElementById('calc-room-type').value;
      const age = parseInt(document.getElementById('calc-patient-age').value) || 45;
      const waitingStatus = document.getElementById('calc-waiting-status').value;

      let roomPenalty = 0;
      let copayPercent = 0;
      let nonMedical = Math.round(totalBill * 0.08); // 8% consumables
      let customaryDeduction = hospitalType === 'non_network' ? Math.round(totalBill * 0.12) : 0;
      let deductible = 0;

      // Room penalty calculation
      if (roomType === 'exceeds_deluxe') {
        roomPenalty = Math.round(totalBill * 0.22); // 22% proportional deduction
      } else if (roomType === 'suite') {
        roomPenalty = Math.round(totalBill * 0.38); // 38% heavy penalty
      }

      // Copay rule based on policy
      if (currentPolicy.id === 'star' && age >= 60) {
        copayPercent = 0.10;
      }

      // Waiting period check
      if (waitingStatus === 'partial') {
        // Disallow pre-existing joint/chronic
        if (treatment === 'knee_replacement' || treatment === 'cataract') {
          document.getElementById('res-total-bill').textContent = `₹${totalBill.toLocaleString()}`;
          document.getElementById('res-insurer-pays').textContent = '₹0';
          document.getElementById('res-you-pay').textContent = `₹${totalBill.toLocaleString()}`;

          document.getElementById('calc-breakdown-tbody').innerHTML = `
            <tr style="background:var(--pink);">
              <td><strong>Claim Disallowed</strong></td>
              <td>₹${totalBill.toLocaleString()}</td>
              <td><strong>Waiting Period Unmet (Clause 5.1):</strong> Pre-existing condition waiting period requires 24-36 continuous active months.</td>
            </tr>
          `;
          return;
        }
      }

      // Sub-limit cappings
      let subLimitCap = 0;
      if (treatment === 'cataract' && currentPolicy.id === 'star') {
        subLimitCap = 25000;
      }

      let allowableBase = totalBill - roomPenalty - nonMedical - customaryDeduction;
      if (subLimitCap > 0 && allowableBase > subLimitCap) {
        allowableBase = subLimitCap;
      }
      if (allowableBase < 0) allowableBase = 0;

      let copayAmount = Math.round(allowableBase * copayPercent);
      let insurerPays = allowableBase - copayAmount;
      if (insurerPays > currentPolicy.sum_insured) {
        insurerPays = currentPolicy.sum_insured;
      }

      let youPay = totalBill - insurerPays;
      if (youPay < 0) youPay = 0;

      // Update UI
      document.getElementById('res-total-bill').textContent = `₹${totalBill.toLocaleString()}`;
      document.getElementById('res-insurer-pays').textContent = `₹${insurerPays.toLocaleString()}`;
      document.getElementById('res-you-pay').textContent = `₹${youPay.toLocaleString()}`;

      // Build breakdown table rows
      let rowsHtml = `
        <tr><td>Hospital Bill Base</td><td>₹${totalBill.toLocaleString()}</td><td>Itemized hospital tariff</td></tr>
      `;

      if (roomPenalty > 0) {
        rowsHtml += `
          <tr style="background:var(--pink);">
            <td>Room Rent Proportionate Penalty</td>
            <td>-₹${roomPenalty.toLocaleString()}</td>
            <td>Exceeded 1% SI (₹5,000/day) - Proportional reduction applied to fees</td>
          </tr>
        `;
      }

      if (customaryDeduction > 0) {
        rowsHtml += `
          <tr style="background:var(--pink);">
            <td>Non-Network Customary Disallowance</td>
            <td>-₹${customaryDeduction.toLocaleString()}</td>
            <td>Non-network hospital rates exceed insurer reasonable tariff by 12%</td>
          </tr>
        `;
      }

      rowsHtml += `
        <tr><td>Consumables & Gloves (Non-Medical)</td><td>-₹${nonMedical.toLocaleString()}</td><td>IRDAI Non-Payables Annexure I exclusions</td></tr>
      `;

      if (copayAmount > 0) {
        rowsHtml += `
          <tr style="background:var(--pink);">
            <td>Co-Payment (${copayPercent * 100}%)</td>
            <td>-₹${copayAmount.toLocaleString()}</td>
            <td>Clause 5.4: Age ${age} triggered senior co-pay requirement</td>
          </tr>
        `;
      }

      if (subLimitCap > 0) {
        rowsHtml += `
          <tr><td>Disease Sub-Limit Cap</td><td>₹${subLimitCap.toLocaleString()} max</td><td>Cataract capped at ₹25,000 per eye</td></tr>
        `;
      }

      rowsHtml += `
        <tr class="total-row">
          <td><strong>Estimated Patient Out-of-Pocket</strong></td>
          <td><strong>₹${youPay.toLocaleString()}</strong></td>
          <td><strong>Net Insurer Coverage: ₹${insurerPays.toLocaleString()}</strong></td>
        </tr>
      `;

      document.getElementById('calc-breakdown-tbody').innerHTML = rowsHtml;
      showToast('Calculated out-of-pocket projection');
    }

    /* ==========================================================================
       ACCORDION (FAQ)
       ========================================================================== */
    function toggleAccordion(toggleBtn) {
      const item = toggleBtn.closest('.accordion-item');
      const body = item.querySelector('.accordion-body');
      const icon = toggleBtn.querySelector('.accordion-icon');
      const isOpen = item.classList.contains('open');

      // Close all other open accordions
      document.querySelectorAll('.accordion-item.open').forEach(openItem => {
        if (openItem !== item) {
          openItem.classList.remove('open');
          openItem.querySelector('.accordion-body').style.maxHeight = '0';
          openItem.querySelector('.accordion-icon').textContent = '+';
        }
      });

      // Toggle clicked
      if (isOpen) {
        item.classList.remove('open');
        body.style.maxHeight = '0';
        icon.textContent = '+';
      } else {
        item.classList.add('open');
        body.style.maxHeight = `${body.scrollHeight + 30}px`;
        icon.textContent = '-';
      }
    }

    /* ==========================================================================
       PRICING BILLING TOGGLE
       ========================================================================== */
    function setBilling(mode) {
      const btnMonthly = document.getElementById('billing-btn-monthly');
      const btnAnnual = document.getElementById('billing-btn-annual');
      const pricePro = document.getElementById('price-pro');
      const periodPro = document.getElementById('period-pro');

      if (mode === 'monthly') {
        btnMonthly.classList.add('active');
        btnAnnual.classList.remove('active');
        pricePro.textContent = '₹499';
        periodPro.textContent = '/ month';
      } else {
        btnAnnual.classList.add('active');
        btnMonthly.classList.remove('active');
        pricePro.textContent = '₹349';
        periodPro.textContent = '/ month (billed ₹4,188/yr)';
      }
    }

    /* ==========================================================================
       MODAL CONTROLS
       ========================================================================== */
    function openClauseModal(section, page, text) {
      document.getElementById('modal-clause-badge').textContent = `Page ${page}, ${section}`;
      document.getElementById('modal-clause-title').textContent = `Policy Clause Evidence: ${section}`;
      document.getElementById('modal-clause-text').textContent = text;
      document.getElementById('clause-modal').classList.add('open');
    }

    function closeClauseModal(e) {
      if (!e || e.target.id === 'clause-modal' || e.target.classList.contains('modal-close') || e.target.tagName === 'BUTTON') {
        document.getElementById('clause-modal').classList.remove('open');
      }
    }

    function viewRawPolicyModal() {
      openClauseModal(
        'Section 4.1 to 6.2 Master Schedule',
        1,
        `Insurer: ${currentPolicy.insurer}\nPolicy: ${currentPolicy.policy_name}\nSum Insured: ₹${currentPolicy.sum_insured.toLocaleString()}\nRoom Limit: ${currentPolicy.room_rent_limit}\nICU Limit: ${currentPolicy.icu_limit}\nWaiting Periods: Initial ${currentPolicy.waiting_periods.initial}, Pre-Existing ${currentPolicy.waiting_periods.pre_existing}\nCo-payment: ${currentPolicy.co_payment}`
      );
    }

    function openPlanModal(planName) {
      document.getElementById('plan-modal-badge').textContent = `${planName.toUpperCase()} PLAN`;
      document.getElementById('plan-modal-title').textContent = `Select ${planName} Plan`;
      document.getElementById('plan-modal-desc').textContent = `You are selecting the ${planName} subscription tier for Insurix Policy Intelligence.`;
      document.getElementById('plan-modal').classList.add('open');
    }

    function closePlanModal(e) {
      if (!e || e.target.id === 'plan-modal' || e.target.classList.contains('modal-close')) {
        document.getElementById('plan-modal').classList.remove('open');
      }
    }

    function confirmPlanSubscription() {
      const email = document.getElementById('plan-email-input').value;
      closePlanModal();
      showToast(`Subscription activated for ${email}!`);
      navigateTo('demo');
    }

    /* ==========================================================================
       CONTACT FORM
       ========================================================================== */
    function handleContactSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('contact-name').value;
      showToast(`Thank you ${name}! Our policy specialist will contact you shortly.`);
      e.target.reset();
    }

    /* ==========================================================================
       TOAST NOTIFICATION SYSTEM
       ========================================================================== */
    function showToast(message) {
      // Remove old
      const old = document.querySelector('.toast-box');
      if (old) old.remove();

      const toast = document.createElement('div');
      toast.className = 'toast-box';
      toast.innerHTML = `
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        <span>${message}</span>
      `;
      document.body.appendChild(toast);

      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 350);
      }, 3200);
    }

    /* ==========================================================================
       CURSOR TRAIL (Desktop fine pointer only)
       ========================================================================== */
    function setupCursorTrail() {
      if (window.matchMedia('(pointer: fine)').matches) {
        const trail = [];
        const trailLength = 5;
        
        for (let i = 0; i < trailLength; i++) {
          const dot = document.createElement('div');
          dot.className = 'cursor-trail-dot';
          dot.style.cssText = `
            position: fixed;
            width: ${18 - i * 2}px;
            height: ${18 - i * 2}px;
            border: 3px solid var(--black);
            background: ${i % 2 === 0 ? 'var(--lime)' : 'var(--pink)'};
            box-shadow: 4px 4px 0 var(--black);
            border-radius: 999px;
            pointer-events: none;
            z-index: 9999;
            transition: transform 100ms ease;
            top: 0;
            left: 0;
          `;
          document.body.appendChild(dot);
          trail.push({ el: dot, x: -100, y: -100 });
        }
        
        let mouseX = -100, mouseY = -100;
        
        document.addEventListener('pointermove', (e) => {
          mouseX = e.clientX;
          mouseY = e.clientY;
        });
        
        function animate() {
          trail.forEach((dot, i) => {
            const leader = i === 0 ? { x: mouseX, y: mouseY } : trail[i - 1];
            dot.x += (leader.x - dot.x) * 0.3;
            dot.y += (leader.y - dot.y) * 0.3;
            dot.el.style.transform = `translate(${dot.x}px, ${dot.y}px) translate(-50%, -50%)`;
          });
          requestAnimationFrame(animate);
        }
        
        animate();
      }
    }

    /* ==========================================================================
       INITIALIZATION
       ========================================================================== */
    document.addEventListener('DOMContentLoaded', () => {
      setupThemeToggle();
      setupDragAndDrop();
      setupCursorTrail();

      // Mobile button listener
      const mobBtn = document.getElementById('mobile-toggle');
      if (mobBtn) {
        mobBtn.addEventListener('click', toggleMobileMenu);
      }

      // Check URL hash for initial route
      const hash = window.location.hash.replace('#', '') || 'home';
      navigateTo(hash);

      // Run initial treatment calculation
      runTreatmentCalculation();
    });
  </script>
</body>
</html>
'''

with open("/Users/sarthak/Desktop/Insurix/index.html", "w") as f:
    f.write(html_content.strip())

print("Created /Users/sarthak/Desktop/Insurix/index.html successfully!")
