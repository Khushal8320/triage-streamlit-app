import streamlit as st
import time
import uuid

#ktas = st.session_state.get("triage_data")
#name = st.session_state.get("prediction")

#st.write("KTAS Result:", ktas)
#st.write("Patient Name:", name)

# HIDE DEFAULT MULTIPAGE NAVIGATION
st.markdown("""
<style>
div[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- Page Setup ---
st.set_page_config(page_title="AI Triage Prediction", layout="centered")

# --- Custom Styling ---
st.markdown("""
<style>

body {
    background-color: #f8f9fa;
}

/* Header */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
    width: 90%;
    margin: 20px auto;
}

.header-left {
    font-weight: 600;
    font-size: 18px;
    color: #1e73e8;
    display: flex;
    align-items: center;
    gap: 8px;
}

.header-right {
    width: 40px;
    height: 40px;
    background-color: #fde7d9;
    border-radius: 50%;
}

/* Center layout */
.center {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;      
    justify-content: center;
    text-align: center;
    padding-top: 40px;
}

/* Circle image wrapper (keeps centered alignment always) */
.circle-img-wrapper {
    width: 100%;
    display: flex;
    justify-content: center; 
    margin-bottom: 20px;
}

.circle-img {
    width: 260px;
    height: 260px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 0 30px rgba(30,115,232,0.5);
    background-color: black;
}

.circle-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

h2 {
    margin-top: 15px;
    font-weight: 700;
    color: #1c1c1c;
}

p {
    color: gray;
    font-size: 14px;
    margin-top: -5px;
}

/* Progress labels */
.progress-label {
    font-size: 14px;
    font-weight: 500;
    color: #333;
    margin-top: 25px;
    margin-bottom: 5px;
    text-align: left;
    width: 300px;
}

/* Completion message */
.complete-box {
    margin-top: 40px;
    background-color: #e9f5e9;
    color: #1c7c1c;
    border: 1px solid #c6e1c6;
    padding: 15px 30px;
    border-radius: 10px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)


# --- Sidebar ---
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



# --- Header ---
st.markdown("""
<div class="header">
    <div class="header-left">🔷 AI Triage System</div>
    <div class="header-right"></div>
</div>
""", unsafe_allow_html=True)


# --- Main Section ---
st.markdown('<div class="center">', unsafe_allow_html=True)

# Centered Circle Image
st.markdown("""
<div class="circle-img-wrapper">
    <div class="circle-img">
        <img src="images/image1.png">
    </div>
</div>
""", unsafe_allow_html=True)

# Patient ID
patient_id = str(uuid.uuid4())[:12].upper()

st.markdown(f"""
<h2>Generating Triage Prediction...</h2>
<p>Processing for Patient ID: <strong>{patient_id}</strong></p>
""", unsafe_allow_html=True)


# --- Progress Bars ---
progress_labels = [
    "Processing Vitals & Symptoms...",
    "Cross-referencing Medical History...",
    "Finalizing Prediction..."
]

progress_bars = []
st.write("")

for label in progress_labels:
    st.markdown(f"<div class='progress-label'>{label}</div>", unsafe_allow_html=True)
    progress_bars.append(st.progress(0))

for i in range(101):
    progress_bars[0].progress(min(i, 100))
    if i > 40:
        progress_bars[1].progress(min(i - 40, 100))
    if i > 70:
        progress_bars[2].progress(min(i - 70, 100))
    time.sleep(0.05)


# --- Completion Message ---
st.markdown("""
<div class="complete-box">
    ✅ Triage Prediction Generated Successfully!
</div>
""", unsafe_allow_html=True)


# --- Button ---
st.markdown("<br>", unsafe_allow_html=True)

if st.button("View Prediction Report"):
    st.success("Redirecting to results page...")
    st.switch_page("pages/third.py")

st.markdown("</div>", unsafe_allow_html=True)
