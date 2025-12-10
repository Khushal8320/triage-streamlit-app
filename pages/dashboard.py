# pages/1_Dashboard.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
import random, pandas as pd
st.set_page_config(page_title="Dashboard - Harmony", layout="wide")

st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

apply_css()
ensure_state()
render_sidebar()
render_header("Dashboard", "Overview of triage activity and alerts")

# Top metrics using Streamlit metrics for perfect alignment
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Cases", random.randint(5, 24))
col2.metric("Critical Alerts", random.randint(0, 6))
col3.metric("Avg Triage Time (min)", random.randint(5, 18))
col4.metric("Completed Today", random.randint(10, 40))

st.markdown("---")

# Charts / insights — use st.dataframe and placeholders
st.subheader("Recent Cases")
df = pd.DataFrame([
    {"Patient":"John Doe","Priority":"Critical","ETA":"Immediate"},
    {"Patient":"Jane Roe","Priority":"High","ETA":"10 min"},
    {"Patient":"Ali Patel","Priority":"Medium","ETA":"25 min"},
])
print(df)
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.subheader("Operational Notes")
st.write("- Auto-refresh interval: 60s (configurable in Settings)")
st.write("- Model confidence threshold: 85%")

render_footer()
