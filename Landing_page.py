import streamlit as st
from PIL import Image
import os
from aci_mix_landing_view import show_pro_landing

# Page config
st.set_page_config(
    page_title="Automation_Hub | Civil Engineering Tools",
    page_icon="🛠️",
    layout="wide"
)

# Styling
st.markdown("""
    <style>
    body {
        background-color: #f4f9ff;
    }
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }
    /* ✅ Responsive Logo */
    .logo {
        max-width: 200px;   /* laptop/desktop size */
        width: 50%;         /* scale relative to container */
        height: auto;       /* keep aspect ratio */
    }
    @media (max-width: 768px) {  /* phones & tablets */
        .logo {
            max-width: 150px;   /* smaller for mobile */
        }
    }
    .header-title {
        color: #0d47a1;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .header-subtitle {
        color: #1565c0;
        margin-top: 5px;
    }
    .header-tagline {
        color: #37474f;
        font-style: italic;
    }
    hr {
        border: 1px solid #90caf9;
    }
    .stButton>button {
        background-color: #1565c0;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #0d47a1;
        color: #e3f2fd;
    }
    </style>
""", unsafe_allow_html=True)

# Function to load logo from assets folder
def load_logo():
    logo_paths = [
        "assets/automation_hub_logo.png",
        "assets/logo.png",
        "assets/automation_hub_logo.jpg",
        "assets/logo.jpg",
        "assets/automation_hub_logo.svg",
        "assets/logo.svg"
    ]
    
    for path in logo_paths:
        if os.path.exists(path):
            try:
                return path  # return the path instead of Image object
            except Exception as e:
                st.warning(f"Could not load logo from {path}: {str(e)}")
    
    return None  # No logo found

# Logo + Header - Perfectly centered
logo_path = load_logo()

st.markdown('<div class="centered-container">', unsafe_allow_html=True)

if logo_path:
    # ✅ Use <img> tag with responsive CSS
    st.markdown(f"<img src='{logo_path}' class='logo'>", unsafe_allow_html=True)
else:
    # Fallback to inline SVG (already scalable)
    st.markdown("""
        <svg class="logo" viewBox="0 0 100 100">
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
    """, unsafe_allow_html=True)

# Header text
st.markdown("<h1 class='header-title'>Automation_Hub</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='header-subtitle'>Smart, practical tools for Geotechnical and Materials Engineers</h3>", unsafe_allow_html=True)
st.markdown("<p class='header-tagline'>Built for engineers. Powered by code.</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #90caf9'/>", unsafe_allow_html=True)

# --- Rest of your content remains unchanged ---
