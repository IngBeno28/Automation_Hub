import streamlit as st
from PIL import Image
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
    h1 {
        color: #0d47a1;
    }
    h3 {
        color: #1565c0;
    }
    p {
        color: #37474f;
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

# Logo + Header 
st.markdown("""
    <div style='text-align: center;'>
        <svg width="120" height="120" viewBox="0 0 100 100" style="margin-bottom: -20px;">
            <!-- Outer Gear (Blue) -->
            <circle cx="50" cy="50" r="40" fill="none" stroke="#0d47a1" stroke-width="6"/>
            <!-- Gear Teeth (Red) -->
            <path d="M50,10 L50,30 M70,50 L90,50 M50,70 L50,90 M30,50 L10,50" 
                  stroke="#e53935" stroke-width="4" stroke-linecap="round"/>
            <!-- Bridge (Green) -->
            <path d="M20,60 L35,45 L50,60 L65,45 L80,60" 
                  stroke="#43a047" stroke-width="3" fill="none"/>
            <path d="M35,45 L35,30 L65,30 L65,45" 
                  stroke="#43a047" stroke-width="3" fill="none"/>
            <!-- Support Pillars (Blue) -->
            <line x1="35" y1="60" x2="35" y2="75" stroke="#0d47a1" stroke-width="2"/>
            <line x1="65" y1="60" x2="65" y2="75" stroke="#0d47a1" stroke-width="2"/>
        </svg>
        <h1 style='color: #0d47a1; margin-top: 0;'>Automation_Hub</h1>
        <h3 style='color: #1565c0;'>Smart, practical tools for Geotechnical and Materials Engineers</h3>
        <p style='font-style: italic;'>Built for engineers. Powered by code.</p>
    </div>
    <hr style='border:1px solid #90caf9'/>
""", unsafe_allow_html=True)

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
st.markdown("🔗 LinkedIn: [Bernard Wiafe-Akenteng, P.E.](https://www.linkedin.com/in/bernard-wiafe-akenteng-p-e-93005124b/)")

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
