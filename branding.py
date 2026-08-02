# branding.py - Centralized visual assets for Automation_Hub

# ============================================================================
# CARD BACKGROUND DEFINITIONS
# ============================================================================

CARD_STYLES = {
    "aashto": {
        "gradient": "linear-gradient(145deg, #f8faff 0%, #e3edfb 100%)",
        "accent_color": "#0d47a1",
        "pattern": "📊",
        "border_accent": "#0d47a1",
        "icon": "📊",
        "badge": "AASHTO M 145",
        "title": "AASHTO Soil Classification",
        "description": "Classify natural gravel materials using the AASHTO M 145 standard. Get Group Index, detailed logic, and professional PDF reports.",
        "link": "https://aashtoclassificationtool.streamlit.app"
    },
    "uscs": {
        "gradient": "linear-gradient(145deg, #f8faff 0%, #e8f0fe 100%)",
        "accent_color": "#1565c0",
        "pattern": "🧱",
        "border_accent": "#1565c0",
        "icon": "🧱",
        "badge": "ASTM D2487",
        "title": "USCS Soil Classification",
        "description": "Automated soil classification based on ASTM D2487. Includes gradation curves, plasticity charts, and comprehensive PDF reports.",
        "link": "https://uscs-classification-tool.streamlit.app"
    },
    "concrete": {
        "gradient": "linear-gradient(145deg, #f8faff 0%, #eaf3fb 100%)",
        "accent_color": "#1e88e5",
        "pattern": "🧪",
        "border_accent": "#1e88e5",
        "icon": "🧪",
        "badge": "ACI 211.1",
        "title": "Concrete Mix Optimizer",
        "description": "Automate your ACI 211.1 mix proportion calculations. Input design strength, exposure class, and aggregate properties for optimized mix ratios.",
        "link": "https://Concreteoptimizationtool.streamlit.app"
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_card_style(card_key):
    """Generate inline CSS style string for a specific card."""
    style = CARD_STYLES.get(card_key, CARD_STYLES["aashto"])
    return f"background: {style['gradient']}; border-left: 4px solid {style['border_accent']};"

def get_bg_pattern(card_key):
    """Get the background pattern emoji for a card."""
    return CARD_STYLES.get(card_key, CARD_STYLES["aashto"])["pattern"]

def get_card_data(card_key):
    """Get all card data for a specific card."""
    return CARD_STYLES.get(card_key, CARD_STYLES["aashto"])

# ============================================================================
# SVG BACKGROUND PATTERNS (Decorative)
# ============================================================================

def get_card_svg(card_key):
    """Return an SVG decorative pattern for the card background."""
    patterns = {
        "aashto": '''<svg viewBox="0 0 120 120" style="position:absolute; bottom:0; right:0; width:100px; height:100px; opacity:0.06; pointer-events:none; z-index:0;">
            <rect x="10" y="10" width="100" height="100" rx="12" fill="none" stroke="#0d47a1" stroke-width="2"/>
            <line x1="20" y1="35" x2="100" y2="35" stroke="#0d47a1" stroke-width="2"/>
            <line x1="20" y1="55" x2="100" y2="55" stroke="#0d47a1" stroke-width="2"/>
            <line x1="20" y1="75" x2="80" y2="75" stroke="#0d47a1" stroke-width="2"/>
            <rect x="30" y="60" width="25" height="25" rx="4" fill="none" stroke="#0d47a1" stroke-width="1.5"/>
            <rect x="65" y="60" width="25" height="25" rx="4" fill="none" stroke="#0d47a1" stroke-width="1.5"/>
            <path d="M42,72 L52,72 L52,82 L42,82 Z" fill="#0d47a1" opacity="0.2"/>
            <path d="M77,72 L87,72 L87,82 L77,82 Z" fill="#0d47a1" opacity="0.2"/>
        </svg>''',
        "uscs": '''<svg viewBox="0 0 120 120" style="position:absolute; bottom:0; right:0; width:100px; height:100px; opacity:0.06; pointer-events:none; z-index:0;">
            <rect x="15" y="15" width="90" height="90" rx="10" fill="none" stroke="#1565c0" stroke-width="2"/>
            <circle cx="60" cy="45" r="18" fill="none" stroke="#1565c0" stroke-width="2"/>
            <circle cx="42" cy="80" r="12" fill="none" stroke="#1565c0" stroke-width="1.5"/>
            <circle cx="78" cy="80" r="12" fill="none" stroke="#1565c0" stroke-width="1.5"/>
            <line x1="48" y1="58" x2="48" y2="73" stroke="#1565c0" stroke-width="1.5"/>
            <line x1="72" y1="58" x2="72" y2="73" stroke="#1565c0" stroke-width="1.5"/>
            <path d="M48,48 L60,38 L72,48" fill="none" stroke="#1565c0" stroke-width="1.5"/>
        </svg>''',
        "concrete": '''<svg viewBox="0 0 120 120" style="position:absolute; bottom:0; right:0; width:100px; height:100px; opacity:0.06; pointer-events:none; z-index:0;">
            <rect x="10" y="10" width="100" height="100" rx="8" fill="none" stroke="#1e88e5" stroke-width="2"/>
            <rect x="22" y="22" width="28" height="28" rx="4" fill="none" stroke="#1e88e5" stroke-width="1.5"/>
            <rect x="70" y="22" width="28" height="28" rx="4" fill="none" stroke="#1e88e5" stroke-width="1.5"/>
            <rect x="22" y="70" width="28" height="28" rx="4" fill="none" stroke="#1e88e5" stroke-width="1.5"/>
            <rect x="70" y="70" width="28" height="28" rx="4" fill="none" stroke="#1e88e5" stroke-width="1.5"/>
            <circle cx="60" cy="60" r="10" fill="#1e88e5" opacity="0.12"/>
            <circle cx="60" cy="60" r="4" fill="none" stroke="#1e88e5" stroke-width="1.5"/>
        </svg>'''
    }
    return patterns.get(card_key, "")
