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
        background: linear-gradient(180deg, #f8faff 0%, #ffffff 100%);
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

    /* ===== HERO BACKGROUND ENHANCEMENTS ===== */
    .hero-section {
        position: relative;
        overflow: hidden;
        padding: 2rem 1rem 3rem 1rem;
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
            linear-gradient(rgba(13, 71, 161, 0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(13, 71, 161, 0.04) 1px, transparent 1px);
        background-size: 50px 50px;
    }

    .hero-section .hero-bg-enhanced .blob {
        position: absolute;
        border-radius: 50%;
        filter: blur(60px);
    }

    .hero-section .hero-bg-enhanced .blob-1 {
        width: 400px;
        height: 400px;
        background: rgba(13, 71, 161, 0.05);
        top: -100px;
        right: -100px;
        animation: floatBlob 20s ease-in-out infinite;
    }

    .hero-section .hero-bg-enhanced .blob-2 {
        width: 300px;
        height: 300px;
        background: rgba(66, 165, 245, 0.05);
        bottom: -80px;
        left: -80px;
        animation: floatBlob 25s ease-in-out infinite reverse;
    }

    .hero-section .hero-bg-enhanced .blob-3 {
        width: 200px;
        height: 200px;
        background: rgba(13, 71, 161, 0.03);
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        animation: floatBlob 30s ease-in-out infinite;
    }

    @keyframes floatBlob {
        0%, 100% { transform: translate(0, 0) scale(1); }
        33% { transform: translate(30px, -30px) scale(1.05); }
        66% { transform: translate(-20px, 20px) scale(0.95); }
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
        background: linear-gradient(135deg, #e8f0fe 0%, #f8faff 100%);
        border-radius: 24px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }

    .glow-orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        pointer-events: none;
        z-index: 0;
    }

    .glow-orb.blue {
        width: 300px;
        height: 300px;
        background: rgba(13, 71, 161, 0.06);
        top: -100px;
        right: -50px;
    }

    .glow-orb.light-blue {
        width: 250px;
        height: 250px;
        background: rgba(66, 165, 245, 0.05);
        bottom: -80px;
        left: -50px;
    }

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
        border-bottom: 1px solid rgba(13, 71, 161, 0.06);
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
        font-weight: 700;
        font-size: 1.3rem;
        color: #0a1e3c;
        letter-spacing: -0.5px;
    }

    .navbar-brand .brand-text span {
        color: #0d47a1;
    }

    .navbar-actions {
        display: flex;
        gap: 1rem;
        align-items: center;
    }

    .navbar-actions .nav-link {
        color: #5a6a7e;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        transition: color 0.3s ease;
        padding: 0.4rem 0;
    }

    .navbar-actions .nav-link:hover {
        color: #0d47a1;
    }

    .navbar-actions .nav-cta {
        background: #0d47a1;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.85rem;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.2);
    }

    .navbar-actions .nav-cta:hover {
        background: #0a3578;
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(13, 71, 161, 0.3);
        color: white;
    }

    /* ===== CONTAINER UTILITIES ===== */
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 4rem 1rem;
    }

    .section-label {
        display: inline-block;
        background: rgba(13, 71, 161, 0.08);
        color: #0d47a1;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0a1e3c;
        line-height: 1.2;
        margin-bottom: 0.75rem;
    }

    .section-title span {
        background: linear-gradient(135deg, #0d47a1, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .section-subtitle {
        font-size: 1.2rem;
        color: #5a6a7e;
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
        gap: 0.5rem;
        background: rgba(13, 71, 161, 0.08);
        padding: 0.3rem 1rem 0.3rem 0.3rem;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 500;
        color: #0d47a1;
        margin-bottom: 1.5rem;
    }

    .hero-badge span {
        background: #0d47a1;
        color: white;
        padding: 0.15rem 0.7rem;
        border-radius: 20px;
        font-weight: 600;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        color: #0a1e3c;
        line-height: 1.1;
        margin-bottom: 1.5rem;
    }

    .hero-title .highlight {
        background: linear-gradient(135deg, #0d47a1, #1e88e5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-description {
        font-size: 1.2rem;
        color: #5a6a7e;
        line-height: 1.8;
        max-width: 500px;
        margin-bottom: 2rem;
    }

    .hero-pillars {
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }

    .hero-pillar {
        flex: 1;
        min-width: 140px;
    }

    .hero-pillar strong {
        display: block;
        font-size: 1rem;
        color: #0a1e3c;
        margin-bottom: 0.2rem;
    }

    .hero-pillar span {
        font-size: 0.9rem;
        color: #5a6a7e;
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
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(13, 71, 161, 0.12);
        border: 1px solid rgba(13, 71, 161, 0.06);
        width: 100%;
        max-width: 400px;
        position: relative;
        transition: transform 0.3s ease;
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.85);
    }

    .hero-visual .floating-card:hover {
        transform: translateY(-5px);
    }

    .floating-card .stat-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 1rem;
    }

    .floating-card .stat-item {
        text-align: center;
    }

    .floating-card .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #0d47a1;
        line-height: 1;
    }

    .floating-card .stat-label {
        font-size: 0.8rem;
        color: #5a6a7e;
        margin-top: 0.3rem;
    }

    .floating-card .tool-preview {
        display: flex;
        gap: 0.8rem;
        align-items: center;
        padding: 0.8rem 1rem;
        background: #f8faff;
        border-radius: 12px;
        margin-top: 1rem;
        border-left: 4px solid #0d47a1;
    }

    .floating-card .tool-preview .icon {
        font-size: 1.5rem;
    }

    .floating-card .tool-preview .info {
        flex: 1;
    }

    .floating-card .tool-preview .info .name {
        font-weight: 600;
        color: #0a1e3c;
        font-size: 0.9rem;
    }

    .floating-card .tool-preview .info .desc {
        font-size: 0.75rem;
        color: #5a6a7e;
    }

    /* ===== BUTTONS ===== */
    .btn-primary {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #0d47a1;
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(13, 71, 161, 0.25);
        font-family: 'Inter', sans-serif;
    }

    .btn-primary:hover {
        background: #0a3578;
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(13, 71, 161, 0.35);
        color: white;
    }

    .btn-secondary {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: transparent;
        color: #0d47a1;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        border: 2px solid rgba(13, 71, 161, 0.2);
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }

    .btn-secondary:hover {
        background: rgba(13, 71, 161, 0.05);
        border-color: #0d47a1;
        transform: translateY(-2px);
    }

    .btn-ghost {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #0d47a1;
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
        color: #0a3578;
    }

    /* ===== PRODUCT CARDS ===== */
    .products-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .product-card {
        border-radius: 24px;
        padding: 2rem 1.5rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.04);
        min-height: 320px;
        display: flex;
        flex-direction: column;
        background: white;
    }

    .product-card .card-bg-pattern {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(13, 71, 161, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(66, 165, 245, 0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
        border-radius: 24px;
    }

    .product-card .icon-circle {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin-bottom: 1.2rem;
        background: rgba(13, 71, 161, 0.06);
        transition: all 0.3s ease;
        z-index: 1;
    }

    .product-card:hover .icon-circle {
        background: rgba(13, 71, 161, 0.12);
        transform: scale(1.05);
    }

    .product-card .badge {
        display: inline-block;
        background: rgba(13, 71, 161, 0.08);
        color: #0d47a1;
        padding: 0.15rem 0.7rem;
        border-radius: 12px;
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        margin-bottom: 0.8rem;
        align-self: flex-start;
        z-index: 1;
    }

    .product-card h3 {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.5rem;
        z-index: 1;
    }

    .product-card p {
        color: #5a6a7e;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        flex: 1;
        z-index: 1;
    }

    .product-card .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 1rem;
        border-top: 1px solid rgba(13, 71, 161, 0.06);
        margin-top: auto;
        z-index: 1;
    }

    .product-card .card-footer .status {
        font-size: 0.75rem;
        color: #5a6a7e;
        font-weight: 500;
    }

    .product-card .card-footer .status .dot {
        display: inline-block;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        margin-right: 6px;
        background: #4caf50;
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
        border-radius: 16px;
        border: 1px solid rgba(13, 71, 161, 0.06);
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(13, 71, 161, 0.02);
    }

    .feature-badge:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(13, 71, 161, 0.08);
        border-color: rgba(13, 71, 161, 0.12);
    }

    .feature-badge .emoji {
        font-size: 1.8rem;
        flex-shrink: 0;
    }

    .feature-badge .content h4 {
        font-size: 0.95rem;
        font-weight: 600;
        color: #0a1e3c;
        margin-bottom: 0.1rem;
    }

    .feature-badge .content p {
        font-size: 0.8rem;
        color: #5a6a7e;
        margin: 0;
    }

    /* ===== STATISTICS ===== */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
        background: white;
        border-radius: 24px;
        padding: 3rem 2rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.03);
        position: relative;
        overflow: hidden;
    }

    .stats-grid .glow-orb {
        width: 200px;
        height: 200px;
        background: rgba(13, 71, 161, 0.03);
        top: -50px;
        right: -50px;
        filter: blur(60px);
    }

    .stat-item-large {
        text-align: center;
        position: relative;
        z-index: 1;
    }

    .stat-item-large .number {
        font-size: 2.8rem;
        font-weight: 900;
        color: #0d47a1;
        line-height: 1;
    }

    .stat-item-large .label {
        font-size: 0.9rem;
        color: #5a6a7e;
        margin-top: 0.3rem;
        font-weight: 500;
    }

    .stat-divider {
        width: 1px;
        background: #e8edf4;
        margin: 0 auto;
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
        border-radius: 20px;
        padding: 1.8rem 1.5rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .roadmap-item:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(13, 71, 161, 0.06);
    }

    .roadmap-item .phase {
        display: inline-block;
        background: rgba(13, 71, 161, 0.06);
        color: #0d47a1;
        padding: 0.15rem 0.7rem;
        border-radius: 12px;
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }

    .roadmap-item h4 {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.3rem;
    }

    .roadmap-item p {
        font-size: 0.85rem;
        color: #5a6a7e;
        line-height: 1.5;
        margin: 0;
    }

    .roadmap-item .coming-soon {
        display: inline-block;
        background: #fff3e0;
        color: #e65100;
        padding: 0.15rem 0.7rem;
        border-radius: 12px;
        font-size: 0.6rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.8rem;
    }

    /* ===== TRUST & CONTACT SECTION ===== */
    .trust-section {
        background: white;
        border-radius: 24px;
        padding: 3rem 2.5rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.03);
        margin-top: 2rem;
        position: relative;
        overflow: hidden;
    }

    .trust-section .glow-orb {
        width: 300px;
        height: 300px;
        background: rgba(13, 71, 161, 0.03);
        top: -100px;
        right: -50px;
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
        color: #0a1e3c;
        margin-bottom: 0.5rem;
    }

    .trust-info p {
        color: #5a6a7e;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .trust-info .trust-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(13, 71, 161, 0.04);
    }

    .trust-info .trust-item:last-child {
        border-bottom: none;
    }

    .trust-info .trust-item .icon {
        font-size: 1.3rem;
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(13, 71, 161, 0.06);
        border-radius: 10px;
        flex-shrink: 0;
        margin-top: 0.1rem;
    }

    .trust-info .trust-item .text strong {
        display: block;
        font-size: 0.95rem;
        color: #0a1e3c;
        margin-bottom: 0.1rem;
    }

    .trust-info .trust-item .text span {
        font-size: 0.9rem;
        color: #5a6a7e;
    }

    .trust-form {
        background: #f8faff;
        border-radius: 16px;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
    }

    .trust-form .glow-orb {
        width: 150px;
        height: 150px;
        background: rgba(66, 165, 245, 0.04);
        bottom: -50px;
        right: -30px;
    }

    .trust-form h4 {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.3rem;
        position: relative;
        z-index: 1;
    }

    .trust-form p {
        font-size: 0.9rem;
        color: #5a6a7e;
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
        color: #0a1e3c;
        margin-bottom: 0.3rem;
    }

    .trust-form .form-group input,
    .trust-form .form-group textarea {
        width: 100%;
        padding: 0.7rem 1rem;
        border: 1px solid rgba(13, 71, 161, 0.1);
        border-radius: 10px;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        transition: border-color 0.3s ease;
        background: white;
    }

    .trust-form .form-group input:focus,
    .trust-form .form-group textarea:focus {
        outline: none;
        border-color: #0d47a1;
        box-shadow: 0 0 0 3px rgba(13, 71, 161, 0.08);
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

    /* ===== FOOTER ===== */
    .footer {
        margin-top: 4rem;
        padding: 3rem 0 1.5rem 0;
        border-top: 1px solid rgba(13, 71, 161, 0.06);
    }

    .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 2rem;
        margin-bottom: 2rem;
    }

    .footer-brand p {
        color: #5a6a7e;
        font-size: 0.9rem;
        line-height: 1.6;
        max-width: 300px;
        margin-top: 0.5rem;
    }

    .footer-col h5 {
        font-size: 0.8rem;
        font-weight: 700;
        color: #0a1e3c;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 1rem;
    }

    .footer-col a {
        display: block;
        color: #5a6a7e;
        text-decoration: none;
        font-size: 0.9rem;
        padding: 0.3rem 0;
        transition: color 0.3s ease;
    }

    .footer-col a:hover {
        color: #0d47a1;
    }

    .footer-bottom {
        border-top: 1px solid rgba(13, 71, 161, 0.06);
        padding-top: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .footer-bottom p {
        font-size: 0.8rem;
        color: #5a6a7e;
        margin: 0;
    }

    .footer-bottom .social-links {
        display: flex;
        gap: 1rem;
    }

    .footer-bottom .social-links a {
        color: #5a6a7e;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s ease;
    }

    .footer-bottom .social-links a:hover {
        color: #0d47a1;
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
                <span>🚀</span> Engineering Automation · v2.0
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
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:1rem;">
                    <span style="font-size:2rem;">🛠️</span>
                    <div>
                        <div style="font-weight:700; color:#0a1e3c; font-size:1.1rem;">Engineering Suite</div>
                        <div style="font-size:0.8rem; color:#5a6a7e;">3 powerful tools available</div>
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
                <div class="tool-preview" style="border-left-color:#42a5f5;">
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
    <div class="product-card" style="{style}">
        <div class="card-bg-pattern"></div>
        {svg}
        <div class="card-pattern">{pattern}</div>
        <div class="deco-badge">{data['icon']}</div>
        <div class="icon-circle">{data['icon']}</div>
        <div class="badge">{data['badge']}</div>
        <h3>{data['title']}</h3>
        <p>{data['description']}</p>
        <div class="card-footer">
            <span class="status"><span class="dot"></span>Free Version</span>
            <a href="{data['link']}" target="_blank" class="btn-ghost" style="font-size:0.85rem;">Try Now →</a>
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
    <div style="background: linear-gradient(135deg, #0d47a1 0%, #1a237e 100%); 
                border-radius: 24px; 
                padding: 3rem 2.5rem; 
                text-align: center;
                color: white;
                box-shadow: 0 20px 60px rgba(13, 71, 161, 0.25);
                position: relative;
                overflow: hidden;">
        <div style="position:absolute; top:-100px; right:-100px; width:300px; height:300px; background:rgba(255,255,255,0.03); border-radius:50%; filter:blur(60px);"></div>
        <div style="position:absolute; bottom:-80px; left:-80px; width:200px; height:200px; background:rgba(255,255,255,0.02); border-radius:50%; filter:blur(60px);"></div>
        <div style="font-size:3rem; margin-bottom:1rem; position:relative; z-index:1;">🔐</div>
        <h2 style="font-size:2rem; font-weight:800; margin-bottom:0.5rem; color:white; position:relative; z-index:1;">Ready for Pro Access?</h2>
        <p style="font-size:1.1rem; opacity:0.9; max-width:500px; margin:0 auto 1.5rem auto; line-height:1.6; position:relative; z-index:1;">
            Unlock advanced features, priority support, and enterprise-grade capabilities for your engineering team.
        </p>
        <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; position:relative; z-index:1;">
            <a href="mailto:wiafe1713@gmail.com" class="btn-primary" style="background:white; color:#0d47a1; box-shadow:0 4px 20px rgba(255,255,255,0.2);">
                Contact Sales →
            </a>
        </div>
        <p style="font-size:0.8rem; opacity:0.7; margin-top:1.5rem; position:relative; z-index:1;">
            📩 wiafe1713@gmail.com · 📱 +233 (0) 50 136 5878
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
                <span style="font-size:1.8rem;">🛠️</span>
                <span style="font-weight:800; font-size:1.3rem; color:#0a1e3c;">Automation_Hub</span>
            </div>
            <p>Smart, practical tools for Geotechnical and Materials Engineers. Built for engineers. Powered by code.</p>
            <div style="margin-top:1rem;">
                <span style="display:inline-block; background:rgba(13,71,161,0.06); color:#0d47a1; padding:0.2rem 1rem; border-radius:12px; font-size:0.7rem; font-weight:600;">MIT Licensed</span>
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
            <a href="mailto:wiafe1713@gmail.com">✉️ Email</a>
            <a href="https://www.linkedin.com/in/bernard-wiafe-akenteng-p-e-ghie-93005124b" target="_blank">🔗 LinkedIn</a>
            <a href="https://github.com/IngBeno28" target="_blank">🐙 GitHub</a>
        </div>
    </div>
    <div style="text-align:center; margin-top:1.5rem; font-size:0.7rem; color:#b0bec5;">
        Built for engineers. Powered by code.
    </div>
</div>
''', unsafe_allow_html=True)
