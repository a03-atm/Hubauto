[Hubauto.py](https://github.com/user-attachments/files/26307107/Hubauto.py)
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Hub Auto — Expert Automobile | Aide à la décision</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,700&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html {
  scroll-behavior: smooth;
}

/* ========== THÈME NOIR ET ROUGE ========== */
:root {
  --bg-primary: #0a0a0c;
  --bg-secondary: #111113;
  --bg-card: #151517;
  --border-subtle: #222427;
  --text-primary: #ffffff;
  --text-secondary: #b3b7c0;
  --text-muted: #6f7480;
  --accent: #e33b2c;
  --accent-dark: #b92c1f;
  --accent-glow: rgba(227, 59, 44, 0.2);
  --shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
  --serif: 'Cormorant Garamond', Georgia, serif;
  --sans: 'DM Sans', system-ui, sans-serif;
}

body {
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--sans);
  font-weight: 300;
  overflow-x: hidden;
  line-height: 1.5;
}

.page {
  display: none;
}
.page.active {
  display: block;
  animation: fadeUp 0.45s ease both;
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: none; }
}

/* ========== NAVIGATION ========== */
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 300;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 56px;
  background: rgba(10, 10, 12, 0.94);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.logo {
  font-family: var(--sans);
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--text-primary);
  cursor: pointer;
}
.logo em {
  font-style: normal;
  color: var(--accent);
}
.nav-r {
  display: flex;
  align-items: center;
  gap: 40px;
}
.nl {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-secondary);
  cursor: pointer;
  transition: 0.2s;
  text-decoration: none;
}
.nl:hover {
  color: var(--accent);
}
.nav-cta {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  background: var(--accent);
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 0;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
  display: inline-block;
}
.nav-cta:hover {
  background: var(--accent-dark);
}

/* ========== HERO AVEC PHOTO BMW ========== */
.hero {
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.hero-bg {
  position: absolute;
  inset: 0;
  background-image: url('https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=2000&q=90');
  background-size: cover;
  background-position: center 35%;
  z-index: 0;
  transform: scale(1.02);
  animation: slowZoom 14s ease-out forwards;
}
@keyframes slowZoom {
  from { transform: scale(1.08); }
  to { transform: scale(1); }
}
.hero-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(95deg, #0a0a0c 0%, rgba(0, 0, 0, 0.7) 50%, rgba(0, 0, 0, 0.3) 100%);
  z-index: 1;
}
.hero-bg::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 280px;
  background: linear-gradient(to top, #0a0a0c, transparent);
  z-index: 1;
}

.hero-inner {
  position: relative;
  z-index: 20;
  padding: 68px 56px 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 720px;
}
.hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 2rem;
  animation: fadeUp 0.6s ease 0.1s both;
}
.hero-eyebrow::before {
  content: '';
  display: block;
  width: 44px;
  height: 1.5px;
  background: var(--accent);
}
.hero-h1 {
  font-family: var(--serif);
  font-size: clamp(54px, 8.5vw, 108px);
  font-weight: 400;
  line-height: 0.95;
  letter-spacing: -1px;
  color: white;
  margin-bottom: 2rem;
  animation: fadeUp 0.6s ease 0.2s both;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
}
.hero-h1 .r {
  color: var(--accent);
  font-style: italic;
}
.hero-sub {
  font-size: 17px;
  font-weight: 300;
  color: #e0e4ed;
  line-height: 1.7;
  max-width: 480px;
  margin-bottom: 3.5rem;
  animation: fadeUp 0.6s ease 0.35s both;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
}

/* Cartes d'action */
.hero-cards {
  display: flex;
  gap: 0;
  animation: fadeUp 0.6s ease 0.5s both;
  max-width: 560px;
}
.hc {
  flex: 1;
  background: rgba(21, 21, 23, 0.9);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2rem 1.8rem;
  cursor: pointer;
  transition: all 0.28s ease;
  display: flex;
  flex-direction: column;
  gap: 10px;
  position: relative;
  overflow: hidden;
}
.hc::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}
.hc:hover::after {
  transform: scaleX(1);
}
.hc:hover {
  background: #1c1c20;
  transform: translateY(-4px);
  box-shadow: var(--shadow);
}
.hc + .hc {
  border-left: none;
}
.hc-tag {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--accent);
}
.hc-title {
  font-family: var(--serif);
  font-size: 28px;
  font-weight: 600;
  color: white;
  line-height: 1.1;
}
.hc-desc {
  font-size: 13px;
  line-height: 1.6;
  color: var(--text-secondary);
}
.hc-cta {
  margin-top: 0.5rem;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 6px;
  transition: gap 0.2s, color 0.2s;
}
.hc:hover .hc-cta {
  gap: 12px;
  color: var(--accent);
}

/* Stats band */
.hero-stats {
  position: relative;
  z-index: 10;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(4px);
}
.hstat {
  padding: 1.4rem 2rem;
  border-right: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  gap: 1rem;
}
.hstat:last-child {
  border-right: none;
}
.hstat-ico {
  font-size: 1rem;
  flex-shrink: 0;
}
.hstat-lbl {
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin-bottom: 0.15rem;
}
.hstat-val {
  font-size: 13px;
  font-weight: 500;
  color: white;
}

/* Section Process */
.proc-sec {
  background: var(--bg-secondary);
  padding: 80px 56px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}
