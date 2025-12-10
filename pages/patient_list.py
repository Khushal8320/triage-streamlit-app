# pages/2_Patient_List.py
import streamlit as st
from pages.ui import apply_css, render_sidebar, render_header, render_footer, ensure_state
import pandas as pd
st.set_page_config(page_title="Patient List - Harmony", layout="wide")
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
render_header("Patient List", "Search, filter, and open patient records")
# HIDE AUTO MULTIPAGE SIDEBAR LIST
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# sample data (replace with DB / API)
data = [
    {"id":"894321","name":"John Doe","age":48,"sex":"M","status":"In ED"},
    {"id":"11032-B","name":"Jane Roe","age":36,"sex":"F","status":"Discharged"},
    {"id":"55219-A","name":"Ali Patel","age":67,"sex":"M","status":"In Ward"},
    {"id":"778233","name":"Maria Alvarez","age":58,"sex":"F","status":"In ED"},
]
df = pd.DataFrame(data)

# search & filters
col1, col2 = st.columns([3,1])
with col1:
    search = st.text_input("Search (name or ID)")
with col2:
    status_filter = st.selectbox("Status", ["All","In ED","In Ward","Discharged"])

filtered = df.copy()
if search:
    mask = df['name'].str.contains(search, case=False) | df['id'].str.contains(search, case=False)
    filtered = df[mask]
if status_filter != "All":
    filtered = filtered[filtered['status'] == status_filter]

st.dataframe(filtered, use_container_width=True)

# show selected patient summary
sel = st.selectbox("Open patient record", options=[""] + filtered['id'].tolist())
if sel:
    patient = filtered[filtered['id'] == sel].iloc[0].to_dict()
    st.markdown("### Patient Summary")
    left, right = st.columns([2,1])
    with left:
        st.write(f"**Name:** {patient['name']}")
        st.write(f"**ID:** {patient['id']}")
        st.write(f"**Age / Sex:** {patient['age']} / {patient['sex']}")
        st.write(f"**Status:** {patient['status']}")
    with right:
        st.markdown('<div class="summary">', unsafe_allow_html=True)
        st.write("Quick Vitals")
        st.write("- HR: 110 bpm")
        st.write("- BP: 150/95")
        st.write("- SpO₂: 92%")
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()
