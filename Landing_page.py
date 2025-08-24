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
    .header-title {
        color: #0d47a1;
        margin-top: 10px;
        margin-bottom: 5px;
        text-align: center;
    }
    .header-subtitle {
        color: #1565c0;
        margin-top: 5px;
        text-align: center;
    }
    .header-tagline {
        color: #37474f;
        font-style: italic;
        text-align: center;
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
                logo = Image.open(path)
                return logo
            except Exception as e:
                st.warning(f"Could not load logo from {path}: {str(e)}")
    
    # Return None if no logo found
    return None

# Logo + Header - Centered section with slight right shift
logo = load_logo()

col1, col2, col3 = st.columns([1, 4, 2])

with col2:
    # Display centered logo (larger size - 220px)
    if logo:
        st.image(logo, width=220, use_container_width=False)
    else:
        # Fallback to SVG if no image logo found
        st.markdown("""
            <div style="text-align: center;">
                <svg width="220" height="220" viewBox="0 0 100 100">
                    <!-- Outer Gear (Blue) -->
                    <circle cx="50" cy="50" r="45" fill="none" stroke="#0d47a1" stroke-width="6"/>
                    
                    <!-- Gear Teeth (Red) -->
                    <path d="M50,10 L50,30 M70,50 L90,50 M50,70 L50,90 M30,50 L10,50" 
                          stroke="#e53935" stroke-width="4" stroke-linecap="round"/>
                    
                    <!-- Inner Gear (Lighter Blue) -->
                    <circle cx="50" cy="50" r="30" fill="none" stroke="#42a5f5" stroke-width="4"/>
                    
                    <!-- Bridge Structure (Green) -->
                    <path d="M25,60 L40,45 L60,45 L75,60" 
                          stroke="#43a047" stroke-width="3" fill="none"/>
                    <path d="M40,45 L40,30 L60,30 L60,45" 
                          stroke="#43a047" stroke-width="3" fill="none"/>
                    
                    <!-- Support Pillars (Blue) -->
                    <line x1="40" y1="60" x2="40" y2="75" stroke="#0d47a1" stroke-width="2"/>
                    <line x1="60" y1="60" x2="60" y2="75" stroke="#0d47a1" stroke-width="2"/>
                    
                    <!-- Hub Center (Gold) -->
                    <circle cx="50" cy="50" r="8" fill="#ffd700" stroke="#ff9800" stroke-width="2"/>
                    
                    <!-- Automation Symbol (Inside Hub) -->
                    <path d="M45,50 L55,50 M50,45 L50,55" stroke="#0d47a1" stroke-width="2"/>
                </svg>
            </div>
        """, unsafe_allow_html=True)

    # Header text
    st.markdown("<h1 class='header-title'>Automation_Hub</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='header-subtitle'>Smart, practical tools for Geotechnical and Materials Engineers</h3>", unsafe_allow_html=True)
    st.markdown("<p class='header-tagline'>Built for engineers. Powered by code.</p>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #90caf9'/>", unsafe_allow_html=True)

# Rest of the content (not centered)
# AASHTO Tool Section
st.subheader("📊 AASHTO Soil Classification Tool")
st.markdown("""
The AASHTO Classification Tool helps engineers quickly classify natural gravel materials 
using the AASHTO M 145 standard. Enter sieve results, LL, and PI — and get your classification, 
including group index and detailed logic used for classification.
""")

col1, col2 = st.columns([1,1])
with col1:
    st.link_button("Try Free Version", "https://aashtoclassificationtool.streamlit.app")
with col2:
    st.link_button("View Source Code", "https://github.com/IngBeno28/AASHTO_Classification_tool")

st.markdown("---")

# Concrete Optimizer Section
st.subheader("🧪 Concrete Mix Design Optimizer")
st.markdown("""
The Concrete Mix Design Optimizer automates your ACI 211.1 mix proportion calculations. 
Enter design strength, exposure class, workability, and aggregate properties — the tool computes 
the required mix ratios with intelligent suggestions based on ACI tables.
""")

col3, col4 = st.columns([1,1])
with col3:
    st.link_button("Try Free Version", "https://Concreteoptimizationtool.streamlit.app")
with col4:
    st.link_button("View Source Code", "https://github.com/IngBeno28/concrete-optimizer1")

st.markdown("---")

# Pro CTA
st.subheader("🔐 Want Pro Access?")
with st.expander('🔐 Explore Pro Version Features For Concrete Optimizer', expanded=False):
    show_pro_landing()

st.markdown("**Interested?**")
st.markdown("📩 Email: [wiafe1713@gmail.com](mailto:wiafe1713@gmail.com)")  
st.markdown("🔗 LinkedIn: [Bernard Wiafe Akenteng (P.E - GhIE)](www.linkedin.com/in/bernard-wiafe-akenteng-p-e-ghie-93005124b)")

# Footer
st.markdown("""
---
<p style='text-align: center; font-size: 0.9em; color: #78909c;'>
    © 2025 Automation_Hub | Built by Automation_Hub  
    | <a href='https://github.com/IngBeno28'>GitHub</a>
    | MIT Licensed<br>
    <em>Built for engineers. Powered by code.</em>
</p>
""", unsafe_allow_html=True)
