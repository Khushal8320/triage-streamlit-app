import streamlit as st

st.set_page_config(page_title="Harmony Register", page_icon="💙", layout="wide")

# ---------------------------------------
# SAME CSS AS LOGIN PAGE  (REUSED 100%)
# ---------------------------------------


st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .block-container { padding: 0rem 1rem 1rem 1rem !important; }
    main > div { padding-top: 0 !important; }

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-color: #f6f8fb;
    }

    .login-card {
        width: 960px;
        max-width: 96%;
        height: 600px;
        display: flex;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08);
        overflow: hidden;
        background: #fff;
    }

    .left {
        width: 50%;
        background: linear-gradient(180deg, #1e73e8 0%, #1660d6 100%);
        color: #fff;
        padding: 72px 56px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 6px;
    }
    .left h1 { margin: 0; font-size: 40px; font-weight: 700; letter-spacing: -0.6px; }
    .left h3 { margin: 0; font-size: 18px; font-weight: 600; opacity: 0.95; }
    .left p  { margin-top: 10px; font-size: 15px; color: rgba(255,255,255,0.9); line-height: 1.4; }

    .right {
        width: 50%;
        padding: 64px 56px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 18px;
        background: #ffffff;
    }
    .right h2 { margin: 0; font-size: 28px; color: #0f1724; font-weight: 800; }

    div[data-testid="stTextInput"] > div > div,
    div[data-testid="stTextInput"] input {
        border-radius: 10px !important;
        padding: 12px 14px !important;
        border: 1px solid #e3e7ee !important;
        box-shadow: none !important;
        font-size: 14px !important;
    }
    div[data-testid="stTextInput"] label {
        font-size: 13px;
        color: #344054;
        margin-bottom: 6px;
    }

    div[data-testid="stTextInput"] > div > div > svg { right: 12px; }

    .stButton > button {
        width: 100%;
        background-color: #1e73e8 !important;
        color: white !important;
        padding: 12px 14px !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        font-weight: 600;
        border: none !important;
    }
    .stButton > button:hover { background-color: #155ec0 !important; }

    .footer { font-size: 12px; color: #9096a4; margin-top: 10px; }

    @media (max-width: 880px) {
        .login-card { flex-direction: column; height: auto; }
        .left, .right { width: 100%; padding: 36px; }
        .container { padding: 24px 12px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# PAGE STRUCTURE (REUSED)
# -------------------------------
st.markdown(
    """
    <div class="container">
      <div class="login-card">
        <div class="left">
          <h1>Harmony</h1>
          <h3>Emergency Triage AI System</h3>
          <p>Create your Harmony staff account to access secure triage tools.</p>
        </div>
        <div class="right">
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# REGISTER FORM
# -------------------------------
st.markdown("<h2>Create Account</h2>", unsafe_allow_html=True)

full_name = st.text_input("Full Name", placeholder="Enter your full name")
email = st.text_input("Hospital Email", placeholder="Enter your hospital email")
hospital_id = st.text_input("Hospital ID", placeholder="Enter your official Hospital ID")
role = st.selectbox("Role", ["Select Role", "Physician", "Nurse", "Triage Staff", "Admin"])
password = st.text_input("Password", placeholder="Create a password", type="password")
confirm_password = st.text_input("Confirm Password", placeholder="Re-enter your password", type="password")

# Register button
if st.button("📝 Register Account"):
    if not full_name or not email or not hospital_id or role == "Select Role" or not password or not confirm_password:
        st.error("❌ Please fill all fields.")
    elif password != confirm_password:
        st.error("❌ Passwords do not match.")
    else:
        st.success(f"✅ Account created for {full_name} ({role})")

# ● Link to Login Page
st.markdown(
    """
    <div style="margin-top:8px; text-align:center; font-size:13px;">
        Already have an account?
        <a href="#" style="color:#1e73e8; text-decoration:none;">Log In</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown('<div class="footer">© 2025 Harmony. All rights reserved.</div>', unsafe_allow_html=True)

# Close HTML
st.markdown("</div></div></div>", unsafe_allow_html=True)
