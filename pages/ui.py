# ui.py
import streamlit as st
from datetime import datetime

# Minimal CSS for cards / badges / chips — layout done via Streamlit
CSS = """
<style>



/* reduce default Streamlit padding */
.block-container { padding: 1rem 1rem 2rem 1rem !important; }

/* card look */
.h-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 6px 24px rgba(15,23,42,0.06);
  padding: 18px;
}

/* left brand panel (used on Home/login/register) */
.brand-panel {
  background: linear-gradient(180deg, #1e73e8 0%, #1660d6 100%);
  color: white;
  padding: 20px;
  border-radius: 10px;
}

/* small badges */
.badge {
  background: #f2f2f2;
  color: #374151;
  padding: 6px 10px;
  border-radius: 8px;
  font-size: 13px;
}

/* compact patient summary */
.summary {
  background: #f8f9fa;
  padding: 12px;
  border-radius: 8px;
}

/* chips */
.chip {
  display:inline-block;
  padding:6px 10px;
  border-radius:10px;
  font-weight:600;
  margin:4px 4px 4px 0;
}

/* color chips */
.chip-red { background:#ffd6d6; color:#c62828; }
.chip-yellow { background:#fff5cc; color:#b38f00; }
.chip-info { background:#e6f2ff; color:#155ec0; }

/* small footer */
.footer { font-size:12px; color:#9096a4; margin-top:12px; }
</style>
"""
def render_header(title: str, subtitle: str = ""):
    st.markdown(
        f"""
        <style>
        .custom-header {{
            margin-top: 20px !important;
        }}
        .custom-header h2 {{
            margin-bottom: 0px !important;
        }}
        </style>

        <div class="custom-header">
            <h2>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    if subtitle:
        st.caption(subtitle)
def apply_css():
    st.markdown(CSS, unsafe_allow_html=True)

def render_sidebar(active=None):
    """Render a consistent sidebar (uses Streamlit UI only). Updates st.session_state['page'] when a button clicked."""
    with st.sidebar:
        st.image("images/image1.png", width=80)
        st.markdown("**Dr. Jaydeep Ramani**  \nCardiologist")
        st.markdown("---")
        if st.button("🏠 Dashboard",width=200):
            st.switch_page('pages/six.py')
        if st.button("👥 Patient List",width=200):
            st.switch_page('pages/patient_list.py')
        if st.button("📋 Triage Queue", type="primary",width=200):
            st.switch_page('pages/triage.py')
        if st.button("📊 Analytics",width=200):
            st.switch_page('pages/Ai_prediction.py')
        if st.button("🕘 History",width=200):
            st.switch_page('pages/five.py')

        st.markdown("---")
        st.markdown("**Dr. Jaydeep Ramani**  \nCardiologist")
        if st.button("⚙️ Settings",width=200):
            st.switch_page('pages/setting.py')
        if st.button("🚪 Log Out",width=200):
            st.success("Logged out successfully...")
            st.switch_page('app.py')

def render_header(title: str, subtitle: str = ""):
    st.header(title)
    if subtitle:
        st.caption(subtitle)

def render_footer():
    st.markdown('<div class="footer">© 2025 Harmony. All rights reserved.</div>', unsafe_allow_html=True)

def ensure_state():
    if 'page' not in st.session_state:
        st.session_state['page'] = None
