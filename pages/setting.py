# pages/6_Settings.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
st.set_page_config(page_title="Settings - Harmony", layout="wide")
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

apply_css()
ensure_state()
render_sidebar()
render_header("Settings", "Application settings & preferences")
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.subheader("Profile")
name = st.text_input("Name", value="Dr. Evelyn Reed")
title = st.text_input("Title", value="Cardiologist")
email = st.text_input("Email", value="e.reed@hospital.org")
if st.button("Save Profile"):
    st.success("Profile saved (placeholder).")

st.subheader("Application")
refresh = st.slider("Auto-refresh interval (s)", 0, 300, 60)
if st.button("Save Settings"):
    st.success("Settings saved (placeholder).")

render_footer()