.proc-hd {
  text-align: center;
  margin-bottom: 60px;
}
.proc-badge {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--accent);
  background: rgba(227, 59, 44, 0.12);
  padding: 5px 16px;
  border-radius: 40px;
  margin-bottom: 18px;
}
.proc-hd h2 {
  font-family: var(--serif);
  font-size: clamp(30px, 4vw, 48px);
  font-weight: 400;
  color: white;
  letter-spacing: -0.5px;
}
.proc-hd h2 span {
  color: var(--accent);
  font-style: italic;
}
.proc-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
.proc-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  padding: 2rem 1.6rem;
  transition: all 0.28s;
  position: relative;
  overflow: hidden;
}
.proc-card::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s;
}
.proc-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow);
}
.proc-card:hover::after {
  transform: scaleX(1);
}
.proc-ico {
  width: 52px;
  height: 52px;
  background: var(--bg-primary);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.4rem;
  transition: 0.2s;
}
.proc-card:hover .proc-ico {
  background: var(--accent);
  border-color: var(--accent);
}
.proc-ico svg {
  width: 26px;
  height: 26px;
  stroke: var(--accent);
  stroke-width: 1.5;
  fill: none;
  transition: 0.2s;
}
.proc-card:hover .proc-ico svg {
  stroke: white;
}
.proc-n {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 10px;
}
.proc-card h3 {
  font-family: var(--serif);
  font-size: 22px;
  font-weight: 600;
  color: white;
  margin-bottom: 8px;
  line-height: 1.2;
}
.proc-card p {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.55;
}

/* ========== FORMULAIRES (même structure, couleurs adaptées) ========== */
.fwrap {
  min-height: 100vh;
  padding: 120px 0 80px;
  background: var(--bg-primary);
}
.fc {
  max-width: 1040px;
  margin: 0 auto;
  padding: 0 28px;
}
.fbk {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-secondary);
  background: none;
  border: 1px solid var(--border-subtle);
  padding: 8px 18px;
  margin-bottom: 40px;
  cursor: pointer;
  transition: 0.2s;
  font-family: var(--sans);
}
.fbk:hover {
  border-color: var(--accent);
  color: var(--accent);
}
.fhd {
  margin-bottom: 48px;
}
.fkick {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 3px;
  color: var(--accent);
  margin-bottom: 12px;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 12px;
}
.fkick::before {
  content: '';
  width: 32px;
  height: 1.5px;
  background: var(--accent);
}
.ftit {
  font-family: var(--serif);
  font-size: clamp(44px, 7vw, 80px);
  font-weight: 400;
  line-height: 1;
  color: white;
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}
.ftit strong {
  color: var(--accent);
  font-style: italic;
  font-weight: 400;
}
.fdesc {
  font-size: 15px;
  color: var(--text-secondary);
  max-width: 540px;
  line-height: 1.65;
}

.form-layout {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 28px;
  align-items: start;
}
.fsec {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  padding: 32px 36px;
  margin-bottom: 20px;
}
.fsec-hd {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 26px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-subtle);
}
.fsec-n {
  background: var(--accent);
  font-size: 12px;
  font-weight: 700;
  padding: 5px 14px;
  color: white;
  font-family: var(--sans);
  letter-spacing: 0.5px;
}
.fsec-t {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--text-muted);
}
.fg {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}
.gf {
  grid-column: 1/-1;
}
.fg3 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 18px;
}
.fgrp {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-muted);
}
.req {
  color: var(--accent);
}
input, select, textarea {
  background: var(--bg-primary);
  border: 1px solid var(--border-subtle);
  padding: 12px 16px;
  border-radius: 0;
  font-family: var(--sans);
  font-size: 14px;
  color: white;
  font-weight: 300;
  transition: all 0.2s;
}
input:focus, select:focus, textarea:focus {
  border-color: var(--accent);
  outline: none;
  background: var(--bg-secondary);
  box-shadow: 0 0 0 3px rgba(227, 59, 44, 0.1);
}
.rrow {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}
.rpill input {
  display: none;
}
.rpl {
  background: var(--bg-primary);
  border: 1px solid var(--border-subtle);
  padding: 7px 18px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--text-secondary);
  cursor: pointer;
  transition: 0.2s;
}
.rpill input:checked + .rpl {
  background: var(--accent);
  border-color: var(--accent);
  color: white;
}
.phdrop {
  border: 2px dashed rgba(227, 59, 44, 0.4);
  background: var(--bg-primary);
  padding: 40px;
  text-align: center;
  cursor: pointer;
  transition: 0.2s;
  position: relative;
}
.phdrop:hover {
  border-color: var(--accent);
  background: rgba(227, 59, 44, 0.05);
}
.phdrop input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}
.ph-icon {
  font-size: 28px;
  margin-bottom: 10px;
}
.ph-txt {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.6;
}
.ph-txt b {
  color: var(--accent);
}
.ph-preview {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 16px;
}
.ph-preview img {
  width: 72px;
  height: 72px;
  object-fit: cover;
  border: 1px solid var(--border-subtle);
}

