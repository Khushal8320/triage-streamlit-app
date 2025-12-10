# pages/4_Case_Report.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
import io
st.set_page_config(page_title="Case Report - Harmony", layout="wide")

apply_css()
ensure_state()
render_sidebar()
render_header("Full Case Report", "Detailed patient report and timeline")

st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

patient_id = st.text_input("Enter Patient ID", value="894321")
if st.button("Load Report"):
    # sample structured content built via Streamlit (no raw HTML)
    st.subheader("John Doe • 894321")
    st.markdown("**Chief Complaint:** Acute Chest Pain")
    st.markdown("**Vitals:** HR 110 bpm • BP 150/95 • SpO₂ 92%")
    st.markdown("---")
    st.subheader("Timeline")
    st.write("- 14:20: Arrival at triage")
    st.write("- 14:25: AI alert generated (ECG/O₂ abnormal)")
    st.write("- 14:28: Nurse assessment completed")
    st.write("- 14:35: Physician notified")

    # download as text (replace with real PDF generation later)
    report_text = f"Report for {patient_id}\nChief Complaint: Acute Chest Pain\n..."
    buf = io.BytesIO(report_text.encode('utf-8'))
    st.download_button("📄 Download Report (TXT)", data=buf, file_name=f"report_{patient_id}.txt", mime="text/plain")

render_footer()
