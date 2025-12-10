"""
Harmony Emergency Triage AI System - Staff Login
Author: Sakir
Description: Compact, centered login with original colors and branding
"""

import streamlit as st

# ===========================
# PAGE CONFIGURATION
# ===========================
st.set_page_config(
    page_title="Harmony Login", 
    page_icon="💙", 
    layout="centered"
)

# ===========================
# CUSTOM CSS STYLING
# ===========================
def load_custom_css():
    """Load custom CSS with original colors"""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        * { font-family: 'Inter', sans-serif; }
        
        #MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }
        
        /* Original background color */
        .stApp {
            #background-color: #f6f8fb;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .block-container {
            padding: 40px 20px !important;
            max-width: 550px !important;
        }
        
        /* Card styling */
        .main-card {
            background: white;
            border-radius: 16px;
            padding: 45px 50px;
            box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08);
            margin: 0 auto;
        }
        
        /* Logo with original blue gradient */
        .logo-box {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .logo-icon {
            width: 64px;
            height: 64px;
            background: linear-gradient(180deg, #1e73e8 0%, #1660d6 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 16px;
            font-size: 32px;
        }
        
        .logo-box h1 {
            font-size: 40px;
            font-weight: 700;
            color: #0f1724;
            margin: 0 0 6px 0;
            letter-spacing: -0.6px;
        }
        
        .logo-box h3 {
            font-size: 18px;
            font-weight: 600;
            color: #344054;
            margin: 0 0 4px 0;
            opacity: 0.95;
        }
        
        .logo-box p {
            font-size: 15px;
            color: #374151;
            margin: 0;
            line-height: 1.4;
        }
        
        /* Form header */
        .form-header {
            text-align: center;
            margin-bottom: 28px;
        }
        
        .form-header h2 {
            font-size: 28px;
            font-weight: 800;
            color: #0f1724;
            margin: 0;
        }
        
        /* Inputs */
        div[data-testid="stTextInput"] {
            margin-bottom: 14px;
        }
        
        div[data-testid="stTextInput"] label {
            font-size: 13px !important;
            font-weight: 500 !important;
            color: #344054 !important;
            margin-bottom: 6px !important;
        }
        
        div[data-testid="stTextInput"] input {
            padding: 12px 14px !important;
            border: 1px solid #e3e7ee !important;
            border-radius: 10px !important;
            font-size: 14px !important;
            transition: border-color 0.2s !important;
            box-shadow: none !important;
        }
        
        div[data-testid="stTextInput"] input:focus {
            border-color: #1e73e8 !important;
            box-shadow: 0 0 0 3px rgba(30, 115, 232, 0.1) !important;
        }
        
        /* Checkbox */
        div[data-testid="stCheckbox"] label {
            font-size: 14px !important;
            color: #374151 !important;
        }
        
        /* Button - Original colors */
        .stButton > button {
            background-color: #1e73e8 !important;
            color: white !important;
            padding: 12px 14px !important;
            border-radius: 10px !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            border: none !important;
            width: 100% !important;
        }
        
        .stButton > button:hover {
            background-color: #155ec0 !important;
        }
        
        /* Links - Original color */
        a {
            color: #1e73e8;
            text-decoration: none;
            font-size: 13px;
            font-weight: 500;
        }
        
        a:hover { text-decoration: none; }
        
        /* Footer - Original color */
        .footer {
            text-align: center;
            margin-top: 24px;
            padding-top: 24px;
            border-top: 1px solid #e3e7ee;
            font-size: 12px;
            color: #9096a4;
        }
        
        .footer p { margin: 4px 0; }
        
        .footer a {
            color: #6b7280;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ===========================
# RENDER
# ===========================
def render_page():
    """Render the login page"""
    
    #st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Logo section with original branding
    st.markdown(
        """
        <div class="logo-box">
            <div class="logo-icon">🏥</div>
            <h1>Harmony</h1>
            <h3>Emergency Triage AI System</h3>
            <p>AI-powered triage for faster, more accurate care.</p>
        </div>
        <div class="form-header">
            <h2>Staff Login</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create margins with columns - content in middle
    spacer1, content, spacer2 = st.columns([1, 5, 1])
    
    with content:
        # Inputs
        user_id = st.text_input(
            "Hospital ID or Email",
            placeholder="Enter your Hospital ID or Email",
            key="user_id"
        )
        
        password = st.text_input(
            "Password",
            placeholder="Enter your password",
            type="password",
            key="password"
        )
        
        # Remember me row
        c1, c2 = st.columns([1, 1])
        with c1:
            remember = st.checkbox("Remember me")
        with c2:
            st.markdown('<div style="text-align:right; padding-top:8px;"><a href="#">Forgot Password?</a></div>', unsafe_allow_html=True)
        
        st.markdown('<div style="height:6px;"></div>', unsafe_allow_html=True)
        
        # Login button
        if st.button("🔐 Log In", use_container_width=True):
            if not user_id.strip() or not password.strip():
                st.error("❌ Please enter both Hospital ID/Email and Password")
            else:
                st.success(f"✅ Login successful for: {user_id}")
    
    # Footer with original text and colors
    st.markdown(
        """
        <div class="footer">
            <p>© 2025 Harmony. All rights reserved. • <a href="#">Privacy Policy</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('</div>', unsafe_allow_html=True)


# ===========================
# MAIN
# ===========================
def main():
    load_custom_css()
    render_page()


if __name__ == "__main__":
    main()