/* Sidebar paiement */
.pay-side {
  position: sticky;
  top: 84px;
}
.pay-card-box {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  overflow: hidden;
  box-shadow: var(--shadow);
}
.pay-card-top {
  background: var(--accent);
  padding: 24px 28px;
}
.pay-card-lbl {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 8px;
}
.pay-card-price {
  font-family: var(--serif);
  font-size: 68px;
  font-weight: 400;
  color: white;
  line-height: 1;
}
.pay-card-price span {
  font-family: var(--sans);
  font-size: 16px;
  color: rgba(255, 255, 255, 0.6);
  font-weight: 300;
}
.pay-card-body {
  padding: 24px 28px;
}
.pay-recap {
  margin-bottom: 20px;
}
.pay-rl {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  padding: 9px 0;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-secondary);
}
.pay-rl:last-child {
  border: none;
}
.pay-rl strong {
  color: white;
  font-weight: 500;
}
.garantie {
  border-left: 3px solid var(--accent);
  padding: 12px 14px;
  background: rgba(227, 59, 44, 0.1);
  margin-bottom: 14px;
  font-size: 12px;
  line-height: 1.65;
  color: var(--text-secondary);
}
.garantie strong {
  display: block;
  font-size: 10px;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: white;
  margin-bottom: 4px;
  font-weight: 700;
}
.btn-pay {
  width: 100%;
  background: var(--accent);
  color: white;
  border: none;
  padding: 16px;
  font-family: var(--serif);
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: background 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
.btn-pay:hover {
  background: var(--accent-dark);
}
.ssl-note {
  text-align: center;
  font-size: 10px;
  color: var(--text-muted);
  margin-top: 8px;
  letter-spacing: 0.08em;
}

/* Page paiement Stripe */
.pwrap {
  min-height: 100vh;
  padding: 120px 24px 80px;
  background: var(--bg-primary);
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pbk {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-secondary);
  background: none;
  border: 1px solid var(--border-subtle);
  padding: 8px 18px;
  margin-bottom: 40px;
  cursor: pointer;
  transition: 0.2s;
  font-family: var(--sans);
  align-self: flex-start;
}
.pbk:hover {
  border-color: var(--accent);
  color: var(--accent);
}
.stripe-card {
  max-width: 720px;
  width: 100%;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  box-shadow: var(--shadow);
  overflow: hidden;
}
.stripe-img {
  height: 200px;
  background: var(--bg-secondary);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
}
.stripe-img-svg {
  width: 100%;
  height: 100%;
  opacity: 0.2;
  position: absolute;
  inset: 0;
}
.stripe-img::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, var(--bg-card), transparent);
}
.stripe-img-txt {
  position: relative;
  z-index: 2;
  padding: 20px 28px;
  font-size: 10px;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.55);
}
.stripe-body {
  padding: 40px 44px;
}
.stripe-kick {
  font-size: 10px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 2.5px;
  text-transform: uppercase;
  margin-bottom: 10px;
}
.stripe-title {
  font-family: var(--serif);
  font-size: 48px;
  font-weight: 400;
  color: white;
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}
.price-box {
  background: var(--bg-primary);
  border: 1px solid var(--border-subtle);
  padding: 20px 24px;
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-bottom: 28px;
}
.price-n {
  font-family: var(--serif);
  font-size: 64px;
  font-weight: 400;
  color: var(--accent);
  line-height: 1;
}
.price-r {
  font-size: 14px;
  color: white;
  font-weight: 500;
}
.price-rs {
  font-size: 12px;
  color: var(--text-muted);
}
.pfeat {
  list-style: none;
  margin-bottom: 28px;
}
.pfeat li {
  display: flex;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border-subtle);
  font-size: 14px;
  font-weight: 400;
  color: var(--text-secondary);
}
.pfeat-dot {
  width: 5px;
  height: 5px;
  background: var(--accent);
  border-radius: 50%;
  margin-top: 8px;
  flex-shrink: 0;
}
.pmethods {
  background: var(--bg-primary);
  padding: 10px 18px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 24px;
  align-items: center;
}
.pmb {
  padding: 4px 12px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--text-secondary);
}
.btn-stripe {
  display: block;
  width: 100%;
  background: var(--accent);
  color: white;
  padding: 18px;
  text-align: center;
  text-decoration: none;
  font-family: var(--serif);
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 0.3px;
  cursor: pointer;
  border: none;
  transition: background 0.2s;
}
.btn-stripe:hover {
  background: var(--accent-dark);
}

/* Page succès */
.swrap {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px 24px;
  background: var(--bg-primary);
}
.scheck {
  width: 72px;
  height: 72px;
  background: var(--accent);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  color: white;
  margin-bottom: 2rem;
  box-shadow: 0 0 0 8px rgba(227, 59, 44, 0.2);
  animation: pop 0.5s ease both;
}
@keyframes pop {
  from { transform: scale(0.4); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}
.stit {
  font-family: var(--serif);
  font-size: clamp(48px, 8vw, 88px);
  font-weight: 400;
  color: white;
  margin-bottom: 1.2rem;
  line-height: 1;
}
.stit .r {
  color: var(--accent);
  font-style: italic;
}
.ssub {
  font-size: 16px;
  color: var(--text-secondary);
  max-width: 440px;
  margin: 0 auto 2rem;
  line-height: 1.7;
}
.sbox {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  padding: 24px 32px;
  max-width: 480px;
  width: 100%;
  margin-bottom: 2.5rem;
  text-align: left;
}
.sbox-item {
  font-size: 14px;
  color: var(--text-secondary);
  padding: 8px 0;
  border-bottom: 1px solid var(--border-subtle);
}
.sbox-item:last-child {
  border: none;
}
.btn-retour {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 14px 28px;
  background: var(--accent);
  color: white;
  border: none;
  cursor: pointer;
  font-family: var(--sans);
  transition: background 0.2s;
  text-decoration: none;
}
.btn-retour:hover {
  background: var(--accent-dark);
}

/* Admin (même structure) */
.admin-login-wrap {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-primary);
}
.admin-login-box {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  padding: 48px;
  max-width: 400px;
  width: 100%;
  text-align: center;
  box-shadow: var(--shadow);
}
.admin-login-logo {
  font-family: var(--serif);
  font-size: 36px;
  font-weight: 400;
  color: white;
  margin-bottom: 8px;
}
.admin-login-logo em {
  font-style: italic;
  color: var(--accent);
}
.admin-login-sub {
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 32px;
}
.admin-err {
  font-size: 12px;
  color: var(--accent);
  margin-top: 12px;
  display: none;
}
.adwrap {
  max-width: 1400px;
  margin: 0 auto;
  padding: 100px 32px 80px;
}
.ad-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 40px;
}
.ad-tit {
  font-family: var(--serif);
  font-size: clamp(36px, 5vw, 60px);
  font-weight: 400;
  color: white;
  line-height: 1;
}
.ad-tit span {
  color: var(--accent);
  font-style: italic;
}
.ad-date {
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-top: 6px;
}
.live-dot {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #2a8a4a;
}
.live-dot::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #2a8a4a;
  animation: blink 1.5s ease-in-out infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
