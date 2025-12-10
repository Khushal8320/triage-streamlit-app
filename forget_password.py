# pages/7_Forgot_Password.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
st.set_page_config(page_title="Forgot Password - Harmony", layout="wide")

apply_css()
ensure_state()
render_sidebar()
render_header("Forgot Password", "Recover your account")

st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

email = st.text_input("Hospital Email", placeholder="Enter your hospital email")
if st.button("Send Recovery Link"):
    if not email:
        st.error("Please enter your email.")
    else:
        st.success(f"Recovery link sent to {email} (placeholder).")

render_footer()
