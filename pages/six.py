import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
# from ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
# --- PAGE CONFIG ---
st.set_page_config(page_title="Emergency Triage Dashboard", layout="wide")
# HIDE AUTO MULTIPAGE SIDEBAR LIST
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---




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



# --- HEADER ---
st.markdown("## Emergency Triage Dashboard")
st.caption("Real-time overview of triage performance and patient flow.")

# --- TIME FILTERS ---
cols = st.columns([1,1,1,1,6])
cols[0].button("Last 24 Hours", type="primary",width=250)
cols[1].button("This Week",width=250)
cols[2].button("This Month",width=250)
cols[3].button("Custom Range 🗓️",width=250)
cols[4].markdown("<p style='text-align:right;color:gray;'>Last updated: 1 min ago</p>", unsafe_allow_html=True)

st.markdown("")

# --- TOP METRIC CARDS ---
card1, card2, card3 = st.columns(3)
with card1:
    st.markdown("""
    <div style="background-color:#f9fafb;padding:18px;border-radius:12px;">
        <h4>Patients in Queue</h4>
        <h2>42</h2>
        <p style="color:green;">▲ +5% vs last hour</p>
    </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
    <div style="background-color:#f9fafb;padding:18px;border-radius:12px;">
        <h4>Avg. Wait Time</h4>
        <h2>18 min</h2>
        <p style="color:red;">▼ -2% vs last hour</p>
    </div>
    """, unsafe_allow_html=True)

with card3:
    st.markdown("""
    <div style="background-color:#f9fafb;padding:18px;border-radius:12px;">
        <h4>Mistrage Rate</h4>
        <h2>3.2%</h2>
        <p style="color:orange;">▲ +1.1% vs yesterday</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# --- CHARTS SECTION ---
chart_col, donut_col = st.columns([2,1])

# Bar Chart
bar_data = pd.DataFrame({
    "Hour": [f"{i}:00" for i in range(8, 20)],
    "Patients": [12, 9, 14, 20, 17, 19, 23, 25, 22, 26, 27, 29]
})
bar_fig = px.bar(bar_data, x="Hour", y="Patients", 
                 title="Patient Triage Stats (Last 24 Hours)",
                 color_discrete_sequence=["#3b82f6"])
bar_fig.update_layout(title_x=0.02, plot_bgcolor="#ffffff", paper_bgcolor="#ffffff", margin=dict(l=20, r=20, t=60, b=20))
chart_col.plotly_chart(bar_fig, use_container_width=True)

# Donut Chart
donut_data = pd.DataFrame({
    "Level": ["Level 1 (Critical)", "Level 2 (Emergent)", "Level 3 (Urgent)", "Level 4/5 (Less Urgent)"],
    "Count": [4, 11, 17, 10]
})
donut_fig = px.pie(donut_data, values="Count", names="Level", hole=0.6,
                   color_discrete_sequence=["#ef4444","#f59e0b","#3b82f6","#22c55e"])
donut_fig.update_layout(title="Triage Level Distribution", showlegend=True, margin=dict(l=20, r=20, t=60, b=20))
donut_col.plotly_chart(donut_fig, use_container_width=True)

# --- RECENT PATIENT ACTIVITY ---
st.markdown("### Recent Patient Activity")
st.caption("Showing AI prediction vs. final triage for recent entries.")

data = {
    "Patient ID": ["#P789123", "#P789122", "#P789121", "#P789120", "#P789119"],
    "Timestamp": ["2024-05-21 14:32", "2024-05-21 14:28", "2024-05-21 14:25", "2024-05-21 14:19", "2024-05-21 14:15"],
    "AI Predicted Level": ["Level 2 (Emergent)", "Level 4 (Less Urgent)", "Level 1 (Critical)", "Level 3 (Urgent)", "Level 5 (Non-urgent)"],
    "Final Triage Level": ["Level 2 (Emergent)", "Level 3 (Urgent)", "Level 1 (Critical)", "Level 3 (Urgent)", "Level 5 (Non-urgent)"],
    "Status": ["Match", "Mismatch", "Match", "Match", "Match"]
}

df = pd.DataFrame(data)

def highlight_status(val):
    color = "green" if val == "Match" else "orange"
    return f'background-color:{color};color:white;text-align:center;border-radius:6px;'

st.dataframe(
    df.style.applymap(highlight_status, subset=["Status"]),
    use_container_width=True,
    hide_index=True
)