.kgrid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--border-subtle);
  margin-bottom: 32px;
  border: 1px solid var(--border-subtle);
}
.kcard {
  background: var(--bg-card);
  padding: 28px 24px;
}
.kcard.hot {
  background: rgba(227, 59, 44, 0.08);
}
.kl {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 8px;
}
.kv {
  font-family: var(--serif);
  font-size: 48px;
  font-weight: 400;
  color: white;
  line-height: 1;
}
.kv.r {
  color: var(--accent);
}
.ksub {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 4px;
}
.tsec {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  overflow: hidden;
  margin-bottom: 32px;
}
.tsec-h {
  padding: 16px 24px;
  background: var(--bg-secondary);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.tsec-t {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.5);
}
.tsec-c {
  font-family: var(--serif);
  font-size: 24px;
  font-weight: 400;
  color: var(--accent);
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  text-align: left;
  padding: 13px 20px;
  border-bottom: 1px solid var(--border-subtle);
  font-size: 13px;
  color: var(--text-secondary);
}
th {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-muted);
}
tr:hover td {
  background: rgba(227, 59, 44, 0.05);
  color: white;
}
.bd {
  display: inline-block;
  padding: 3px 12px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  background: rgba(227, 59, 44, 0.15);
  color: var(--accent);
}
.bd.ok {
  background: rgba(42, 138, 74, 0.15);
  color: #2a8a4a;
}
.bd.enc {
  background: rgba(234, 179, 8, 0.15);
  color: #eab308;
}
.ca-wrap {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
}
.ca-row {
  display: flex;
  align-items: center;
  padding: 12px 20px;
  border-bottom: 1px solid var(--border-subtle);
}
.ca-row:last-child {
  border: none;
}
.ca-m {
  font-size: 12px;
  color: var(--text-muted);
  min-width: 80px;
}
.ca-bar-bg {
  flex: 1;
  margin: 0 16px;
  height: 3px;
  background: var(--border-subtle);
}
.ca-bar {
  height: 3px;
  background: var(--accent);
}
.ca-v {
  font-size: 13px;
  font-weight: 500;
  color: white;
  min-width: 60px;
  text-align: right;
}

/* Footer */
footer {
  background: #060608;
  padding: 40px 56px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  flex-wrap: wrap;
  gap: 20px;
}
.flo {
  font-family: var(--sans);
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: white;
}
.flo em {
  font-style: normal;
  color: var(--accent);
}
.fmeta {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.3);
  margin-top: 5px;
  letter-spacing: 1px;
  text-transform: uppercase;
}
.fls {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
}
.fls a {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.4);
  text-decoration: none;
  cursor: pointer;
  transition: 0.2s;
}
.fls a:hover {
  color: var(--accent);
}

