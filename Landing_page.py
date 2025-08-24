import streamlit as st
from PIL import Image
import os
from aci_mix_landing_view import show_pro_landing

# --- PAGE CONFIG ---
st.set_page_config(page_title="Automation Hub", page_icon="🤖", layout="wide")

# --- LOGO SECTION ---
st.markdown(
    """
    <style>
        /* Responsive logo */
        .logo-container img {
            width: 280px;
            max-width: 60%;
            height: auto;
        }

        /* Responsive header */
        .header-text h1 {
            font-size: clamp(2em, 4vw, 3.2em);
            margin-bottom: 15px;
        }

        /* Responsive tagline */
        .header-text p {
            font-size: clamp(1em, 2vw, 1.6em);
            color: #555;
        }

        /* Divider */
        .divider {
            border: 1px solid #ddd;
            width: 60%;
            margin: 20px auto;
        }
    </style>

    <div class="logo-container" style="text-align: center; margin-top: 20px; margin-bottom: 30px;">
        <img src="your_logo.png">
    </div>

    <div class="header-text" style="text-align: center; margin-top: 10px;">
        <h1>Automation_Hub</h1>
        <p>Smart Tools for Smarter Engineers</p>
        <hr class="divider">
    </div>
    """,
    unsafe_allow_html=True
)

# --- BODY CONTENT ---
st.markdown("""
    <div style="text-align: center; margin-top: 40px; font-size: 1.2em; color: #444;">
        <p>
            Welcome to <b>Automation_Hub</b> — a suite of intelligent engineering tools 
            designed to simplify workflows, optimize designs, and enhance decision-making.
        </p>
        <p>
            Explore web applications built for concrete mix optimization, soil classification, 
            and AI-powered specification queries. Faster, smarter, and more reliable solutions 
            for civil engineers and project managers.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; margin-top: 60px; font-size: 0.9em; color: #777;">
        <p>© 2025 Automation_Hub | Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)


