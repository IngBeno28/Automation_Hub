import streamlit as st
from PIL import Image
import os
from datetime import datetime

# Import branding module
from branding import (
    CARD_STYLES, 
    get_card_style, 
    get_bg_pattern, 
    get_card_data,
    get_card_svg,
    CARD_CSS  # Now this exists in branding.py
)

# --- Page Configuration ---
st.set_page_config(
    page_title="Automation_Hub | Engineering Solutions",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (Premium SaaS Design with Background Enhancements) ---
st.markdown("""
<style>
    /* ===== GLOBAL RESET & BASE ===== */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(180deg, #faf9f6 0%, #ffffff 100%);
    }

    .main > div {
        padding: 0rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    html, body, h1, h2, h3, h4, h5, h6, p, div, span, button {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ===== HERO — dark editorial band ===== */
    .hero-section {
        position: relative;
        overflow: hidden;
        background: linear-gradient(155deg, #0b0f14 0%, #151b23 100%);
        border-radius: 6px;
        padding: 4rem 3rem;
        margin: 1.5rem 0 3rem 0;
    }

    .hero-section .hero-bg-enhanced {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .hero-section .hero-bg-enhanced .grid-pattern {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
        background-size: 48px 48px;
        mask-image: linear-gradient(180deg, rgba(0,0,0,0.9) 0%, transparent 85%);
    }

    .hero-section .hero-bg-enhanced .blob-1 {
        position: absolute;
        top: -1px;
        right: -1px;
        width: 220px;
        height: 220px;
        border-top: 1px solid rgba(181, 82, 42, 0.5);
        border-right: 1px solid rgba(181, 82, 42, 0.5);
    }

    .hero-section .hero-bg-enhanced .blob-2,
    .hero-section .hero-bg-enhanced .blob-3 {
        display: none;
    }

    .hero-section .hero-content-inner {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        gap: 4rem;
        flex-wrap: wrap;
    }

    /* ===== SECTION GRADIENT BACKGROUNDS ===== */
    .section-gradient-blue {
        background: linear-gradient(155deg, #0b0f14 0%, #151b23 100%);
        border-radius: 6px;
        padding: 3.5rem 2.5rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }

    .section-gradient-blue::before {
        content: '';
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
        background-size: 44px 44px;
        mask-image: radial-gradient(ellipse at 70% 20%, rgba(0,0,0,0.9) 0%, transparent 65%);
        pointer-events: none;
        z-index: 0;
    }

    .glow-orb { display: none; }

    .section-gradient-blue .section-label { color: rgba(255,255,255,0.55); }
    .section-gradient-blue .section-label::before { background: #b5522a; }
    .section-gradient-blue .section-title { color: #ffffff; }
    .section-gradient-blue .section-title span { color: #7fa3d6; }
    .section-gradient-blue .section-subtitle { color: rgba(255,255,255,0.55); }

    .section-gradient-blue > * {
        position: relative;
        z-index: 1;
    }

    /* ===== NAVBAR ===== */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(11, 15, 20, 0.06);
        margin-bottom: 1rem;
    }

    .navbar-brand {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        text-decoration: none;
    }

    .navbar-brand img {
        height: 40px;
        width: auto;
    }

    .navbar-brand .brand-text {
        font-weight: 800;
        font-size: 1.2rem;
        color: #0b0f14;
        letter-spacing: -0.3px;
        text-transform: uppercase;
    }

    .navbar-brand .brand-text span {
        color: #2f5fa8;
    }

    .navbar-actions {
        display: flex;
        gap: 1.75rem;
        align-items: center;
    }

    .navbar-actions .nav-link {
        color: #0b0f14;
        text-decoration: none;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        transition: color 0.3s ease;
        padding: 0.4rem 0;
    }

    .navbar-actions .nav-link:hover {
        color: #2f5fa8;
    }

    .navbar-actions .nav-cta {
        background: #0b0f14;
        color: white;
        padding: 0.55rem 1.4rem;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        text-decoration: none;
        transition: all 0.25s ease;
    }

    .navbar-actions .nav-cta:hover {
        background: #2f5fa8;
        color: white;
    }

    /* ===== CONTAINER UTILITIES ===== */
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 4rem 1rem;
    }

    .section-label {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        color: #6b6f76;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .section-label::before {
        content: '';
        display: inline-block;
        width: 22px;
        height: 1px;
        background: #b5522a;
    }

    .section-title {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #0b0f14;
        line-height: 1.2;
        margin-bottom: 0.75rem;
    }

    .section-title span {
        color: #2f5fa8;
    }

    .section-subtitle {
        font-size: 1.1rem;
        color: #6b6f76;
        font-weight: 400;
        line-height: 1.6;
        max-width: 600px;
    }

    /* ===== HERO CONTENT ===== */
    .hero-text {
        flex: 1 1 50%;
        min-width: 300px;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: rgba(255,255,255,0.55);
        margin-bottom: 1.75rem;
    }

    .hero-badge span {
        display: inline-block;
        width: 26px;
        height: 1px;
        background: #b5522a;
    }

    .hero-title {
        font-size: 3.4rem;
        font-weight: 800;
        letter-spacing: -1px;
        color: #ffffff;
        line-height: 1.08;
        margin-bottom: 1.5rem;
    }

    .hero-title .highlight {
        color: #ffffff;
        position: relative;
        white-space: nowrap;
    }

    .hero-title .highlight::after {
        content: '';
        position: absolute;
        left: 0; right: 0; bottom: 6px;
        height: 10px;
        background: rgba(181, 82, 42, 0.55);
        z-index: -1;
    }

    .hero-description {
        font-size: 1.15rem;
        color: rgba(255,255,255,0.65);
        line-height: 1.8;
        max-width: 500px;
        margin-bottom: 2.25rem;
    }

    .hero-pillars {
        display: flex;
        gap: 0;
        flex-wrap: wrap;
        margin-bottom: 2.25rem;
        border-top: 1px solid rgba(255,255,255,0.12);
        padding-top: 1.25rem;
    }

    .hero-pillar {
        flex: 1;
        min-width: 140px;
        border-right: 1px solid rgba(255,255,255,0.12);
        padding-right: 1rem;
    }

    .hero-pillar:last-child {
        border-right: none;
    }

    .hero-pillar strong {
        display: block;
        font-size: 0.95rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.2rem;
    }

    .hero-pillar span {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.5);
    }

    .hero-actions {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        align-items: center;
    }

    .hero-visual {
        flex: 1 1 40%;
        min-width: 280px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }

    .hero-visual .floating-card {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 4px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.14);
        width: 100%;
        max-width: 400px;
        position: relative;
        transition: transform 0.3s ease;
    }

    .hero-visual .floating-card:hover {
        transform: translateY(-4px);
    }

    .floating-card .panel-label {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: rgba(255,255,255,0.4);
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid rgba(255,255,255,0.12);
    }

    .floating-card .stat-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 0.25rem;
    }

    .floating-card .stat-item {
        text-align: left;
    }

    .floating-card .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
    }

    .floating-card .stat-label {
        font-size: 0.78rem;
        color: rgba(255,255,255,0.45);
        margin-top: 0.3rem;
    }

    .floating-card .tool-preview {
        display: flex;
        gap: 0.8rem;
        align-items: center;
        padding: 0.8rem 0;
        margin-top: 0.75rem;
        border-top: 1px solid rgba(255,255,255,0.1);
    }

    .floating-card .tool-preview .icon {
        font-size: 1.3rem;
    }

    .floating-card .tool-preview .info {
        flex: 1;
    }

    .floating-card .tool-preview .info .name {
        font-weight: 600;
        color: #ffffff;
        font-size: 0.88rem;
    }

    .floating-card .tool-preview .info .desc {
        font-size: 0.74rem;
        color: rgba(255,255,255,0.45);
    }

    /* ===== BUTTONS ===== */
    .btn-primary {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #2f5fa8;
        color: white;
        padding: 0.8rem 1.9rem;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.95rem;
        border: none;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.25s ease;
        font-family: 'Inter', sans-serif;
    }

    .btn-primary:hover {
        background: #1f4278;
        color: white;
    }

    .btn-secondary {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: transparent;
        color: #0b0f14;
        padding: 0.8rem 1.9rem;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid rgba(11, 15, 20, 0.25);
        cursor: pointer;
        text-decoration: none;
        transition: all 0.25s ease;
        font-family: 'Inter', sans-serif;
    }

    .btn-secondary:hover {
        background: rgba(11, 15, 20, 0.04);
        border-color: #0b0f14;
    }

    .hero-actions .btn-secondary {
        color: #ffffff;
        border-color: rgba(255,255,255,0.35);
    }

    .hero-actions .btn-secondary:hover {
        background: rgba(255,255,255,0.08);
        border-color: #ffffff;
    }

    .btn-ghost {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #2f5fa8;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
        background: none;
        border: none;
        cursor: pointer;
        font-size: 1rem;
    }

    .btn-ghost:hover {
        gap: 0.8rem;
        color: #1f4278;
    }

    /* ===== PRODUCT CARDS ===== */
    .products-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .product-card {
        border-radius: 4px;
        border: 1px solid rgba(11, 15, 20, 0.10);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        background: white;
    }

    .product-card .card-body {
        padding: 1.5rem 1.5rem 1.75rem 1.5rem;
        display: flex;
        flex-direction: column;
        flex: 1;
        position: relative;
        z-index: 1;
    }

    .product-card .badge {
        display: inline-block;
        color: var(--card-accent, #2f5fa8);
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
        align-self: flex-start;
    }

    .product-card h3 {
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: -0.2px;
        color: #0b0f14;
        margin-bottom: 0.5rem;
    }

    .product-card p {
        color: #6b6f76;
        font-size: 0.92rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        flex: 1;
    }

    .product-card .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 1rem;
        border-top: 1px solid rgba(11, 15, 20, 0.08);
        margin-top: auto;
    }

    .product-card .card-footer .status {
        font-size: 0.72rem;
        color: #6b6f76;
        font-weight: 500;
    }

    .product-card .card-footer .status .dot {
        display: inline-block;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        margin-right: 6px;
        background: #3f8f5f;
    }

    /* ===== FEATURE BADGES ===== */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .feature-badge {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1.2rem 1.5rem;
        background: white;
        border-radius: 4px;
        border: 1px solid rgba(11, 15, 20, 0.06);
        transition: all 0.3s ease;
    }

    .feature-badge:hover {
        transform: translateY(-4px);
        border-color: #b5522a;
    }

    .feature-badge .emoji {
        font-size: 1.8rem;
        flex-shrink: 0;
    }

    .feature-badge .content h4 {
        font-size: 0.95rem;
        font-weight: 600;
        color: #0b0f14;
        margin-bottom: 0.1rem;
    }

    .feature-badge .content p {
        font-size: 0.8rem;
        color: #6b6f76;
        margin: 0;
    }

    /* ===== STATISTICS — editorial metric strip ===== */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
        background: #0b0f14;
        border-radius: 6px;
        padding: 3rem 2rem;
        position: relative;
        overflow: hidden;
    }

    .stats-grid .glow-orb { display: none; }

    .stat-item-large {
        text-align: left;
        position: relative;
        z-index: 1;
        padding-left: 1.25rem;
        border-left: 2px solid #b5522a;
    }

    .stat-item-large .number {
        font-size: 2.6rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
    }

    .stat-item-large .label {
        font-size: 0.78rem;
        color: rgba(255,255,255,0.5);
        margin-top: 0.4rem;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .stat-divider {
        display: none;
    }

    /* ===== ROADMAP ===== */
    .roadmap-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .roadmap-item {
        background: white;
        border-radius: 4px;
        padding: 1.8rem 1.5rem;
        border: 1px solid rgba(11, 15, 20, 0.10);
        border-top: 3px solid #0b0f14;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .roadmap-item:hover {
        transform: translateY(-4px);
        border-top-color: #b5522a;
    }

    .roadmap-item .phase {
        display: inline-block;
        color: #6b6f76;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .roadmap-item h4 {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0b0f14;
        margin-bottom: 0.3rem;
    }

    .roadmap-item p {
        font-size: 0.85rem;
        color: #6b6f76;
        line-height: 1.5;
        margin: 0;
    }

    .roadmap-item .coming-soon {
        display: inline-block;
        color: #b5522a;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 0.9rem;
    }

    /* ===== TRUST & CONTACT SECTION ===== */
    .trust-section {
        background: white;
        border-radius: 4px;
        padding: 3rem 2.5rem;
        border: 1px solid rgba(11, 15, 20, 0.10);
        margin-top: 2rem;
        position: relative;
        overflow: hidden;
    }

    .trust-section .glow-orb { display: none; }

    /* Bentley-style oversized quotation mark */
    .trust-quote {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 1.25rem;
        align-items: flex-start;
        padding: 1.5rem 0 2.25rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(11, 15, 20, 0.10);
    }

    .trust-quote .mark {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 4.5rem;
        line-height: 0.6;
        color: #b5522a;
        font-weight: 700;
    }

    .trust-quote .quote-text {
        font-size: 1.15rem;
        color: #0b0f14;
        line-height: 1.55;
        font-weight: 500;
        max-width: 640px;
    }

    .trust-quote .quote-attr {
        display: block;
        margin-top: 0.9rem;
        font-size: 0.82rem;
        color: #6b6f76;
        font-weight: 600;
    }

    .trust-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
        align-items: start;
        position: relative;
        z-index: 1;
    }

    .trust-info h3 {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0b0f14;
        margin-bottom: 0.5rem;
    }

    .trust-info p {
        color: #6b6f76;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .trust-info .trust-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(11, 15, 20, 0.04);
    }

    .trust-info .trust-item:last-child {
        border-bottom: none;
    }

    .trust-info .trust-item .icon {
        font-size: 1.2rem;
        width: 34px;
        height: 34px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(11, 15, 20, 0.05);
        border-radius: 4px;
        flex-shrink: 0;
        margin-top: 0.1rem;
    }

    .trust-info .trust-item .text strong {
        display: block;
        font-size: 0.95rem;
        color: #0b0f14;
        margin-bottom: 0.1rem;
    }

    .trust-info .trust-item .text span {
        font-size: 0.9rem;
        color: #6b6f76;
    }

    .trust-form {
        background: #faf9f6;
        border-radius: 4px;
        border: 1px solid rgba(11, 15, 20, 0.08);
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
    }

    .trust-form .glow-orb { display: none; }

    .trust-form h4 {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0b0f14;
        margin-bottom: 0.3rem;
        position: relative;
        z-index: 1;
    }

    .trust-form p {
        font-size: 0.9rem;
        color: #6b6f76;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }

    .trust-form .form-group {
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }

    .trust-form .form-group label {
        display: block;
        font-size: 0.8rem;
        font-weight: 600;
        color: #0b0f14;
        margin-bottom: 0.3rem;
    }

    .trust-form .form-group input,
    .trust-form .form-group textarea {
        width: 100%;
        padding: 0.7rem 1rem;
        border: 1px solid rgba(11, 15, 20, 0.15);
        border-radius: 4px;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        transition: border-color 0.3s ease;
        background: white;
    }

    .trust-form .form-group input:focus,
    .trust-form .form-group textarea:focus {
        outline: none;
        border-color: #2f5fa8;
        box-shadow: 0 0 0 3px rgba(11, 15, 20, 0.08);
    }

    .trust-form .form-group textarea {
        resize: vertical;
        min-height: 100px;
    }

    .trust-form .btn-primary {
        width: 100%;
        justify-content: center;
        position: relative;
        z-index: 1;
    }

    /* ===== FOOTER — true black, editorial ===== */
    .footer {
        margin-top: 4rem;
        margin-left: -2rem;
        margin-right: -2rem;
        padding: 3.5rem 2rem 1.5rem 2rem;
        background: #0b0f14;
    }

    .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 2rem;
        margin-bottom: 2rem;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }

    .footer-brand p {
        color: rgba(255,255,255,0.45);
        font-size: 0.9rem;
        line-height: 1.6;
        max-width: 300px;
        margin-top: 0.5rem;
    }

    .footer-col h5 {
        font-size: 0.72rem;
        font-weight: 700;
        color: rgba(255,255,255,0.85);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 1rem;
    }

    .footer-col a {
        display: block;
        color: rgba(255,255,255,0.45);
        text-decoration: none;
        font-size: 0.9rem;
        padding: 0.3rem 0;
        transition: color 0.3s ease;
    }

    .footer-col a:hover {
        color: #ffffff;
    }

    .footer-bottom {
        border-top: 1px solid rgba(255,255,255,0.1);
        padding-top: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }

    .footer-bottom p {
        font-size: 0.8rem;
        color: rgba(255,255,255,0.4);
        margin: 0;
    }

    .footer-bottom .social-links {
        display: flex;
        gap: 1.25rem;
    }

    .footer-bottom .social-links a {
        color: rgba(255,255,255,0.45);
        text-decoration: none;
        font-size: 0.85rem;
        transition: color 0.3s ease;
    }

    .footer-bottom .social-links a:hover {
        color: #ffffff;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .navbar {
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .navbar-actions {
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .navbar-actions .nav-link {
            font-size: 0.8rem;
        }
        .navbar-actions .nav-cta {
            padding: 0.4rem 1rem;
            font-size: 0.75rem;
        }
        .hero-title {
            font-size: 2.2rem;
        }
        .hero-description {
            font-size: 1rem;
        }
        .hero-pillars {
            gap: 1rem;
        }
        .section-title {
            font-size: 1.8rem;
        }
        .section-subtitle {
            font-size: 1rem;
        }
        .stats-grid {
            grid-template-columns: 1fr 1fr;
            padding: 2rem 1rem;
        }
        .stat-item-large .number {
            font-size: 2rem;
        }
        .stat-divider {
            display: none;
        }
        .footer-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        .footer-bottom {
            flex-direction: column;
            text-align: center;
        }
        .main > div {
            padding: 0rem 1rem;
        }
        .footer {
            margin-left: -1rem;
            margin-right: -1rem;
            padding: 3rem 1rem 1.5rem 1rem;
        }
        .hero-visual .floating-card {
            padding: 1.5rem;
        }
        .floating-card .stat-grid {
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        .floating-card .stat-number {
            font-size: 1.5rem;
        }
        .trust-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        .section-gradient-blue {
            padding: 2rem 1.5rem;
        }
    }

    @media (max-width: 480px) {
        .hero-title {
            font-size: 1.8rem;
        }
        .hero-actions {
            flex-direction: column;
            width: 100%;
        }
        .hero-actions .btn-primary,
        .hero-actions .btn-secondary {
            width: 100%;
            justify-content: center;
        }
        .products-grid {
            grid-template-columns: 1fr;
        }
        .features-grid {
            grid-template-columns: 1fr;
        }
        .roadmap-grid {
            grid-template-columns: 1fr;
        }
        .stats-grid {
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        .navbar {
            flex-direction: column;
            align-items: flex-start;
        }
        .navbar-actions {
            width: 100%;
            justify-content: flex-start;
        }
        .hero-pillars {
            flex-direction: column;
            gap: 0.5rem;
        }
        .section-gradient-blue {
            padding: 1.5rem 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Inject the card-panel styles defined in branding.py
st.markdown(f"<style>{CARD_CSS}</style>", unsafe_allow_html=True)

# --- LOAD LOGO ---
def load_logo():
    logo_paths = [
        "assets/automation_hub_logo.png",
        "assets/logo.png",
        "assets/Automation_Hub_Logo.png"
    ]
    for path in logo_paths:
        if os.path.exists(path):
            return path
    return None

logo_path = load_logo()

# ============================================================================
# TOP NAVBAR
# ============================================================================
st.markdown('<div class="navbar">', unsafe_allow_html=True)

if logo_path:
    st.markdown(f'''
    <a href="#" class="navbar-brand">
        <img src="data:image/png;base64,{__import__('base64').b64encode(open(logo_path, "rb").read()).decode()}" alt="Automation_Hub Logo">
        <span class="brand-text">Automation_<span>Hub</span></span>
    </a>
    ''', unsafe_allow_html=True)
else:
    st.markdown('''
    <a href="#" class="navbar-brand">
        <span style="font-size:2rem;">🛠️</span>
        <span class="brand-text">Automation_<span>Hub</span></span>
    </a>
    ''', unsafe_allow_html=True)

st.markdown('''
<div class="navbar-actions">
    <a href="#tools" class="nav-link">Tools</a>
    <a href="#trust" class="nav-link">Why Us</a>
    <a href="#pro" class="nav-cta">Get Pro →</a>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# HERO SECTION - COMPLETELY FIXED
# ============================================================================
st.markdown('''
<div class="hero-section">
    <div class="hero-bg-enhanced">
        <div class="grid-pattern"></div>
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
        <div class="blob blob-3"></div>
    </div>
    
    <div class="hero-content-inner">
        <div class="hero-text">
            <div class="hero-badge">
                <span></span> Engineering Automation · v2.0
            </div>
            <h1 class="hero-title">
                Empower Your <span class="highlight">Geotechnical & Materials</span> Projects
            </h1>
            <p class="hero-description">
                Automation_Hub delivers professional-grade tools to increase productivity, ensure standard compliance, and deliver better project outcomes.
            </p>
            <div class="hero-pillars">
                <div class="hero-pillar">
                    <strong>✅ Do more</strong>
                    <span>Streamline complex workflows</span>
                </div>
                <div class="hero-pillar">
                    <strong>✅ Ensure compliance</strong>
                    <span>Meet ASTM, AASHTO & ACI standards</span>
                </div>
                <div class="hero-pillar">
                    <strong>✅ Deliver better reports</strong>
                    <span>Professional PDFs in seconds</span>
                </div>
            </div>
            <div class="hero-actions">
                <a href="#tools" class="btn-primary">Explore Our Solutions →</a>
                <a href="#trust" class="btn-secondary">Why Automation_Hub</a>
            </div>
        </div>
        
        <div class="hero-visual">
            <div class="floating-card">
                <div class="panel-label">Engineering Suite</div>
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.5rem;">
                    <span style="font-size:2rem;">🛠️</span>
                    <div>
                        <div style="font-weight:700; color:#ffffff; font-size:1.1rem;">3 tools available</div>
                        <div style="font-size:0.8rem; color:rgba(255,255,255,0.5);">Free to try, no lock-in</div>
                    </div>
                </div>
                <div class="stat-grid">
                    <div class="stat-item">
                        <div class="stat-number">3</div>
                        <div class="stat-label">Engineering Tools</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">100%</div>
                        <div class="stat-label">Compliant</div>
                    </div>
                </div>
                <div class="tool-preview">
                    <span class="icon">📊</span>
                    <div class="info">
                        <div class="name">AASHTO & USCS Classification</div>
                        <div class="desc">ASTM D2487 · AASHTO M 145</div>
                    </div>
                    <span style="color:#4caf50; font-size:0.8rem; font-weight:600;">Active</span>
                </div>
                <div class="tool-preview">
                    <span class="icon">🧪</span>
                    <div class="info">
                        <div class="name">Concrete Mix Optimizer</div>
                        <div class="desc">ACI 211.1 · Mix Design</div>
                    </div>
                    <span style="color:#4caf50; font-size:0.8rem; font-weight:600;">Active</span>
                </div>
            </div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# ============================================================================
# ENGINEERING SOLUTIONS SECTION
# ============================================================================
st.markdown('<div class="section-container" id="tools">', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-bottom:2rem;">
    <div class="section-label">Our Solutions</div>
    <h2 class="section-title">Product Value for <span>Every Project</span></h2>
    <p class="section-subtitle" style="margin:0 auto;">
        Our software spans engineering disciplines, helping you improve project delivery and asset performance.
    </p>
</div>
<div class="products-grid">
""", unsafe_allow_html=True)

# --- Generate Cards ---
card_keys = ["aashto", "uscs", "concrete"]

for key in card_keys:
    data = get_card_data(key)
    style = get_card_style(key)
    pattern = get_bg_pattern(key)
    svg = get_card_svg(key)
    
    card_html = f"""
    <div class="product-card">
        <div class="card-panel" style="{style}">
            {svg}
            <div class="card-pattern">{pattern}</div>
            <div class="panel-eyebrow">{data['eyebrow']}</div>
        </div>
        <div class="card-body">
            <div class="badge">{data['badge']}</div>
            <h3>{data['title']}</h3>
            <p>{data['description']}</p>
            <div class="card-footer">
                <span class="status"><span class="dot"></span>Free Version</span>
                <a href="{data['link']}" target="_blank" class="btn-ghost" style="font-size:0.85rem;">Try Now →</a>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

st.markdown("""
</div>
<div style="text-align:center; margin-top:2.5rem;">
    <a href="#pro" class="btn-secondary" style="font-size:0.95rem;">🔐 Upgrade to Pro →</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# TECHNOLOGY INNOVATION SECTION
# ============================================================================
st.markdown('''
<div class="section-container" style="padding-top:1rem;">
    <div class="section-gradient-blue">
        <div class="glow-orb blue"></div>
        <div class="glow-orb light-blue"></div>
        
        <div style="text-align:center; margin-bottom:2rem; position:relative; z-index:1;">
            <div class="section-label">Technology Innovation</div>
            <h2 class="section-title">Leverage Data Across the <span>Engineering Lifecycle</span></h2>
            <p class="section-subtitle" style="margin:0 auto;">
                Unlock the value of your data with our AI-powered and automated solutions.
            </p>
        </div>
        <div class="features-grid" style="position:relative; z-index:1;">
            <div class="feature-badge">
                <span class="emoji">🤖</span>
                <div class="content">
                    <h4>Boost Productivity with AI</h4>
                    <p>Automated classification and mix design powered by intelligent algorithms.</p>
                </div>
            </div>
            <div class="feature-badge">
                <span class="emoji">📊</span>
                <div class="content">
                    <h4>3D & Visual Data Insights</h4>
                    <p>Visualize gradation curves and plasticity charts for better understanding.</p>
                </div>
            </div>
            <div class="feature-badge">
                <span class="emoji">📄</span>
                <div class="content">
                    <h4>Seamless Reporting</h4>
                    <p>Generate professional, shareable PDF reports directly from your data.</p>
                </div>
            </div>
            <div class="feature-badge">
                <span class="emoji">☁️</span>
                <div class="content">
                    <h4>Cloud-Based Access</h4>
                    <p>Access your tools and data from anywhere, on any device.</p>
                </div>
            </div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# ============================================================================
# STATISTICS
# ============================================================================
st.markdown('''
<div class="section-container" style="padding-top:0.5rem;">
    <div class="stats-grid">
        <div class="glow-orb"></div>
        <div class="stat-item-large">
            <div class="number">3</div>
            <div class="label">Engineering Tools</div>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item-large">
            <div class="number">100%</div>
            <div class="label">Compliant</div>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item-large">
            <div class="number">🚀</div>
            <div class="label">Production Ready</div>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item-large">
            <div class="number">📈</div>
            <div class="label">Continuous Updates</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# ============================================================================
# COMING SOON ROADMAP
# ============================================================================
st.markdown('''
<div class="section-container" style="padding-top:0.5rem;">
    <div style="text-align:center; margin-bottom:2rem;">
        <div class="section-label">Roadmap</div>
        <h2 class="section-title">What's <span>Coming Soon</span></h2>
        <p class="section-subtitle" style="margin:0 auto;">
            We're constantly expanding our suite of engineering tools.
        </p>
    </div>
    <div class="roadmap-grid">
        <div class="roadmap-item">
            <div class="phase">Phase 1</div>
            <h4>Pro Version Launch</h4>
            <p>Advanced features, batch processing, and priority support for enterprise users.</p>
            <div class="coming-soon">Q4 2025</div>
        </div>
        <div class="roadmap-item">
            <div class="phase">Phase 2</div>
            <h4>API Access</h4>
            <p>RESTful API for integrating our classification engines into your existing workflows.</p>
            <div class="coming-soon">Q1 2026</div>
        </div>
        <div class="roadmap-item">
            <div class="phase">Phase 3</div>
            <h4>Team Collaboration</h4>
            <p>Shared projects, version control, and team management features.</p>
            <div class="coming-soon">Q2 2026</div>
        </div>
        <div class="roadmap-item">
            <div class="phase">Phase 4</div>
            <h4>Mobile App</h4>
            <p>On-the-go access to all tools with a native mobile experience.</p>
            <div class="coming-soon">Q3 2026</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# ============================================================================
# TRUST & CONTACT SECTION
# ============================================================================
st.markdown('''
<div class="section-container" id="trust" style="padding-top:0.5rem;">
    <div style="text-align:center; margin-bottom:2rem;">
        <div class="section-label">Industry Leadership</div>
        <h2 class="section-title">Your Trusted <span>Engineering Partner</span></h2>
        <p class="section-subtitle" style="margin:0 auto;">
            We are the partner of choice for digital delivery and asset analytics.
        </p>
    </div>
    <div class="trust-section">
        <div class="glow-orb"></div>
        <div class="trust-quote">
            <span class="mark">&ldquo;</span>
            <div>
                <span class="quote-text">Built on open standards and full data ownership — no lock-in, no black-box calculations, and every report traceable back to the specification it was built from.</span>
                <span class="quote-attr">Automation_Hub Engineering Team</span>
            </div>
        </div>
        <div class="trust-grid">
            <div class="trust-info">
                <h3>🔒 Built on Trust & Standards</h3>
                <p>We're committed to providing tools that engineers can rely on, with complete transparency and data ownership.</p>
                <div class="trust-item">
                    <div class="icon">🔓</div>
                    <div class="text">
                        <strong>Don't get locked-in</strong>
                        <span>Our tools are free to try, with no long-term commitment or vendor lock-in.</span>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="icon">🛡️</div>
                    <div class="text">
                        <strong>Your data is your data, always</strong>
                        <span>We never use your project data without your explicit consent. Period.</span>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="icon">📋</div>
                    <div class="text">
                        <strong>Committed to standards</strong>
                        <span>Full compliance with ASTM D2487, AASHTO M 145, and ACI 211.1.</span>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="icon">🌍</div>
                    <div class="text">
                        <strong>Built for engineers, by engineers</strong>
                        <span>Every feature is designed with real-world engineering challenges in mind.</span>
                    </div>
                </div>
                <div style="margin-top: 1.5rem;">
                    <a href="mailto:wiafe1713@gmail.com" class="btn-primary">Contact Our Team →</a>
                </div>
            </div>
            <div class="trust-form">
                <div class="glow-orb"></div>
                <h4>📝 Ready to Get Started?</h4>
                <p>Have questions or want to explore Pro access? Reach out to us.</p>
                <form action="mailto:wiafe1713@gmail.com" method="post" enctype="text/plain">
                    <div class="form-group">
                        <label for="name">Your Name</label>
                        <input type="text" id="name" name="name" placeholder="John Doe" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" placeholder="john@example.com" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" placeholder="Tell us how we can help..." required></textarea>
                    </div>
                    <button type="submit" class="btn-primary">
                        Send Message ✉️
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# ============================================================================
# PRO CTA SECTION
# ============================================================================
st.markdown('''
<div class="section-container" id="pro" style="padding-top:0.5rem;">
    <div style="background: #0b0f14;
                border-radius: 6px;
                border-top: 3px solid #b5522a;
                padding: 3.5rem 2.5rem;
                text-align: center;
                color: white;
                position: relative;
                overflow: hidden;">
        <div style="position:absolute; inset:0;
                    background-image:
                        linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
                    background-size:44px 44px;
                    mask-image: radial-gradient(ellipse at 50% 0%, rgba(0,0,0,0.9) 0%, transparent 70%);
                    pointer-events:none; z-index:0;"></div>
        <div style="text-align:center; position:relative; z-index:1;">
            <div class="section-label" style="color:rgba(255,255,255,0.5); justify-content:center;">Pro Access</div>
        </div>
        <h2 style="font-size:2rem; font-weight:800; letter-spacing:-0.5px; margin-bottom:0.5rem; color:white; position:relative; z-index:1;">Ready to unlock the full engineering suite?</h2>
        <p style="font-size:1.05rem; color:rgba(255,255,255,0.6); max-width:500px; margin:0 auto 1.75rem auto; line-height:1.6; position:relative; z-index:1;">
            Advanced features, priority support, and enterprise-grade capabilities for your engineering team.
        </p>
        <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; position:relative; z-index:1;">
            <a href="mailto:wiafe1713@gmail.com" class="btn-primary" style="background:white; color:#0b0f14;">
                Contact Sales →
            </a>
        </div>
        <p style="font-size:0.78rem; color:rgba(255,255,255,0.4); margin-top:1.75rem; position:relative; z-index:1; letter-spacing:0.3px;">
            wiafe1713@gmail.com &nbsp;·&nbsp; +233 (0) 50 136 5878
        </p>
    </div>
</div>
''', unsafe_allow_html=True)


# ============================================================================
# FOOTER
# ============================================================================
current_year = datetime.now().year

st.markdown(f'''
<div class="footer">
    <div class="footer-grid">
        <div class="footer-brand">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                <span style="font-size:1.6rem;">🛠️</span>
                <span style="font-weight:800; font-size:1.15rem; color:#ffffff; text-transform:uppercase; letter-spacing:-0.3px;">Automation_Hub</span>
            </div>
            <p>Smart, practical tools for Geotechnical and Materials Engineers. Built for engineers. Powered by code.</p>
            <div style="margin-top:1rem;">
                <span style="display:inline-block; border:1px solid rgba(255,255,255,0.2); color:rgba(255,255,255,0.6); padding:0.2rem 0.8rem; border-radius:4px; font-size:0.65rem; font-weight:600; letter-spacing:0.5px; text-transform:uppercase;">MIT Licensed</span>
            </div>
        </div>
        <div class="footer-col">
            <h5>Products</h5>
            <a href="https://aashtoclassificationtool.streamlit.app" target="_blank">AASHTO Tool</a>
            <a href="https://uscs-classification-tool.streamlit.app" target="_blank">USCS Tool</a>
            <a href="https://Concreteoptimizationtool.streamlit.app" target="_blank">Concrete Optimizer</a>
        </div>
        <div class="footer-col">
            <h5>Company</h5>
            <a href="#tools">Tools</a>
            <a href="#pro">Pro Access</a>
            <a href="#trust">Why Us</a>
        </div>
        <div class="footer-col">
            <h5>Connect</h5>
            <a href="mailto:wiafe1713@gmail.com">Email</a>
            <a href="https://www.linkedin.com/in/bernard-wiafe-akenteng-p-e-ghie-93005124b" target="_blank">LinkedIn</a>
            <a href="https://github.com/IngBeno28" target="_blank">GitHub</a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© {current_year} Automation_Hub. All rights reserved.</p>
        <div class="social-links">
            <a href="mailto:wiafe1713@gmail.com">Email</a>
            <a href="https://www.linkedin.com/in/bernard-wiafe-akenteng-p-e-ghie-93005124b" target="_blank">LinkedIn</a>
            <a href="https://github.com/IngBeno28" target="_blank">GitHub</a>
        </div>
    </div>
    <div style="text-align:center; margin-top:1.5rem; font-size:0.7rem; color:rgba(255,255,255,0.3); letter-spacing:0.3px;">
        Built for engineers. Powered by code.
    </div>
</div>
''', unsafe_allow_html=True)
