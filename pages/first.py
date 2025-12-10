import streamlit as st

# Page setup
st.set_page_config(page_title="Harmony - New Triage Assessment", layout="wide")

# Hide auto page selector
st.markdown("""
<style>
div[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------
# Custom CSS
# ------------------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #f8f9fa;
    padding: 2rem 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* clickable area fix */
.menu-btn button,
.bottom-btn button {
    width: 100%;
    background: none;
    border: none;
    text-align: left;
    font-size: 15px;
    padding: 10px;
    border-radius: 8px;
    cursor: pointer;
    color: #333;
}
.menu-btn button:hover,
.bottom-btn button:hover {
    background: #e9f0ff;
    color: #0056d6;
}

.active {
    background-color: #e9f0ff !important;
    color: #0056d6 !important;
    border-radius: 8px;
}

.sidebar-bottom { 
    border-top: 1px solid #ddd; 
    padding-top: 1rem; 
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------
# Sidebar (FIXED: uses real Streamlit buttons)
# ------------------------------------
with st.sidebar:

    st.markdown("""
        <div class="sidebar-user">
            <h3>Dr. Emily Carter</h3>
            <p>Cardiologist</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ")

    new_assessment = st.container()
    with new_assessment:
        clicked_new = st.button("➕ New Assessment", key="btn_new", type="primary")

    clicked_history = st.button("⏱ History", key="btn_history")

    st.markdown("---")
    clicked_settings = st.button("⚙️ Settings", key="btn_settings")
    clicked_logout = st.button("🚪 Logout", key="btn_logout")


# ------------------------------------
# HANDLE CLICKS (NOW WORKING)
# ------------------------------------
if clicked_new:
    st.switch_page("pages/first.py", )

if clicked_history:
    st.switch_page("pages/history.py")

if clicked_settings:
    st.switch_page("pages/setting.py")

if clicked_logout:
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.switch_page("app.py")


# ------------------------------------
# MAIN ASSESSMENT LOGIC
# ------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "progress" not in st.session_state:
    st.session_state.progress = 10

parameters = [
    "Systolic Blood Pressure (SBP)",
    "Respiratory Rate (RR)",
    "Heart Rate (HR)",
    "Body Temperature (BT)",
    "Pain Score (NRS)",
    "Mental Status",
    "Oxygen Saturation (SpO2)",
    "Blood Glucose Level",
    "KTAS RN",
    "Final Expert KTAS",
]

param = parameters[st.session_state.step]

st.markdown("## New Triage Assessment")
st.markdown(f"**{st.session_state.progress}% Complete**")

st.progress(st.session_state.progress / 100)


with st.form(key="triage_form"):
    st.markdown(f"### {param}")
    st.text_input("", key=f"input_{st.session_state.step}", placeholder="Enter value here")

    col1, col2 = st.columns(2)
    back = col1.form_submit_button("⬅ Back", disabled=(st.session_state.step == 0))
    next_btn = col2.form_submit_button("Next ➡")

if back:
    st.session_state.step -= 1
    st.session_state.progress = max(10, st.session_state.progress - 10)
    st.rerun()

if next_btn:
    if st.session_state.step < len(parameters) - 1:
        st.session_state.step += 1
        st.session_state.progress = min(100, st.session_state.progress + 10)
        st.rerun()
    if st.session_state.progress == 100:
        st.switch_page("pages/second.py")

st.markdown("<div class='footer'>© 2025 Harmony. All rights reserved. Privacy Policy</div>", unsafe_allow_html=True)
