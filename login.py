import streamlit as st

st.set_page_config(page_title="Harmony Login", page_icon="💙", layout="wide")
st.markdown(
    """
    <style>
    /* Reset Streamlit spacing */
    .block-container { padding: 0rem 1rem 1rem 1rem !important; }
    main > div { padding-top: 0 !important; }

    /* Full-screen center container */
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-color: #f6f8fb;
    }

    /* Card */
    .login-card {
        width: 100%;
        max-width: 96%;
        height: 740px;
        display: flex;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08);
        overflow: hidden;
        background: #fff;
    }

    /* Left panel (branding) */
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

    /* Right panel (form) */
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

    /* Streamlit input overrides for consistent look */
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

    /* Password eye icon area keep default but consistent spacing */
    div[data-testid="stTextInput"] > div > div > svg { right: 12px; }

    /* Button */
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

    /* Row with remember + forgot */
    .extra-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: -6px;
    }
    .extra-row .remember { font-size: 14px; color: #374151; display:flex; align-items:center; gap:8px; }
    .extra-row .forgot { color: #1e73e8; font-size: 13px; text-decoration: none; }

    /* Footer */
    .footer { font-size: 12px; color: #9096a4; margin-top: 10px; }

    /* Responsive adjustments */
    @media (max-width: 880px) {
        .login-card { flex-direction: column; height: auto; }
        .left, .right { width: 100%; padding: 36px; }
        .container { padding: 24px 12px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML container start
st.markdown(
    """
    <div class="container">
      <div class="login-card">
        <div class="left">
          <h1>Harmony</h1>
          <h3>Emergency Triage AI System</h3>
          <p>AI-powered triage for faster, more accurate care.</p>
        </div>
        <div class="right">
    """,
    unsafe_allow_html=True,
)

# Form (right panel)
st.markdown("<h2>Staff Login</h2>", unsafe_allow_html=True)
user_id = st.text_input("Hospital ID or Email", placeholder="Enter your Hospital ID or Email")
password = st.text_input("Password", placeholder="Enter your password", type="password")

# Remember checkbox (styled row)
col1, col2 = st.columns([1, 1])
with col1:
    remember = st.checkbox("Remember me")
with col2:
    st.markdown('<div style="text-align:right; margin-top:6px;"><a class="forgot" href="#">Forgot Password?</a></div>', unsafe_allow_html=True)

# Login button
if st.button("🔐 Log In"):
    if not user_id.strip() or not password.strip():
        st.error("❌ Please enter both Hospital ID/Email and Password")
    else:
        st.success(f"✅ Login successful for: {user_id}")

# Footer and close containers
st.markdown('<div class="footer">© 2025 Harmony. All rights reserved. • <a href="#" style="color:#6b7280; text-decoration:none;">Privacy Policy</a></div>', unsafe_allow_html=True)
st.markdown("</div></div></div>", unsafe_allow_html=True)