import streamlit as st
from PIL import Image
from fpdf import FPDF
from datetime import datetime
import base64
import paystackapi
from paystackapi.transaction import Transaction
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paystack configuration
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
paystackapi.SECRET_KEY = PAYSTACK_SECRET_KEY
PRO_PRICE = 5000  # 5000 Naira (~$5 equivalent)

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
    .pro-feature {
        border-left: 4px solid #43a047;
        padding-left: 1rem;
        margin: 1rem 0;
    }
    .pro-badge {
        background-color: #43a047;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8em;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# PDF Generation Class
class ProfessionalPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
        self.set_font('DejaVu', '', 10)
        
    def header(self):
        self.image('logo.png', 10, 8, 33)
        self.set_font('DejaVu', 'B', 16)
        self.cell(0, 10, 'Professional Concrete Mix Design Report', 0, 1, 'C')
        self.set_font('DejaVu', '', 10)
        self.cell(0, 10, f'Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'C')
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Payment Functions
def handle_payment(email, amount, callback_url=None):
    try:
        response = Transaction.initialize(
            email=email,
            amount=amount * 100,
            callback_url=callback_url
        )
        return response
    except Exception as e:
        st.error(f"Payment initialization failed: {str(e)}")
        return None

def verify_payment(reference):
    try:
        response = Transaction.verify(reference)
        return response
    except Exception as e:
        st.error(f"Payment verification failed: {str(e)}")
        return None

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

# Demo PDF Generation (for illustration)
def generate_sample_pdf():
    pdf = ProfessionalPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 18)
    pdf.cell(0, 10, 'Sample Professional Report', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('DejaVu', '', 12)
    pdf.multi_cell(0, 10, "This is a sample of the professional PDF report you'll receive with Pro access. The full version includes detailed mix designs, calculations, and professional formatting.")
    return pdf.output(dest='S').encode('latin1')

# Pro CTA Section - Enhanced with Payment
st.subheader("🔐 Pro Access - Unlock Premium Features")
st.markdown("""
<div class="pro-feature">
    <h4>Professional PDF Reports <span class="pro-badge">PRO</span></h4>
    <p>Download beautifully formatted, ready-to-print reports with all calculations and specifications.</p>
</div>

<div class="pro-feature">
    <h4>Advanced Calculations <span class="pro-badge">PRO</span></h4>
    <p>Get additional calculation methods and optimization suggestions not available in the free version.</p>
</div>

<div class="pro-feature">
    <h4>Team Licenses <span class="pro-badge">PRO</span></h4>
    <p>Special pricing for labs, universities, and engineering teams.</p>
</div>
""", unsafe_allow_html=True)

# Payment Flow
if 'payment_verified' not in st.session_state:
    st.session_state.payment_verified = False

with st.expander("💰 Get Pro Access Now", expanded=False):
    if not st.session_state.payment_verified:
        with st.form("payment_form"):
            email = st.text_input("📧 Your Email Address", help="We'll send your receipt and download link here")
            if st.form_submit_button(f"🔓 Unlock Pro Features (₦{PRO_PRICE:,})"):
                if not email:
                    st.error("Please enter your email address")
                else:
                    response = handle_payment(
                        email=email,
                        amount=PRO_PRICE,
                        callback_url="https://your-streamlit-app-url.com"  # Update with your URL
                    )
                    
                    if response and response.get('status'):
                        st.session_state.payment_reference = response['data']['reference']
                        st.session_state.payment_email = email
                        st.success(f"Payment initialized! Please complete payment at: {response['data']['authorization_url']}")
                        st.markdown(f"[👉 Click here to complete payment]({response['data']['authorization_url']})")
                        
                        with st.spinner("Waiting for payment confirmation..."):
                            for i in range(30):
                                time.sleep(1)
                                verification = verify_payment(st.session_state.payment_reference)
                                if verification and verification['data']['status'] == 'success':
                                    st.session_state.payment_verified = True
                                    st.rerun()
                                    break
                            if not st.session_state.payment_verified:
                                st.error("Payment not completed in time. Please try again.")
    
    if st.session_state.payment_verified:
        st.success("✅ Payment verified! Thank you for your purchase.")
        sample_pdf = generate_sample_pdf()
        
        st.download_button(
            "⬇️ Download Sample Professional Report",
            data=sample_pdf,
            file_name="AutomationHub_Sample_Report.pdf",
            mime="application/pdf"
        )
        
        st.markdown("""
        **Next Steps:**
        1. You'll receive an email with your Pro access credentials
        2. Your account will be upgraded within 24 hours
        3. All tools will now show Pro features
        """)

# Tools Sections (unchanged)
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
