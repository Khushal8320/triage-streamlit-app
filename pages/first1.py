import streamlit as st
import pickle
import numpy as np
import pandas as pd
# Page setup
st.set_page_config(page_title="Harmony - New Triage Assessment", layout="wide")


# load the model
def load_model():
    with open("ktas_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()



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
    add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online","Batch"))
    clicked_settings = st.button("⚙️ Settings", key="btn_settings")
    clicked_logout = st.button("🚪 Logout", key="btn_logout")


# ------------------------------------
# HANDLE CLICKS (NOW WORKING)
# ------------------------------------
if clicked_new:
    st.switch_page("pages/first.py", )

if clicked_history:
    st.switch_page("pages/five.py")

if clicked_settings:
    st.switch_page("pages/setting.py")

if clicked_logout:
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.switch_page("app.py")


# Handle navigation
if clicked_new:
    st.switch_page("pages/first.py")

if clicked_history:
    st.switch_page("pages/history.py")

if clicked_settings:
    st.switch_page("pages/setting.py")

if clicked_logout:
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.switch_page("app.py")

# Page Title
st.title("🏥 Emergency Triage Input Form")
st.write("Enter patient details for triage evaluation.")

# -------------------------------
# SECTION 1: VITAL SIGNS
# -------------------------------
if add_selectbox=='Online':
    with st.container():
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("🩺 Vital Signs")

        col1, col2 = st.columns(2)

    with col1:
        sbp = st.number_input("Systolic Blood Pressure (SBP mmHg)", min_value=50, max_value=250, step=1)
        hr = st.number_input("Heart Rate (HR bpm)", min_value=30, max_value=220, step=1)
        bt = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=43.0, step=0.5)

    with col2:
        rr = st.number_input("Respiratory Rate (breaths/min)", min_value=5, max_value=60, step=1)
        dbp = st.number_input("Diastolic Blood Pressure", min_value=30, max_value=150, step=1)
        ktas_rn = st.selectbox("KTAS RN", [1, 2, 3, 4, 5])

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# SECTION 2: CLINICAL ASSESSMENT
# -------------------------------
    with st.container():
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("🧠 Clinical Assessment")

        mental_status = st.selectbox(
        "Mental Status",
        [1,2,3,4]
    )
   
  


        pain = st.slider("Pain Score (NRS)", 0, 10, 0)

    
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# SUBMIT BUTTON
# -------------------------------
    colA, colB = st.columns([1, 1.2])


    with colB:
        if st.button("➡️ Submit & Analyze"):
           # st.switch_page("pages/second.py")


     # Define columns
            cols = ['mental_status', 'ktas_rn', 'sbp', 'rr', 'hr', 'pain', 'bt', 'dbp']
            input_data = np.array([[mental_status, ktas_rn, sbp, rr, hr, pain, bt, dbp]])
            prediction = model.predict(input_data)
         # Store values in session
            st.session_state["triage_data"] = input_data
            st.session_state["prediction"] = prediction

            st.success(f"Predicted KTAS Level: **{prediction}**")

# Create dataframe
            df = pd.DataFrame(
    [[sbp, hr, bt, rr, dbp, pain, ktas_rn,dbp]],
    columns=['sbp', 'hr', 'bt', 'rr', 'dbp', 'pain', 'ktas_rn','dbp']
)
# Save to session state
            st.session_state["triage_data"] = df
            st.session_state["prediction"] = prediction
# Convert to string
        #df[["sbp", "hr", "bt", "rr", "spo2", "glucose", "mental_status", "pain", "ktas_rn"]] = df[
    #["sbp", "hr", "bt", "rr", "spo2", "glucose", "mental_status", "pain", "ktas_rn"]
#].astype(str)

# Save to session state
if add_selectbox == 'Batch':

    st.subheader("📂 Batch Prediction Mode")

    file_upload = st.file_uploader("Upload a CSV file for prediction", type=['csv'])

    submit_batch = st.button("➡️ Submit & Analyze")

    if submit_batch:
        if file_upload is None:
            st.error("⚠ Please upload a CSV file first.")
        else:
            try:
                data = pd.read_csv(file_upload)

                st.write("### Uploaded Data Preview:")
                st.write(data.head())

                # Rename columns
                rename_map = {
                    'sbp': 'SBP',
                    'hr': 'HR',
                    'bt': 'BT',
                    'rr': 'RR',
                    'dbp': 'DBP',
                    'pain': 'NRS_pain',
                    'ktas_rn': 'KTAS_RN',
                    'mental_status': 'Mental'
                }
                data = data.rename(columns=rename_map)

                expected_cols = ['Mental','KTAS_RN','SBP','RR','HR','NRS_pain','BT','DBP']

                missing = [c for c in expected_cols if c not in data.columns]

                if missing:
                    st.error(f"❌ Missing required columns: {missing}")
                else:
                    # Reorder & predict
                    data_model = data[expected_cols]
                    predictions = model.predict(data_model)

                    # Attach predictions to dataframe
                    data["Prediction"] = predictions

                    # Save to session state for next page
                    st.session_state["batch_data"] = data

                    st.write("### 🔮 Batch Predictions:")
                    st.write(data)

                    # Redirect to results page
                    st.success("Batch prediction completed! Redirecting...")
                    #st.switch_page("pages/batch_results.py")

            except Exception as e:
                st.error(f"❌ Error processing file: {e}")

       

# Redirect to next page
        #st.switch_page("pages/second.py")
