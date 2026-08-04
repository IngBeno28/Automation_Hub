# branding.py - Centralized visual assets for Automation_Hub
# Design language: editorial / industrial (inspired by Bentley Systems' dark,
# high-contrast, blueprint-driven visual identity), adapted for a
# geotechnical & materials engineering toolkit.

# ============================================================================
# CORE PALETTE (referenced by Landing_page.py as well — keep in sync)
# ============================================================================
INK = "#0b0f14"          # near-black, headers/footers/CTA
INK_2 = "#151b23"         # charcoal panel
PAPER = "#faf9f6"         # warm off-white background
STEEL = "#2f5fa8"         # primary engineering-blue accent
GRAPHITE = "#4a5568"      # secondary slate accent
OXIDE = "#b5522a"         # rust/rebar accent, used sparingly
CONCRETE = "#6b6f76"      # muted body-copy gray
LINE = "rgba(11,15,20,0.10)"  # hairline border

# ============================================================================
# CARD DEFINITIONS
# ============================================================================

CARD_STYLES = {
    "aashto": {
        "accent_color": STEEL,
        "border_accent": STEEL,
        "icon": "📊",
        "badge": "AASHTO M 145",
        "eyebrow": "Soil Classification",
        "title": "AASHTO Soil Classification",
        "description": "Classify natural gravel materials using the AASHTO M 145 standard. Get Group Index, detailed logic, and professional PDF reports.",
        "link": "https://aashtoclassificationtool.streamlit.app"
    },
    "uscs": {
        "accent_color": GRAPHITE,
        "border_accent": GRAPHITE,
        "icon": "🧱",
        "badge": "ASTM D2487",
        "eyebrow": "Soil Classification",
        "title": "USCS Soil Classification",
        "description": "Automated soil classification based on ASTM D2487. Includes gradation curves, plasticity charts, and comprehensive PDF reports.",
        "link": "https://uscs-classification-tool.streamlit.app"
    },
    "concrete": {
        "accent_color": OXIDE,
        "border_accent": OXIDE,
        "icon": "🧪",
        "badge": "ACI 211.1",
        "eyebrow": "Mix Design",
        "title": "Concrete Mix Optimizer",
        "description": "Automate your ACI 211.1 mix proportion calculations. Input design strength, exposure class, and aggregate properties for optimized mix ratios.",
        "link": "https://Concreteoptimizationtool.streamlit.app"
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_card_style(card_key):
    """Inline CSS for the dark header panel of a specific card."""
    style = CARD_STYLES.get(card_key, CARD_STYLES["aashto"])
    accent = style["accent_color"]
    return (
        f"background: linear-gradient(135deg, {INK} 0%, {INK_2} 100%); "
        f"--card-accent: {accent};"
    )

def get_bg_pattern(card_key):
    """Get the icon emoji used as a faint watermark on the card panel."""
    return CARD_STYLES.get(card_key, CARD_STYLES["aashto"])["icon"]

def get_card_data(card_key):
    """Get all card data for a specific card."""
    return CARD_STYLES.get(card_key, CARD_STYLES["aashto"])

# ============================================================================
# SVG BLUEPRINT PATTERNS (Decorative — technical/drafting motif)
# ============================================================================

def get_card_svg(card_key):
    """Return a blueprint-style SVG decorative pattern for the card panel."""
    accent = CARD_STYLES.get(card_key, CARD_STYLES["aashto"])["accent_color"]
    patterns = {
        "aashto": f'''<svg viewBox="0 0 160 120" style="position:absolute; inset:0; width:100%; height:100%; opacity:0.16; pointer-events:none; z-index:0;">
            <line x1="0" y1="20" x2="160" y2="20" stroke="{accent}" stroke-width="0.5"/>
            <line x1="0" y1="50" x2="160" y2="50" stroke="{accent}" stroke-width="0.5"/>
            <line x1="0" y1="80" x2="160" y2="80" stroke="{accent}" stroke-width="0.5"/>
            <line x1="30" y1="0" x2="30" y2="120" stroke="{accent}" stroke-width="0.5"/>
            <line x1="90" y1="0" x2="90" y2="120" stroke="{accent}" stroke-width="0.5"/>
            <line x1="130" y1="0" x2="130" y2="120" stroke="{accent}" stroke-width="0.5"/>
            <circle cx="130" cy="30" r="18" fill="none" stroke="{accent}" stroke-width="1"/>
        </svg>''',
        "uscs": f'''<svg viewBox="0 0 160 120" style="position:absolute; inset:0; width:100%; height:100%; opacity:0.16; pointer-events:none; z-index:0;">
            <line x1="0" y1="30" x2="160" y2="30" stroke="{accent}" stroke-width="0.5"/>
            <line x1="0" y1="90" x2="160" y2="90" stroke="{accent}" stroke-width="0.5"/>
            <line x1="50" y1="0" x2="50" y2="120" stroke="{accent}" stroke-width="0.5"/>
            <line x1="110" y1="0" x2="110" y2="120" stroke="{accent}" stroke-width="0.5"/>
            <circle cx="40" cy="60" r="22" fill="none" stroke="{accent}" stroke-width="1"/>
            <circle cx="120" cy="60" r="14" fill="none" stroke="{accent}" stroke-width="1"/>
        </svg>''',
        "concrete": f'''<svg viewBox="0 0 160 120" style="position:absolute; inset:0; width:100%; height:100%; opacity:0.16; pointer-events:none; z-index:0;">
            <line x1="0" y1="15" x2="160" y2="15" stroke="{accent}" stroke-width="0.5"/>
            <line x1="0" y1="105" x2="160" y2="105" stroke="{accent}" stroke-width="0.5"/>
            <rect x="20" y="35" width="30" height="30" fill="none" stroke="{accent}" stroke-width="1"/>
            <rect x="70" y="35" width="30" height="30" fill="none" stroke="{accent}" stroke-width="1"/>
            <rect x="120" y="35" width="24" height="30" fill="none" stroke="{accent}" stroke-width="1"/>
        </svg>'''
    }
    return patterns.get(card_key, "")

# ============================================================================
# CARD CSS STYLES
# ============================================================================

CARD_CSS = f"""
/* ===== EDITORIAL PRODUCT CARDS ===== */
.product-card {{
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    box-shadow: none;
}}

.product-card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 24px 48px rgba(11,15,20,0.12);
}}

.product-card .card-panel {{
    position: relative;
    height: 130px;
    display: flex;
    align-items: flex-end;
    padding: 1rem 1.25rem;
    overflow: hidden;
}}

.product-card .card-panel::after {{
    content: '';
    position: absolute;
    left: 0; right: 0; bottom: 0;
    height: 3px;
    background: var(--card-accent, {STEEL});
}}

.product-card .card-pattern {{
    position: absolute;
    bottom: -10px;
    right: -6px;
    font-size: 3.4rem;
    opacity: 0.14;
    pointer-events: none;
    user-select: none;
    line-height: 1;
    z-index: 0;
    transition: all 0.5s ease;
}}

.product-card:hover .card-pattern {{
    transform: scale(1.08) rotate(-4deg);
    opacity: 0.2;
}}

.product-card .panel-eyebrow {{
    position: relative;
    z-index: 1;
    color: rgba(255,255,255,0.55);
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}}
"""
