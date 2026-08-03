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
    # CARD_CSS  # Uncomment if you want to use it in your main file
)

# --- Page Configuration ---
st.set_page_config(
    page_title="Automation_Hub | Engineering Solutions",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (Premium SaaS Design) ---
st.markdown(f"""
<style>
    /* ===== GLOBAL RESET & BASE ===== */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    /* Hide default Streamlit elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    .stApp {{
        background: linear-gradient(180deg, #f8faff 0%, #ffffff 100%);
    }}

    .main > div {{
        padding: 0rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }}

    /* ===== TYPOGRAPHY ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    html, body, h1, h2, h3, h4, h5, h6, p, div, span, button {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* ===== TOP NAVBAR ===== */
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(13, 71, 161, 0.06);
        margin-bottom: 1rem;
    }}

    .navbar-brand {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        text-decoration: none;
    }}

    .navbar-brand img {{
        height: 40px;
        width: auto;
    }}

    .navbar-brand .brand-text {{
        font-weight: 700;
        font-size: 1.3rem;
        color: #0a1e3c;
        letter-spacing: -0.5px;
    }}

    .navbar-brand .brand-text span {{
        color: #0d47a1;
    }}

    .navbar-actions {{
        display: flex;
        gap: 1rem;
        align-items: center;
    }}

    .navbar-actions .nav-link {{
        color: #5a6a7e;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        transition: color 0.3s ease;
        padding: 0.4rem 0;
    }}

    .navbar-actions .nav-link:hover {{
        color: #0d47a1;
    }}

    .navbar-actions .nav-cta {{
        background: #0d47a1;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.85rem;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.2);
    }}

    .navbar-actions .nav-cta:hover {{
        background: #0a3578;
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(13, 71, 161, 0.3);
        color: white;
    }}

    /* ===== CONTAINER UTILITIES ===== */
    .section-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 4rem 1rem;
    }}

    .section-label {{
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
    }}

    .section-title {{
        font-size: 2.5rem;
        font-weight: 800;
        color: #0a1e3c;
        line-height: 1.2;
        margin-bottom: 0.75rem;
    }}

    .section-title span {{
        background: linear-gradient(135deg, #0d47a1, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}

    .section-subtitle {{
        font-size: 1.2rem;
        color: #5a6a7e;
        font-weight: 400;
        line-height: 1.6;
        max-width: 600px;
    }}

    .text-center {{
        text-align: center;
        margin-left: auto;
        margin-right: auto;
    }}

    /* ===== HERO SECTION ===== */
    .hero-section {{
        padding: 2rem 1rem 3rem 1rem;
        position: relative;
        overflow: hidden;
    }}

    .hero-section::before {{
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(13, 71, 161, 0.05) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }}

    .hero-section::after {{
        content: '';
        position: absolute;
        bottom: -30%;
        left: -10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(66, 165, 245, 0.05) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }}

    .hero-content {{
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        gap: 4rem;
        flex-wrap: wrap;
    }}

    .hero-text {{
        flex: 1 1 50%;
        min-width: 300px;
    }}

    .hero-badge {{
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
    }}

    .hero-badge span {{
        background: #0d47a1;
        color: white;
        padding: 0.15rem 0.7rem;
        border-radius: 20px;
        font-weight: 600;
    }}

    .hero-title {{
        font-size: 3.5rem;
        font-weight: 900;
        color: #0a1e3c;
        line-height: 1.1;
        margin-bottom: 1.5rem;
    }}

    .hero-title .highlight {{
        background: linear-gradient(135deg, #0d47a1, #1e88e5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}

    .hero-description {{
        font-size: 1.2rem;
        color: #5a6a7e;
        line-height: 1.8;
        max-width: 500px;
        margin-bottom: 2rem;
    }}

    .hero-pillars {{
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }}

    .hero-pillar {{
        flex: 1;
        min-width: 140px;
    }}

    .hero-pillar strong {{
        display: block;
        font-size: 1rem;
        color: #0a1e3c;
        margin-bottom: 0.2rem;
    }}

    .hero-pillar span {{
        font-size: 0.9rem;
        color: #5a6a7e;
    }}

    .hero-actions {{
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        align-items: center;
    }}

    .hero-visual {{
        flex: 1 1 40%;
        min-width: 280px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }}

    .hero-visual .floating-card {{
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
    }}

    .hero-visual .floating-card:hover {{
        transform: translateY(-5px);
    }}

    .floating-card .stat-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 1rem;
    }}

    .floating-card .stat-item {{
        text-align: center;
    }}

    .floating-card .stat-number {{
        font-size: 2rem;
        font-weight: 800;
        color: #0d47a1;
        line-height: 1;
    }}

    .floating-card .stat-label {{
        font-size: 0.8rem;
        color: #5a6a7e;
        margin-top: 0.3rem;
    }}

    .floating-card .tool-preview {{
        display: flex;
        gap: 0.8rem;
        align-items: center;
        padding: 0.8rem 1rem;
        background: #f8faff;
        border-radius: 12px;
        margin-top: 1rem;
        border-left: 4px solid #0d47a1;
    }}

    .floating-card .tool-preview .icon {{
        font-size: 1.5rem;
    }}

    .floating-card .tool-preview .info {{
        flex: 1;
    }}

    .floating-card .tool-preview .info .name {{
        font-weight: 600;
        color: #0a1e3c;
        font-size: 0.9rem;
    }}

    .floating-card .tool-preview .info .desc {{
        font-size: 0.75rem;
        color: #5a6a7e;
    }}

    /* ===== BUTTONS ===== */
    .btn-primary {{
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
    }}

    .btn-primary:hover {{
        background: #0a3578;
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(13, 71, 161, 0.35);
        color: white;
    }}

    .btn-secondary {{
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
    }}

    .btn-secondary:hover {{
        background: rgba(13, 71, 161, 0.05);
        border-color: #0d47a1;
        transform: translateY(-2px);
    }}

    .btn-ghost {{
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
    }}

    .btn-ghost:hover {{
        gap: 0.8rem;
        color: #0a3578;
    }}

    /* ===== PRODUCT CARDS (Enhanced with branding) ===== */
    .products-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }}

    .product-card {{
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
    }}

    /* Gradient top border accent */
    .product-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #0d47a1, #42a5f5);
        opacity: 0;
        transition: opacity 0.4s ease;
    }}

    .product-card:hover::before {{
        opacity: 1;
    }}

    .product-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 20px 60px rgba(13, 71, 161, 0.10);
        border-color: rgba(13, 71, 161, 0.12);
    }}

    /* Pattern overlay for visual depth */
    .product-card .card-pattern {{
        position: absolute;
        bottom: -5px;
        right: -5px;
        font-size: 5rem;
        opacity: 0.04;
        pointer-events: none;
        user-select: none;
        line-height: 1;
        z-index: 0;
        transition: all 0.6s ease;
    }}

    .product-card:hover .card-pattern {{
        transform: scale(1.1) rotate(-5deg);
        opacity: 0.06;
    }}

    /* Card content sits above background */
    .product-card > *:not(.card-pattern) {{
        position: relative;
        z-index: 1;
    }}

    .product-card .icon-circle {{
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
    }}

    .product-card:hover .icon-circle {{
        background: rgba(13, 71, 161, 0.12);
        transform: scale(1.05);
    }}

    .product-card .badge {{
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
    }}

    .product-card h3 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.5rem;
    }}

    .product-card p {{
        color: #5a6a7e;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        flex: 1;
    }}

    .product-card .card-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 1rem;
        border-top: 1px solid rgba(13, 71, 161, 0.06);
        margin-top: auto;
    }}

    .product-card .card-footer .status {{
        font-size: 0.75rem;
        color: #5a6a7e;
        font-weight: 500;
    }}

    .product-card .card-footer .status .dot {{
        display: inline-block;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        margin-right: 6px;
        background: #4caf50;
    }}

    /* Decorative floating badge */
    .product-card .deco-badge {{
        position: absolute;
        top: 12px;
        right: 12px;
        background: rgba(13, 71, 161, 0.04);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
        transition: all 0.3s ease;
        z-index: 1;
    }}

    .product-card:hover .deco-badge {{
        background: rgba(13, 71, 161, 0.10);
        transform: rotate(15deg);
    }}

    /* ===== FEATURE BADGES ===== */
    .features-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }}

    .feature-badge {{
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1.2rem 1.5rem;
        background: white;
        border-radius: 16px;
        border: 1px solid rgba(13, 71, 161, 0.06);
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(13, 71, 161, 0.02);
    }}

    .feature-badge:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(13, 71, 161, 0.08);
        border-color: rgba(13, 71, 161, 0.12);
    }}

    .feature-badge .emoji {{
        font-size: 1.8rem;
        flex-shrink: 0;
    }}

    .feature-badge .content h4 {{
        font-size: 0.95rem;
        font-weight: 600;
        color: #0a1e3c;
        margin-bottom: 0.1rem;
    }}

    .feature-badge .content p {{
        font-size: 0.8rem;
        color: #5a6a7e;
        margin: 0;
    }}

    /* ===== STATISTICS ===== */
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
        background: white;
        border-radius: 24px;
        padding: 3rem 2rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.03);
    }}

    .stat-item-large {{
        text-align: center;
    }}

    .stat-item-large .number {{
        font-size: 2.8rem;
        font-weight: 900;
        color: #0d47a1;
        line-height: 1;
    }}

    .stat-item-large .label {{
        font-size: 0.9rem;
        color: #5a6a7e;
        margin-top: 0.3rem;
        font-weight: 500;
    }}

    .stat-divider {{
        width: 1px;
        background: #e8edf4;
        margin: 0 auto;
    }}

    /* ===== ROADMAP ===== */
    .roadmap-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }}

    .roadmap-item {{
        background: white;
        border-radius: 20px;
        padding: 1.8rem 1.5rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        transition: all 0.3s ease;
        position: relative;
    }}

    .roadmap-item:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(13, 71, 161, 0.06);
    }}

    .roadmap-item .phase {{
        display: inline-block;
        background: rgba(13, 71, 161, 0.06);
        color: #0d47a1;
        padding: 0.15rem 0.7rem;
        border-radius: 12px;
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }}

    .roadmap-item h4 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.3rem;
    }}

    .roadmap-item p {{
        font-size: 0.85rem;
        color: #5a6a7e;
        line-height: 1.5;
        margin: 0;
    }}

    .roadmap-item .coming-soon {{
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
    }}

    /* ===== TRUST & CONTACT SECTION ===== */
    .trust-section {{
        background: white;
        border-radius: 24px;
        padding: 3rem 2.5rem;
        border: 1px solid rgba(13, 71, 161, 0.06);
        box-shadow: 0 2px 10px rgba(13, 71, 161, 0.03);
        margin-top: 2rem;
    }}

    .trust-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
        align-items: start;
    }}

    .trust-info h3 {{
        font-size: 1.5rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.5rem;
    }}

    .trust-info p {{
        color: #5a6a7e;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }}

    .trust-info .trust-item {{
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(13, 71, 161, 0.04);
    }}

    .trust-info .trust-item:last-child {{
        border-bottom: none;
    }}

    .trust-info .trust-item .icon {{
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
    }}

    .trust-info .trust-item .text strong {{
        display: block;
        font-size: 0.95rem;
        color: #0a1e3c;
        margin-bottom: 0.1rem;
    }}

    .trust-info .trust-item .text span {{
        font-size: 0.9rem;
        color: #5a6a7e;
    }}

    .trust-form {{
        background: #f8faff;
        border-radius: 16px;
        padding: 1.5rem;
    }}

    .trust-form h4 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: #0a1e3c;
        margin-bottom: 0.3rem;
    }}

    .trust-form p {{
        font-size: 0.9rem;
        color: #5a6a7e;
        margin-bottom: 1.5rem;
    }}

    .trust-form .form-group {{
        margin-bottom: 1rem;
    }}

    .trust-form .form-group label {{
        display: block;
        font-size: 0.8rem;
        font-weight: 600;
        color: #0a1e3c;
        margin-bottom: 0.3rem;
    }}

    .trust-form .form-group input,
    .trust-form .form-group textarea {{
        width: 100%;
        padding: 0.7rem 1rem;
        border: 1px solid rgba(13, 71, 161, 0.1);
        border-radius: 10px;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        transition: border-color 0.3s ease;
        background: white;
    }}

    .trust-form .form-group input:focus,
    .trust-form .form-group textarea:focus {{
        outline: none;
        border-color: #0d47a1;
        box-shadow: 0 0 0 3px rgba(13, 71, 161, 0.08);
    }}

    .trust-form .form-group textarea {{
        resize: vertical;
        min-height: 100px;
    }}

    /* ===== FOOTER ===== */
    .footer {{
        margin-top: 4rem;
        padding: 3rem 0 1.5rem 0;
        border-top: 1px solid rgba(13, 71, 161, 0.06);
    }}

    .footer-grid {{
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 2rem;
        margin-bottom: 2rem;
    }}

    .footer-brand p {{
        color: #5a6a7e;
        font-size: 0.9rem;
        line-height: 1.6;
        max-width: 300px;
        margin-top: 0.5rem;
    }}

    .footer-col h5 {{
        font-size: 0.8rem;
        font-weight: 700;
        color: #0a1e3c;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 1rem;
    }}

    .footer-col a {{
        display: block;
        color: #5a6a7e;
        text-decoration: none;
        font-size: 0.9rem;
        padding: 0.3rem 0;
        transition: color 0.3s ease;
    }}

    .footer-col a:hover {{
        color: #0d47a1;
    }}

    .footer-bottom {{
        border-top: 1px solid rgba(13, 71, 161, 0.06);
        padding-top: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }}

    .footer-bottom p {{
        font-size: 0.8rem;
        color: #5a6a7e;
        margin: 0;
    }}

    .footer-bottom .social-links {{
        display: flex;
        gap: 1rem;
    }}

    .footer-bottom .social-links a {{
        color: #5a6a7e;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s ease;
    }}

    .footer-bottom .social-links a:hover {{
        color: #0d47a1;
    }}

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {{
        .navbar {{
            flex-wrap: wrap;
            gap: 0.5rem;
        }}
        .navbar-actions {{
            flex-wrap: wrap;
            gap: 0.5rem;
        }}
        .navbar-actions .nav-link {{
            font-size: 0.8rem;
        }}
        .navbar-actions .nav-cta {{
            padding: 0.4rem 1rem;
            font-size: 0.75rem;
        }}
        .hero-section {{
            padding: 1rem 0 2rem 0;
        }}
        .hero-title {{
            font-size: 2.2rem;
        }}
        .hero-description {{
            font-size: 1rem;
        }}
        .hero-pillars {{
            gap: 1rem;
        }}
        .section-title {{
            font-size: 1.8rem;
        }}
        .section-subtitle {{
            font-size: 1rem;
        }}
        .stats-grid {{
            grid-template-columns: 1fr 1fr;
            padding: 2rem 1rem;
        }}
        .stat-item-large .number {{
            font-size: 2rem;
        }}
        .stat-divider {{
            display: none;
        }}
        .footer-grid {{
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }}
        .footer-bottom {{
            flex-direction: column;
            text-align: center;
        }}
        .main > div {{
            padding: 0rem 1rem;
        }}
        .hero-visual .floating-card {{
            padding: 1.5rem;
        }}
        .floating-card .stat-grid {{
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }}
        .floating-card .stat-number {{
            font-size: 1.5rem;
        }}
        .trust-grid {{
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }}
    }}

    @media (max-width: 480px) {{
        .hero-title {{
            font-size: 1.8rem;
        }}
        .hero-actions {{
            flex-direction: column;
            width: 100%;
        }}
        .hero-actions .btn-primary,
        .hero-actions .btn-secondary {{
            width: 100%;
            justify-content: center;
        }}
        .products-grid {{
            grid-template-columns: 1fr;
        }}
        .features-grid {{
            grid-template-columns: 1fr;
        }}
        .roadmap-grid {{
            grid-template-columns: 1fr;
        }}
        .stats-grid {{
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }}
        .navbar {{
            flex-direction: column;
            align-items: flex-start;
        }}
        .navbar-actions {{
            width: 100%;
            justify-content: flex-start;
        }}
        .hero-pillars {{
            flex-direction: column;
            gap: 0.5rem;
        }}
    }}

    /* ===== UTILITY ===== */
    .mt-1 {{ margin-top: 1rem; }}
    .mt-2 {{ margin-top: 2rem; }}
    .mt-3 {{ margin-top: 3rem; }}
    .mb-1 {{ margin-bottom: 1rem; }}
    .mb-2 {{ margin-bottom: 2rem; }}
    .gap-1 {{ gap: 1rem; }}
    .gap-2 {{ gap: 2rem; }}
    .flex {{ display: flex; }}
    .flex-center {{ display: flex; align-items: center; justify-content: center; }}
    .flex-between {{ display: flex; justify-content: space-between; align-items: center; }}
    .flex-wrap {{ flex-wrap: wrap; }}
</style>
""", unsafe_allow_html=True)

# --- LOAD LOGO ---
def load_logo():
    """Load logo from assets folder with fallback."""
    logo_paths = [
        "assets/automation_hub_logo.png",
        "assets/logo.png",
        "assets/Automation_Hub_Logo.png"  # Added case variation
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

# Logo and Brand
if logo_path:
    st.markdown(f'''
    <a href="#" class="navbar-brand">
        <img src="data:image/png;base64,{__import__('base64').b64encode(open(logo_path, "rb").read()).decode()}" alt="Automation_Hub Logo">
        <span class="brand-text">Automation_<span>Hub</span></span>
    </a>
    ''', unsafe_allow_html=True)
else:
    st.markdown('''
    <a href="#"