/* Responsive */
@media (max-width: 1024px) {
  .form-layout {
    grid-template-columns: 1fr;
  }
  .proc-grid {
    grid-template-columns: 1fr 1fr;
  }
  .kgrid {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 860px) {
  nav {
    padding: 0 24px;
  }
  .nav-r .nl {
    display: none;
  }
  .hero-inner {
    padding: 80px 24px 0;
  }
  .hero-cards {
    flex-direction: column;
    max-width: 340px;
  }
  .hero-stats {
    grid-template-columns: 1fr 1fr;
  }
  .proc-sec {
    padding: 56px 24px;
  }
  .proc-grid {
    grid-template-columns: 1fr;
  }
  .fg, .fg3 {
    grid-template-columns: 1fr;
  }
  .adwrap {
    padding: 80px 16px 60px;
  }
  .stripe-body {
    padding: 28px 24px;
  }
  footer {
    flex-direction: column;
    text-align: center;
    padding: 28px 24px;
  }
  .fls {
    justify-content: center;
  }
}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="logo" onclick="showPage('home')">Hub<em>Auto</em></div>
  <div class="nav-r">
    <span class="nl" onclick="showPage('sell')">Vendre</span>
    <span class="nl" onclick="showPage('buy')">Acheter</span>
    <a class="nl" href="mailto:amrcarexpert@gmail.com">Contact</a>
    <button class="nav-cta" onclick="showPage('sell')">Démarrer →</button>
  </div>
</nav>

<!-- PAGE HOME -->
<div id="page-home" class="page active">
  <div class="hero">
    <div class="hero-bg"></div>
    <div class="hero-inner">
      <div class="hero-eyebrow">Expert automobile · France</div>
      <h1 class="hero-h1">
        L'expert<br>
        qui vous <span class="r">correspond.</span>
      </h1>
      <p class="hero-sub">Vendez ou trouvez votre véhicule avec l'accompagnement d'un professionnel sélectionné pour vous.</p>
      <div class="hero-cards">
        <div class="hc" onclick="showPage('sell')">
          <div class="hc-tag">Particulier → Pro</div>
          <div class="hc-title">Vendre ma voiture</div>
          <div class="hc-desc">On analyse votre dossier et on le confie au bon professionnel.</div>
          <div class="hc-cta">Commencer →</div>
        </div>
        <div class="hc" onclick="showPage('buy')">
          <div class="hc-tag">Recherche sur-mesure</div>
          <div class="hc-title">Trouver ma voiture</div>
          <div class="hc-desc">Décrivez votre projet, nos experts le trouvent pour vous.</div>
          <div class="hc-cta">Commencer →</div>
        </div>
      </div>
    </div>
    <div class="hero-stats">
      <div class="hstat"><span class="hstat-ico">⏱</span><div><div class="hstat-lbl">Délai de réponse</div><div class="hstat-val">24h ouvrées</div></div></div>
      <div class="hstat"><span class="hstat-ico">🤝</span><div><div class="hstat-lbl">Professionnels</div><div class="hstat-val">Sélectionnés & vérifiés</div></div></div>
      <div class="hstat"><span class="hstat-ico">🔒</span><div><div class="hstat-lbl">Paiement</div><div class="hstat-val">Sécurisé Stripe · 30 €</div></div></div>
      <div class="hstat"><span class="hstat-ico">📍</span><div><div class="hstat-lbl">Zone</div><div class="hstat-val">Toute la France</div></div></div>
    </div>
  </div>

  <!-- SECTION PROCESS -->
  <div class="proc-sec">
    <div class="proc-hd">
      <div class="proc-badge">Comment ça marche</div>
      <h2>Un accompagnement <span>sur-mesure</span><br>en 4 étapes clés</h2>
    </div>
    <div class="proc-grid">
      <div class="proc-card">
        <div class="proc-ico"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></div>
        <div class="proc-n">Étape 01</div>
        <h3>Formulaire rapide</h3>
        <p>3 minutes. Renseignez votre véhicule ou votre besoin de recherche.</p>
      </div>
      <div class="proc-card">
        <div class="proc-ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg></div>
        <div class="proc-n">Étape 02</div>
        <h3>Analyse stratégique</h3>
        <p>30€ d'aide à la décision. Notre expert étudie votre dossier en profondeur.</p>
      </div>
      <div class="proc-card">
        <div class="proc-ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <div class="proc-n">Étape 03</div>
        <h3>Réponse sous 24h</h3>
        <p>Recommandation personnalisée et profil du professionnel partenaire.</p>
      </div>
      <div class="proc-card">
        <div class="proc-ico"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
        <div class="proc-n">Étape 04</div>
        <h3>Mise en relation</h3>
        <p>Contact direct avec le professionnel, accompagnement jusqu'à la finalisation.</p>
      </div>
    </div>
  </div>

  <footer id="footer-home">
    <div><div class="flo">Hub<em>Auto</em></div><div class="fmeta">AMR CAR EXPERT · SIRET 941 790 222 00017</div></div>
    <div class="fls">
      <a href="https://instagram.com/amr_carr" target="_blank">Instagram</a>
      <a href="https://tiktok.com/@rayou_atm" target="_blank">TikTok</a>
      <a href="https://linkedin.com/in/rayane-ait-malouk" target="_blank">LinkedIn</a>
      <a href="mailto:amrcarexpert@gmail.com">Contact</a>
      <a onclick="showPage('admin-login')">Espace Pro</a>
    </div>
  </footer>
</div>

<!-- VENDRE -->
<div id="page-sell" class="page">
  <div class="fwrap">
    <div class="fc">
      <button class="fbk" onclick="showPage('home')">← Retour</button>
      <div class="fhd">
        <div class="fkick">Vente assistée</div>
        <div class="ftit">Vendre<br><strong>ma voiture</strong></div>
        <p class="fdesc">Remplissez ce formulaire, nous trouvons le professionnel qui reprendra ou vendra votre véhicule au meilleur prix.</p>
      </div>

      <form id="form-sell" onsubmit="submitSell(event)">
        <div class="form-layout">
          <!-- GAUCHE : FORMULAIRE -->
          <div>
            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">1</span><span class="fsec-t">Le véhicule</span></div>
              <div class="fg">
                <div class="fgrp"><label>Marque <span class="req">*</span></label><input name="marque" required placeholder="BMW, Renault, Peugeot…"></div>
                <div class="fgrp"><label>Modèle <span class="req">*</span></label><input name="modele" required placeholder="Série 3, Clio…"></div>
                <div class="fgrp"><label>Année <span class="req">*</span></label><input type="number" name="annee" required placeholder="2020"></div>
                <div class="fgrp"><label>Kilométrage <span class="req">*</span></label><input type="number" name="km" required placeholder="65 000"></div>
              </div>
            </div>

            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">2</span><span class="fsec-t">Motorisation & état</span></div>
              <div class="fg3">
                <div class="fgrp"><label>Énergie</label><select name="energie"><option>Essence</option><option>Diesel</option><option>Hybride</option><option>Électrique</option><option>GPL</option></select></div>
                <div class="fgrp"><label>Boîte</label><select name="boite"><option>Manuelle</option><option>Automatique</option></select></div>
                <div class="fgrp"><label>Couleur</label><input name="couleur" placeholder="Noir, Blanc…"></div>
              </div>
              <div class="rrow">
                <label class="rpill"><input type="radio" name="etat" value="Excellent" required><span class="rpl">⭐ Excellent</span></label>
                <label class="rpill"><input type="radio" name="etat" value="Bon"><span class="rpl">✅ Bon</span></label>
                <label class="rpill"><input type="radio" name="etat" value="Correct"><span class="rpl">🔧 Correct</span></label>
                <label class="rpill"><input type="radio" name="etat" value="À réparer"><span class="rpl">⚠️ À réparer</span></label>
              </div>
            </div>

            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">3</span><span class="fsec-t">Prix & localisation</span></div>
              <div class="fg">
                <div class="fgrp"><label>Prix souhaité (€) <span class="req">*</span></label><input type="number" name="prix" required placeholder="12 000"></div>
                <div class="fgrp"><label>Ville + Code postal <span class="req">*</span></label><input name="localisation" required placeholder="Lyon, 69001"></div>
                <div class="fgrp gf"><label>Historique entretien</label><textarea name="entretien" placeholder="Carnet à jour, CT valide, révision effectuée…"></textarea></div>
                <div class="fgrp gf"><label>Immatriculation <span style="text-transform:none;font-size:9px;letter-spacing:0;color:var(--text-muted)">(optionnel — vérification HistoVec)</span></label><input name="immat" placeholder="AA-123-BB"></div>
              </div>
            </div>

            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">4</span><span class="fsec-t">Photos</span></div>
              <div class="phdrop">
                <input type="file" id="sell-photos" multiple accept="image/*" onchange="previewPhotos(event,'sell-ph')">
                <div class="ph-icon">📸</div>
                <p class="ph-txt">Glissez ou <b>parcourez</b><br>Extérieur, intérieur, compteur — 3 photos min.</p>
              </div>
              <div class="ph-preview" id="sell-ph"></div>
            </div>

            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">5</span><span class="fsec-t">Vos coordonnées</span></div>
              <div class="fg">
                <div class="fgrp"><label>Prénom <span class="req">*</span></label><input name="prenom" required placeholder="Jean"></div>
                <div class="fgrp"><label>Nom <span class="req">*</span></label><input name="nom" required placeholder="Dupont"></div>
                <div class="fgrp"><label>Email <span class="req">*</span></label><input type="email" name="email" required placeholder="jean@mail.com"></div>
                <div class="fgrp"><label>Téléphone <span class="req">*</span></label><input type="tel" name="tel" required placeholder="06 00 00 00 00"></div>
                <div class="fgrp gf"><label>Message complémentaire</label><textarea name="message" placeholder="Précisions, défauts à signaler…"></textarea></div>
              </div>
            </div>
          </div>

          <!-- SIDEBAR PAIEMENT -->
          <div class="pay-side">
            <div class="pay-card-box">
              <div class="pay-card-top">
                <div class="pay-card-lbl">Frais d'analyse de dossier</div>
                <div class="pay-card-price">30 €<span> TTC</span></div>
              </div>
              <div class="pay-card-body">
                <div class="pay-recap">
                  <div class="pay-rl">Analyse personnalisée<strong>Inclus</strong></div>
                  <div class="pay-rl">Sélection du professionnel<strong>Inclus</strong></div>
                  <div class="pay-rl">Vérification HistoVec<strong>Inclus</strong></div>
                  <div class="pay-rl">Suivi jusqu'à finalisation<strong>Inclus</strong></div>
                </div>
                <div class="garantie">
                  <strong>Réponse garantie sous 24h</strong>
                  Pour garantir une prise en charge optimale, je vous donne une réponse dans les 24h suivant votre paiement, hors week-end.
                </div>
                <button type="submit" class="btn-pay">🔒 &nbsp;Valider mon dossier — 30 €</button>
                <div class="ssl-note">Paiement sécurisé via Stripe</div>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- ACHETER -->
<div id="page-buy" class="page">
  <div class="fwrap">
    <div class="fc">
      <button class="fbk" onclick="showPage('home')">← Retour</button>
      <div class="fhd">
        <div class="fkick">Recherche personnalisée</div>
        <div class="ftit">Trouver<br><strong>ma voiture</strong></div>
        <p class="fdesc">Décrivez le véhicule idéal, nos experts le dénichent pour vous.</p>
      </div>

      <form id="form-buy" onsubmit="submitBuy(event)">
        <div class="form-layout">
          <div>
            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">1</span><span class="fsec-t">Le véhicule recherché</span></div>
              <div class="fg">
                <div class="fgrp"><label>Marque(s) <span class="req">*</span></label><input name="marque" required placeholder="BMW, Audi ou toute marque"></div>
                <div class="fgrp"><label>Modèle(s)</label><input name="modele" placeholder="X5, A4… (optionnel)"></div>
                <div class="fgrp"><label>Énergie</label><select name="energie"><option>Indifférent</option><option>Essence</option><option>Diesel</option><option>Hybride</option><option>Électrique</option></select></div>
                <div class="fgrp"><label>Boîte</label><select name="boite"><option>Indifférent</option><option>Manuelle</option><option>Automatique</option></select></div>
              </div>
            </div>

            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">2</span><span class="fsec-t">Critères & budget</span></div>
              <div class="fg">
                <div class="fgrp"><label>Année min <span class="req">*</span></label><input type="number" name="annee_min" required placeholder="2019"></div>
                <div class="fgrp"><label>Année max</label><input type="number" name="annee_max" placeholder="2025"></div>
                <div class="fgrp"><label>KM max <span class="req">*</span></label><input type="number" name="km_max" required placeholder="100 000"></div>
                <div class="fgrp"><label>Budget max (€) <span class="req">*</span></label><input type="number" name="budget" required placeholder="25 000"></div>
                <div class="fgrp"><label>Ville + Code postal <span class="req">*</span></label><input name="localisation" required placeholder="Paris, 75001"></div>
                <div class="fgrp"><label>Rayon de recherche</label><select name="rayon"><option>50 km</option><option>100 km</option><option selected>Toute la France</option><option>Import étranger</option></select></div>
                <div class="fgrp gf"><label>Options souhaitées</label><textarea name="options" placeholder="Toit ouvrant, GPS, sièges chauffants, cuir… (non bloquants)"></textarea></div>
              </div>
            </div>

            <div class="fsec">
              <div class="fsec-hd"><span class="fsec-n">3</span><span class="fsec-t">Vos coordonnées</span></div>
              <div class="fg">
                <div class="fgrp"><label>Prénom <span class="req">*</span></label><input name="prenom" required placeholder="Marie"></div>
                <div class="fgrp"><label>Nom <span class="req">*</span></label><input name="nom" required placeholder="Martin"></div>
                <div class="fgrp"><label>Email <span class="req">*</span></label><input type="email" name="email" required placeholder="marie@mail.com"></div>
                <div class="fgrp"><label>Téléphone <span class="req">*</span></label><input type="tel" name="tel" required placeholder="06 00 00 00 00"></div>
              </div>
            </div>
          </div>

          <div class="pay-side">
            <div class="pay-card-box">
              <div class="pay-card-top">
                <div class="pay-card-lbl">Frais d'analyse de dossier</div>
                <div class="pay-card-price">30 €<span> TTC</span></div>
              </div>
              <div class="pay-card-body">
                <div class="pay-recap">
                  <div class="pay-rl">Analyse de recherche<strong>Inclus</strong></div>
                  <div class="pay-rl">Chasseur auto dédié<strong>Inclus</strong></div>
                  <div class="pay-rl">Vérification du véhicule<strong>Inclus</strong></div>
                  <div class="pay-rl">Suivi jusqu'à finalisation<strong>Inclus</strong></div>
                </div>
                <div class="garantie">
                  <strong>Réponse garantie sous 24h</strong>
                  Pour garantir une prise en charge optimale, je vous donne une réponse dans les 24h suivant votre paiement, hors week-end.
                </div>
                <button type="submit" class="btn-pay">🔒 &nbsp;Lancer ma recherche — 30 €</button>
                <div class="ssl-note">Paiement sécurisé via Stripe</div>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- PAIEMENT STRIPE -->
<div id="page-payment" class="page">
  <div class="pwrap">
    <button class="pbk" onclick="goBackFromPayment()">← Modifier mon dossier</button>
    <div class="stripe-card">
      <div class="stripe-img">
        <svg class="stripe-img-svg" viewBox="0 0 900 300" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
          <g fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round">
            <path d="M40 240 L40 205 Q45 170 95 148 L235 108 Q290 82 380 78 L530 76 Q640 76 710 102 L810 138 Q850 158 868 185 L875 225 L875 240 Z" stroke-width="2.5" fill="#333"/>
            <circle cx="188" cy="240" r="48" stroke-width="3" fill="#1a1a1a"/>
            <circle cx="188" cy="240" r="34" stroke-width="2" fill="#2a2a2a"/>
            <circle cx="188" cy="240" r="13" stroke-width="1.5" fill="#444"/>
            <circle cx="700" cy="240" r="48" stroke-width="3" fill="#1a1a1a"/>
            <circle cx="700" cy="240" r="34" stroke-width="2" fill="#2a2a2a"/>
            <circle cx="700" cy="240" r="13" stroke-width="1.5" fill="#444"/>
          </g>
        </svg>
        <div class="stripe-img-txt">Hub Auto · Aide à la décision</div>
      </div>
      <div class="stripe-body">
        <div class="stripe-kick">Dernière étape</div>
        <div class="stripe-title">Votre dossier est prêt</div>
        <div class="price-box">
          <div class="price-n">30€</div>
          <div><div class="price-r">Aide à la décision stratégique</div><div class="price-rs">Accompagnement expert jusqu'à la concrétisation</div></div>
        </div>
        <ul class="pfeat">
          <li><span class="pfeat-dot"></span>Analyse personnalisée par un expert automobile</li>
          <li><span class="pfeat-dot"></span>Sélection du professionnel le plus adapté</li>
          <li><span class="pfeat-dot"></span>Réponse sous 24h (email / téléphone)</li>
          <li><span class="pfeat-dot"></span>Accompagnement jusqu'à la finalisation</li>
        </ul>
        <div class="pmethods">
          <span class="pmb">VISA</span>
          <span class="pmb">MASTERCARD</span>
          <span class="pmb">APPLE PAY</span>
          <span class="pmb">GOOGLE PAY</span>
          <span style="font-size:12px;color:var(--text-muted);margin-left:4px;">🔒 Stripe</span>
        </div>
        <!-- ⚠️ REMPLACE CE LIEN PAR TON LIEN STRIPE -->
        <a href="https://buy.stripe.com/aFa9AVcoV9aGcIq2QLdZ602" target="_blank" class="btn-stripe">
          Payer 30 € — Carte, Apple Pay ou Google Pay →
        </a>
      </div>
    </div>
  </div>
</div>

<!-- SUCCÈS -->
<div id="page-success" class="page">
  <div class="swrap">
    <div class="scheck">✓</div>
    <div class="stit">Dossier<br>validé <span class="r">!</span></div>
    <p class="ssub">Votre demande est enregistrée. Nos experts vous répondent sous 24h ouvrées.</p>
    <div class="sbox">
      <div class="sbox-item">📧 Confirmation envoyée à votre adresse email</div>
      <div class="sbox-item">📞 Un conseiller peut vous rappeler sur demande</div>
      <div class="sbox-item">⏱ Réponse sous 24h ouvrées (hors week-end)</div>
    </div>
    <button class="btn-retour" onclick="showPage('home')">← Retour à l'accueil</button>
  </div>
</div>

<!-- ADMIN LOGIN -->
<div id="page-admin-login" class="page">
  <div class="admin-login-wrap">
    <div class="admin-login-box">
      <div class="admin-login-logo">Hub<em>Auto</em></div>
      <div class="admin-login-sub">Accès professionnel</div>
      <div class="fgrp"><label>Code d'accès</label><input type="password" id="admin-pwd" placeholder="••••••••" onkeypress="if(event.key==='Enter')adminLogin()"></div>
      <button class="btn-pay" onclick="adminLogin()" style="margin-top:16px">ACCÉDER →</button>
      <div class="admin-err" id="admin-err">Mot de passe incorrect</div>
    </div>
  </div>
</div>

<!-- ADMIN DASHBOARD -->
<div id="page-admin" class="page">
  <div class="adwrap">
    <div class="ad-top">
      <div>
        <div class="ad-tit">Tableau<br>de <span>bord</span></div>
        <div class="ad-date" id="admin-date"></div>
      </div>
      <div style="display:flex;align-items:center;gap:20px;">
        <div class="live-dot">En direct</div>
        <button onclick="showPage('home')" class="fbk">Déconnexion</button>
      </div>
    </div>

    <div class="kgrid">
      <div class="kcard hot"><div class="kl">CA total</div><div class="kv r">420 €</div><div class="ksub">14 dossiers × 30 €</div></div>
      <div class="kcard"><div class="kl">En cours</div><div class="kv">3</div><div class="ksub">Accompagnements actifs</div></div>
      <div class="kcard"><div class="kl">En attente</div><div class="kv r">5</div><div class="ksub">À traiter sous 24h</div></div>
      <div class="kcard"><div class="kl">Finalisés</div><div class="kv">9</div><div class="ksub">Dossiers conclus</div></div>
    </div>

    <div class="tsec" style="margin-bottom:24px;">
      <div class="tsec-h"><span class="tsec-t">Demandes récentes</span><span class="tsec-c">8</span></div>
      <table>
        <thead><tr><th>Client</th><th>Type</th><th>Véhicule / Recherche</th><th>Reçu le</th><th>Statut</th> </tr</thead>
        <tbody>
          <tr><td><strong>Karim B.</strong><br><span style="font-size:11px;color:var(--text-muted)">06 12 34 56 78</span></td><td><span class="bd">Vente</span></td><td>BMW X5 2021 · 58k km</td><td>Auj. 09:12</td><td><span class="bd">Nouveau</span></td></tr>
          <tr><td><strong>Sophie L.</strong></td><td><span class="bd">Achat</span></td><td>Mercedes GLE · 70k€</td><td>Auj. 08:45</td><td><span class="bd">Nouveau</span></td></tr>
          <tr><td><strong>Thomas P.</strong></td><td><span class="bd">Vente</span></td><td>Peugeot 308 · diesel</td><td>Hier 18:30</td><td><span class="bd enc">En cours</span></td></tr>
          <tr><td><strong>Camille R.</strong></td><td><span class="bd">Achat</span></td><td>Audi A3 · essence</td><td>Hier 15:00</td><td><span class="bd ok">Conclu ✓</span></td></tr>
          <tr><td><strong>Lucas B.</strong></td><td><span class="bd">Vente</span></td><td>BMW 320i · 2019</td><td>Hier 11:22</td><td><span class="bd enc">En cours</span></td></tr>
        </tbody>
      </table>
    </div>

    <div class="ca-wrap tsec">
      <div class="tsec-h"><span class="tsec-t">Chiffre d'affaires</span><span class="tsec-c" style="color:var(--text-primary)">420 €</span></div>
      <div style="padding:8px 0;">
        <div class="ca-row"><span class="ca-m">Janvier</span><div class="ca-bar-bg"><div class="ca-bar" style="width:40%"></div></div><span class="ca-v">90 €</span></div>
        <div class="ca-row"><span class="ca-m">Février</span><div class="ca-bar-bg"><div class="ca-bar" style="width:55%"></div></div><span class="ca-v">120 €</span></div>
        <div class="ca-row"><span class="ca-m">Mars</span><div class="ca-bar-bg"><div class="ca-bar" style="width:92%"></div></div><span class="ca-v">210 €</span></div>
      </div>
    </div>
  </div>
</div>

<script>
let formType = null;
let formData = {};

function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  window.scrollTo(0,0);
}

