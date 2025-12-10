import streamlit as st
import random
import datetime
#from ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
# -------------------------------------
# PAGE SETUP
# -------------------------------------
st.set_page_config(page_title="AI Triage Prediction", layout="centered")


# HIDE AUTO MULTIPAGE SIDEBAR LIST
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------
# CUSTOM STYLES
# -------------------------------------
st.markdown("""
<style>
body {
    background-color: black;
}
.main-card {
    background-color: white;
    padding: 30px 40px;
    border-radius: 16px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    width: 80%;
    margin: 40px auto;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    color: #1e1e1e;
    font-size: 18px;
    margin-bottom: 20px;
}
.badge {
    font-size: 13px;
    color: gray;
    background-color: #f2f2f2;
    padding: 6px 12px;
    border-radius: 10px;
}
.severity-box {
    background-color: #ffe5e5;
    border-radius: 12px;
    text-align: center;
    padding: 30px 10px;
    margin-bottom: 20px;
}
.severity-title {
    color: #e63946;
    font-weight: 700;
    font-size: 36px;
    margin-bottom: 5px;
}
.severity-sub {
    color: #b30000;
    font-size: 18px;
    margin-top: -5px;
    font-weight: 500;
}
.section-title {
    font-size: 16px;
    font-weight: 600;
    color: #1e1e1e;
    margin-top: 30px;
    margin-bottom: 10px;
}
.factor-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px 40px;
    font-size: 15px;
}
.factor-label {
    color: gray;
    font-weight: 500;
}
.factor-value {
    font-weight: 600;
    color: #000;
}
.symptom-chip {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    margin: 5px;
    font-weight: 600;
}
.chip-red { background-color: #ffd6d6; color: #c62828; }
.chip-yellow { background-color: #fff5cc; color: #b38f00; }
.buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 30px;
}
.stButton>button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 10px 30px !important;
}
            
</style>
""", unsafe_allow_html=True)
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


# -------------------------------------
# HEADER SECTION
# -------------------------------------
st.markdown(f"""
<div class="header">
    <div>🤖 AI Triage Prediction</div>
    <div>
        <span class="badge">Patient ID: 11032-B</span>
        <span class="badge">Updated: {datetime.datetime.now().strftime("%I:%M %p")}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------
# MAIN CARD BODY
# -------------------------------------
#st.markdown("<div class='main-card'>", unsafe_allow_html=True)

# Severity Block
st.markdown("""
<div class="severity-box">
    <div style="font-size:14px; color:#b30000; letter-spacing:1px;">AI PREDICTED SEVERITY</div>
    <div class="severity-title">KTAS Level 1</div>
    <div class="severity-sub">Critical</div>
</div>
""", unsafe_allow_html=True)

# Confidence Score
confidence = random.uniform(88, 99)
st.markdown("**Prediction Confidence**")
st.progress(int(confidence))
st.markdown(
    f"<div  style='text-align:right; font-weight:600; color:#1e73e8;'>{int(confidence)}%</div>",
    unsafe_allow_html=True
)

# Predictive Factors Section
st.markdown("<div class='section-title'>Key Predictive Factors</div>", unsafe_allow_html=True)

st.markdown("""
<div class='factor-grid'>
    <div><span class='factor-label'>Heart Rate</span><br><span class='factor-value'>120 bpm</span></div>
    <div><span class='factor-label'>Blood Pressure</span><br><span class='factor-value'>140/90 mmHg</span></div>
    <div><span class='factor-label'>SpO₂</span><br><span class='factor-value'>92%</span></div>
    <div><span class='factor-label'>Temperature</span><br><span class='factor-value'>38.5°C</span></div>
    <div><span class='factor-label'>Respiratory Rate</span><br><span class='factor-value'>22 breaths/min</span></div>
</div>
""", unsafe_allow_html=True)

# Symptoms Block
st.markdown("<div class='section-title'>Chief Complaint / Symptoms</div>", unsafe_allow_html=True)

st.markdown("""
<div>
    <span class='symptom-chip chip-red'>Chest Pain</span>
    <span class='symptom-chip chip-red'>Shortness of Breath</span>
    <span class='symptom-chip chip-yellow'>Dizziness</span>
</div>
""", unsafe_allow_html=True)

# Buttons Section
col1, col2 = st.columns(2)
with col1:
    st.button("🩺 Request Manual Review")

with col2:
    if st.button("✅ Acknowledge & Proceed"):
        st.success("✅ Case acknowledged and recorded successfully.")
        st.switch_page("pages/five.py") 

st.markdown("</div>", unsafe_allow_html=True)
