import streamlit as st
from datetime import datetime

# ------------------------------------
# DYNAMIC VARIABLES (You Can Replace)
# ------------------------------------
patient_name = "Mukeshbhai"
patient_age = 48
patient_gender = "M"
patient_id = "894321"
dob = "05/15/1976"

alert_title = "⚠️ Immediate Physician Consultation Required"
alert_reason = "Based on abnormal ECG readings, low O₂ saturation, and patient history of hypertension. High probability of an acute cardiac event."

alert_time = datetime.now().strftime("%I:%M %p")

# Key Factors (dynamic)
factor1 = "⚠️ Abnormal ECG"
factor2 = "🩸 O₂ Saturation: 92%"
factor3 = "📈 History of Hypertension"
factor4 = "💬 Chief Complaint: Acute Chest Pain"

# Patient Summary Variables
chief_complaint = "Acute Chest Pain"
heart_rate = "110 bpm"
bp = "150/95 mmHg"
spo2 = "92%"
temperature = "37.1 °C"
allergy = "Penicillin"

# ------------------------------------
# PAGE CONFIG
# ------------------------------------
st.set_page_config(page_title="AI Triage", layout="wide")
# HIDE AUTO MULTIPAGE SIDEBAR LIST
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------
# SIDEBAR
# ------------------------------------
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



# ------------------------------------
# HEADER
# ------------------------------------
st.markdown(f"## {patient_name}, {patient_age}{patient_gender}")
st.caption(f"Patient ID: {patient_id} • DOB: {dob}")

# ------------------------------------
# ALERT BOX
# ------------------------------------
st.markdown(
    f"""
    <div style="
        background-color:#ffe6e6;
        border-left: 6px solid #ff4b4b;
        padding:16px;
        border-radius:8px;
        margin-top:10px;
    ">
    <h4 style="color:#d00000; margin-bottom:6px;">{alert_title}</h4>
    <p><b>AI Rationale:</b> {alert_reason}</p>
    <p style="font-size:12px; color:gray;">Generated at {alert_time}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------
# FACTOR CHIPS
# ------------------------------------
st.markdown("### Key Influencing Factors")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div style="background-color:#ffe6e6;padding:8px;border-radius:10px;text-align:center;">{factor1}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div style="background-color:#fff0e6;padding:8px;border-radius:10px;text-align:center;">{factor2}</div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div style="background-color:#fff9e6;padding:8px;border-radius:10px;text-align:center;">{factor3}</div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div style="background-color:#fff9e6;padding:8px;border-radius:10px;text-align:center;">{factor4}</div>', unsafe_allow_html=True)

# ------------------------------------
# MAIN LAYOUT
# ------------------------------------
left, right = st.columns([2, 1])

# LEFT SECTION
with left:
    st.markdown("### Next Actions")
    colA, colB, colC = st.columns(3)
    with colA:
        if st.button("🔵 Acknowledge & Escalate"):
            st.success("Escalation submitted.")

    with colB:
        st.button("🧪 Order Labs")

    with colC:
        if st.button("📄 View Full Report"):
            st.switch_page('pages/six.py')
        

    st.markdown("---")
    st.markdown("#### Was this suggestion helpful?")
    
    feedback_col1, feedback_col2 = st.columns(2)
    with feedback_col1:
        if st.button("👍 Yes"):
            st.success("Thank you for your feedback!")
    with feedback_col2:
        st.button("👎 No")

# RIGHT SECTION
with right:
    st.markdown("### Patient Summary")
    st.markdown(
        f"""
        <div style="background-color:#f8f9fa;border-radius:10px;padding:16px;">
        <p><b>Chief Complaint:</b> {chief_complaint}</p>
        <p><b>Heart Rate:</b> {heart_rate}</p>
        <p><b>Blood Pressure:</b> {bp}</p>
        <p><b>O₂ Saturation:</b> {spo2}</p>
        <p><b>Temperature:</b> {temperature}</p>
        <p><b>Known Allergies:</b> {allergy}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