function goBackFromPayment() {
  showPage(formType === 'sell' ? 'sell' : 'buy');
}

function collect(formEl) {
  let d = {};
  formEl.querySelectorAll('input,select,textarea').forEach(el => {
    if (!el.name) return;
    if (el.type === 'radio') { if (el.checked) d[el.name] = el.value; }
    else if (el.type !== 'file') d[el.name] = el.value;
    else d[el.name] = el.files.length + ' photo(s)';
  });
  return d;
}

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.readAsDataURL(file);
    r.onload = () => resolve(r.result);
    r.onerror = e => reject(e);
  });
}

async function submitSell(e) {
  e.preventDefault();
  const data = collect(document.getElementById('form-sell'));
  data._type = 'VENTE';
  const files = document.getElementById('sell-photos').files;
  const photos = [];
  for (let i = 0; i < files.length; i++) photos.push(await fileToBase64(files[i]));
  data.photos = photos;
  formType = 'sell'; formData = data;
  sessionStorage.setItem('hubauto_pending', JSON.stringify({type:'sell', data}));
  showPage('payment');
}

async function submitBuy(e) {
  e.preventDefault();
  const data = collect(document.getElementById('form-buy'));
  data._type = 'ACHAT'; data.photos = [];
  formType = 'buy'; formData = data;
  sessionStorage.setItem('hubauto_pending', JSON.stringify({type:'buy', data}));
  showPage('payment');
}

