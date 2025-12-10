# pages/3_Triage_Queue.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state

st.set_page_config(page_title="Triage Queue - Harmony", layout="wide")

apply_css()
ensure_state()
render_sidebar()
# HIDE AUTO MULTIPAGE SIDEBAR LIST
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# Top margin added for header
st.markdown("""
<style>
.top-margin {
    margin-top: 30px !important;
}
.queue-card {
    padding: 18px 20px;
    background: #ffffff;
    border-radius: 12px;
    margin-bottom: 18px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
}
.queue-header {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="top-margin"></div>', unsafe_allow_html=True)

render_header("Triage Queue", "Active triage queue and quick actions")

# sample queue items (replace with backend)
queue = [
    {"id":"894321","name":"John Doe","priority":"Critical","wait":"2 min"},
    {"id":"778233","name":"Maria Alvarez","priority":"High","wait":"8 min"},
    {"id":"665210","name":"K. Singh","priority":"Medium","wait":"20 min"},
]

# ---------- QUEUE LIST WITH MARGIN + ALIGNMENT ----------
for p in queue:
    st.markdown('<div class="queue-card">', unsafe_allow_html=True)

    cols = st.columns([4, 1.5, 1, 1.2])

    cols[0].markdown(
        f"<div class='queue-header'>{p['name']}</div>"
        f"ID: {p['id']}<br>Priority: <b>{p['priority']}</b>",
        unsafe_allow_html=True
    )
    cols[1].markdown(f"⏳ **{p['wait']}**")

    if cols[2].button("Open", key=f"open_{p['id']}"):
        st.session_state['selected_patient'] = p['id']
        st.success(f"Opened {p['name']}")

    if cols[3].button("Escalate", key=f"escalate_{p['id']}"):
        st.warning(f"Escalation created for {p['name']}")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SELECTED PATIENT ----------
if 'selected_patient' in st.session_state:
    st.markdown("---")
    st.markdown(f"### Selected Patient: **{st.session_state['selected_patient']}**")
    st.write("Open patient panel or run AI prediction here.")

render_footer()
