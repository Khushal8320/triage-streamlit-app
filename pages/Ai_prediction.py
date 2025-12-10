# pages/5_AI_Prediction.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
import random
st.set_page_config(page_title="AI Prediction - Harmony", layout="wide")

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
render_header("AI Prediction", "View model results and confidence")

st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

patient_id = st.text_input("Patient ID to predict", value="894321")
if st.button("Run Prediction"):
    severity = random.choice(["KTAS Level 1", "KTAS Level 2", "KTAS Level 3"])
    conf = random.randint(80, 98)
    st.subheader(f"Prediction — {patient_id}")
    st.metric("Severity", severity)
    st.progress(conf)
    st.markdown(f"**Confidence:** {conf}%")
    st.markdown("**Key factors:** Abnormal ECG • Low SpO₂ • History of Hypertension")

render_footer()
