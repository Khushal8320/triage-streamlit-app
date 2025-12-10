import streamlit as st
import pickle
import numpy as np



# Page configuration
st.set_page_config(page_title="Login", page_icon="💙", layout="wide")
# HIDE AUTO MULTIPAGE SIDEBAR LIST
st.markdown("""
<style>
/* Hide streamlit default page selector */
div[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)
# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'users' not in st.session_state:
    # Demo users for testing
    st.session_state.users = {
        'admin': 'admin123',
        'doctor1': 'password123'
    }

# Custom CSS for styling
st.markdown("""
<style>
    /* Hide Streamlit elements */
    .main > div { padding: 0 !important; }
    footer {visibility: hidden;}
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* White background */
    .stApp {
        background: white;
    }
    
    /* Center container */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 640px !important;
        margin: 0 auto !important;
    }
    
    /* Card styling */
    .main .block-container > div {
        background: white;
        padding: 40px 50px;
    }
    
    /* Logo container */
    .logo-container {
        width: 100px;
        height: 100px;
        border-radius: 24px;
        margin: 0 auto 35px;
        background: linear-gradient(135deg, #c94b4b 0%, #4b4b97 50%, #4ba3a3 100%);
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }
    
    .logo-container::before {
        content: "";
        width: 14px;
        height: 65px;
        background: white;
        border-radius: 7px;
        position: absolute;
    }
    
    .logo-container::after {
        content: "";
        width: 65px;
        height: 14px;
        background: white;
        border-radius: 7px;
        position: absolute;
    }
    
    /* Decorative dots */
    .dot {
        position: absolute;
        width: 8px;
        height: 8px;
        border-radius: 50%;
    }
    
    .dot-1 { top: 18px; left: 22px; background: #ef4444; }
    .dot-2 { top: 18px; right: 22px; background: #8b5cf6; }
    
    /* Title styling */
    h1 {
        font-size: 30px !important;
        font-weight: 700 !important;
        color: #1e40af !important;
        text-align: center !important;
        margin-bottom: 8px !important;
        line-height: 1.3 !important;
    }
    
    /* Subtitle */
    .subtitle {
        font-size: 16px;
        color: #6b7280;
        text-align: center;
        margin-bottom: 45px;
        font-weight: 400;
    }
    
    /* Label styling */
    .stTextInput > label {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #374151 !important;
        margin-bottom: 8px !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        padding: 13px 16px !important;
        border-radius: 8px !important;
        border: 1px solid #d1d5db !important;
        font-size: 15px !important;
        color: #4b5563 !important;
        background: #f9fafb !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
        background: white !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #9ca3af !important;
    }
    
    /* Input spacing */
    .stTextInput {
        margin-bottom: 20px !important;
    }
    
    /* Button */
    .stButton > button {
        width: 100% !important;
        padding: 14px !important;
        border-radius: 8px !important;
        border: 2px solid #1e40af !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        background: white !important;
        color: #1e40af !important;
        box-sizing: border-box !important;
    }
    
    .stButton > button:hover {
        background: #f0f4ff;
        border-color: #1e40af;
    }
    
    /* Sign up link */
    .signup-link {
        text-align: center;
        margin-top: 24px;
        font-size: 15px;
        color: #374151;
    }
    
    .signup-link a {
        color: #2563eb;
        font-weight: 600;
        text-decoration: none;
    }
    
    .signup-link a:hover {
        text-decoration: underline;
    }
    
    /* Success/Error messages */
    .stAlert {
        border-radius: 8px;
        margin-top: 15px;
    }
    
    /* Remove form border */
    .stForm {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Logo with decorative dots
st.markdown('''
<div class="logo-container">
    <div class="dot dot-1"></div>
    <div class="dot dot-2"></div>
</div>
''', unsafe_allow_html=True)

# Title and subtitle
st.title("Human Centred AI Approach to Predict Patient Emergency")
st.markdown('<div class="subtitle">A Machine Learning Application</div>', unsafe_allow_html=True)

# Login form
with st.form("login_form", clear_on_submit=False):
    username = st.text_input("Username/Hospital ID", placeholder="Enter your username", key="username")
    password = st.text_input("Password", placeholder="Enter your password", type="password", key="password")
    
    submit_button = st.form_submit_button("Log in")
    
    if submit_button:
        # Validation
        if not username or not password:
            st.error("⚠️ Please fill in all fields")

        elif username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.success(f"✅ Welcome back, {username}!")
            
            # 🎯 Redirect to first page
            st.switch_page("pages/first1.py")

        else:
            st.error("⚠️ Invalid username or password")

# Sign up link
col = st.container()
with col:
    st.markdown('<div class="signup-link">Already have an account?</div>', unsafe_allow_html=True)
    st.page_link("pages/register1.py", label="Sign In", icon="🔑")


# Debug: Show available users (remove in production)
with st.expander("🔍 Demo Login Credentials"):
    st.write("**Available demo accounts:**")
    for user, pwd in st.session_state.users.items():
        st.write(f"Username: `{user}` | Password: `{pwd}`")