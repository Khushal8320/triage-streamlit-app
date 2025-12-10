# Home.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state

st.set_page_config(page_title="Harmony Home", layout="wide")
apply_css()
ensure_state()
render_sidebar()

render_header("Harmony — Home", "Emergency Triage AI System")

# use Streamlit layout primitives for perfect alignment
with st.container():
    left_col, right_col = st.columns([1.3, 1])
    with left_col:
        st.markdown('<div class="h-card">', unsafe_allow_html=True)
        st.markdown('<div class="brand-panel">', unsafe_allow_html=True)
        st.subheader("Harmony")
        st.write("AI-powered triage for faster, more accurate care.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("### Quick Actions")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("Open Triage Queue")
        with c2:
            st.button("New Patient")
        with c3:
            st.button("Run AI Scan")
        st.markdown('</div>', unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="h-card">', unsafe_allow_html=True)
        st.subheader("Recent Alerts")
        st.write("- John Doe — Critical AI alert (ECG)")
        st.write("- Ali Patel — Elevated BP trend")
        st.write("- System: 3 new updates available")
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()
