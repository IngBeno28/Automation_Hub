import streamlit as st
from PIL import Image
import base64
import os

# --- Load Logo Function ---
def load_logo():
    logo_path = "logo.png"  # update if your logo filename is different
    if os.path.exists(logo_path):
        return Image.open(logo_path)
    return None

# --- Page Config ---
st.set_page_config(
    page_title="Automation_Hub",
    page_icon="🤖",
    layout="centered"
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo + Header (Centered) ---
logo = load_logo()

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if logo:
    st.image(logo, width=300, use_container_width=False)
else:
    # fallback SVG
    st.markdown("""
        <div style='display:flex; justify-content:center;'>
            <svg width="280" height="280" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="none" stroke="#0d47a1" stroke-width="6"/>
                <path d="M50,10 L50,30 M70,50 L90,50 M50,70 L50,90 M30,50 L10,50" 
                      stroke="#e53935" stroke-width="4" stroke-linecap="round"/>
                <circle cx="50" cy="50" r="30" fill="none" stroke="#42a5f5" stroke-width="4"/>
                <path d="M25,60 L40,45 L60,45 L75,60" 
                      stroke="#43a047" stroke-width="3" fill="none"/>
                <path d="M40,45 L40,30 L60,30 L60,45" 
                      stroke="#43a047" stroke-width="3" fill="none"/>
                <line x1="40" y1="60" x2="40" y2="75" stroke="#0d47a1" stroke-width="2"/>
                <line x1="60" y1="60" x2="60" y2="75" stroke="#0d47a1" stroke-width="2"/>
                <circle cx="50" cy="50" r="8" fill="#ffd700" stroke="#ff9800" stroke-width="2"/>
                <path d="M45,50 L55,50 M50,45 L50,55" stroke="#0d47a1" stroke-width="2"/>
            </svg>
        </div>
    """, unsafe_allow_html=True)

# --- Centered Titles ---
st.markdown("<h1 style='text-align: center; color:#0d47a1;'>Automation_Hub</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:#1565c0;'>Smart, practical tools for Geotechnical and Materials Engineers</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#37474f; font-style: italic;'>Built for engineers. Powered by code.</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <hr>
    <div style='text-align: center; color: grey;'>
        © 2025 Automation_Hub | Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
