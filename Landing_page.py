import streamlit as st
from PIL import Image

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

# Main banner
st.markdown("""
    <h1 style='text-align: center;'>🛠️ Automation_Hub</h1>
    <h3 style='text-align: center;'>Smart, practical tools for Geotechnical and Materials Engineers</h3>
    <p style='text-align: center; font-style: italic;'>Built for engineers. Powered by code.</p>
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
st.markdown("""
Pro versions include:
- Downloadable PDF reports
- Offline/mobile versions
- Extra customization for teams or labs

**Interested?**
📩 Email: [wiafe1713@gmail.com](mailto:wiafe1713@gmail.com)  
🔗 LinkedIn: [Bernard Wiafe-Akenteng, P.E.](https://www.linkedin.com/in/bernard-wiafe-akenteng-p-e-93005124b/)

Let’s build tools that make real impact in the field.
""")

# Footer
st.markdown("""
---
<p style='text-align: center; font-size: 0.9em; color: #78909c;'>
    © 2025 Automation_Hub | Built by Bernard Wiafe-Akenteng  
    | <a href='https://github.com/IngBeno28'>GitHub</a>
    | MIT Licensed<br>
    <em>Built for engineers. Powered by code.</em>
</p>
""", unsafe_allow_html=True)