// Webhook Google Sheets (à remplacer par ton URL réelle)
const WEBHOOK_URL = 'https://docs.google.com/spreadsheets/d/1NVoTNRZFv1GnSpAmmQwtNbsEPJanYK52aEwqfS2cMRU/edit?gid=0#gid=0';
async function sendToGoogleSheets(type, data) {
  const payload = {
    type: type === 'sell' ? 'VENTE' : 'ACHAT',
    prenom: data.prenom,
    nom: data.nom,
    email: data.email,
    telephone: data.tel,
    localisation: data.localisation || '',
    date: new Date().toLocaleString('fr-FR'),
    nombre_photos: data.photos ? data.photos.length : 0,
    details: type === 'sell' ? {
      marque: data.marque,
      modele: data.modele,
      annee: data.annee,
      km: data.km,
      energie: data.energie,
      boite: data.boite,
      couleur: data.couleur || '',
      etat: data.etat,
      prix: data.prix,
      immat: data.immat || '',
      entretien: data.entretien || '',
      message: data.message || ''
    } : {
      marque: data.marque,
      modele: data.modele,
      energie: data.energie,
      boite: data.boite || 'Indifférent',
      annee_min: data.annee_min,
      annee_max: data.annee_max || '',
      km_max: data.km_max,
      budget: data.budget,
      couleur: data.couleur || '',
      options: data.options || ''
    }
  };
  try {
    await fetch(WEBHOOK_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    console.log('Données envoyées à Google Sheets');
  } catch (e) { console.error(e); }
}

// Détection retour Stripe
if (window.location.search.includes('success')) {
  const saved = sessionStorage.getItem('hubauto_pending');
  if (saved) {
    const { type, data } = JSON.parse(saved);
    sessionStorage.removeItem('hubauto_pending');
    sendToGoogleSheets(type, data);
    setTimeout(() => showPage('success'), 500);
  } else { showPage('success'); }
}

function previewPhotos(event, id) {
  const c = document.getElementById(id); c.innerHTML = '';
  Array.from(event.target.files).slice(0,8).forEach(f => {
    const r = new FileReader();
    r.onload = e => { const img = document.createElement('img'); img.src = e.target.result; c.appendChild(img); };
    r.readAsDataURL(f);
  });
}

function adminLogin() {
  const pwd = document.getElementById('admin-pwd').value;
  if (pwd === 'hubpro2025') {
    showPage('admin');
    document.getElementById('admin-date').textContent = new Date().toLocaleDateString('fr-FR',{weekday:'long',year:'numeric',month:'long',day:'numeric'});
    document.getElementById('admin-err').style.display = 'none';
  } else {
    document.getElementById('admin-err').style.display = 'block';
  }
}

showPage('home');
</script>
</body>
</html>
