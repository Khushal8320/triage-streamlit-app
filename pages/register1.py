import streamlit as st

# Page configuration
st.set_page_config(page_title="Register", page_icon="📝", layout="wide")

# Initialize session state
if 'registered_users' not in st.session_state:
    st.session_state.registered_users = []

# Custom CSS for styling
st.markdown("""
<style>
    /* Hide Streamlit elements */
    .main > div { padding: 0 !important; }
    footer {visibility: hidden;}
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* Background gradient - matching the login design */
    .stApp {
        background: linear-gradient(to right, #3b5998 0%, #3b5998 17%, white 17%, white 83%, #3b5998 83%, #3b5998 100%);
    }
    
    /* Center container */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 670px !important;
    }
    
    /* Card styling */
    .main .block-container > div {
        background: white;
        padding: 50px 60px 60px;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    
    /* Logo container */
    .logo-container {
        width: 110px;
        height: 110px;
        border-radius: 24px;
        margin: 0 auto 30px;
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
    .logo-container .dot {
        position: absolute;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: rgba(255,255,255,0.6);
    }
    
    .dot-1 { top: 18px; left: 22px; background: #fbbf24; }
    .dot-2 { top: 18px; right: 22px; background: #a78bfa; }
    
    /* Title styling */
    h1 {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #1e3a8a !important;
        text-align: center !important;
        margin-bottom: 8px !important;
        line-height: 1.3 !important;
    }
    
    /* Subtitle */
    .subtitle {
        font-size: 17px;
        color: #6b7280;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 500;
    }
    
    /* Label styling */
    .stTextInput > label {
        font-size: 15px !important;
        font-weight: 600 !important;
        color: #374151 !important;
        margin-bottom: 8px !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        padding: 14px 18px !important;
        border-radius: 10px !important;
        border: 2px solid #e5e7eb !important;
        font-size: 16px !important;
        color: #6b7280 !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #9ca3af !important;
    }
    
    /* Add spacing between inputs */
    .stTextInput {
        margin-bottom: 20px !important;
    }
    
    /* Button */
    .stButton > button {
        width: 100%;
        padding: 16px;
        background: #2563eb;
        border: none;
        border-radius: 10px;
        color: white;
        font-size: 17px;
        font-weight: 600;
        margin-top: 10px;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        background: #1d4ed8;
        border: none;
    }
    
    /* Login link */
    .login-link {
        text-align: center;
        margin-top: 24px;
        font-size: 15px;
    }
    
    .login-link a {
        color: #2563eb;
        font-weight: 600;
        text-decoration: none;
    }
    
    .login-link a:hover {
        text-decoration: underline;
    }
    
    /* Success/Error messages */
    .stAlert {
        border-radius: 10px;
        margin-top: 15px;
    }
    
    /* Remove label from form */
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

# Registration form
with st.form("registration_form", clear_on_submit=False):
    full_name = st.text_input("Full Name", placeholder="Enter your full name", key="full_name")
    email = st.text_input("Email Address", placeholder="Enter your email", key="email")
    username = st.text_input("Username", placeholder="Enter your username", key="username")
    password = st.text_input("Password", placeholder="Enter your password", type="password", key="password")
    confirm_password = st.text_input("Confirm Password", placeholder="Confirm your password", type="password", key="confirm_password")
    
    submit_button = st.form_submit_button("Create Account For Emergency Triage System")
    
    if submit_button:
        # Validation
        if not all([full_name, email, username, password, confirm_password]):
            st.error("⚠️ Please fill in all fields")
        elif password != confirm_password:
            st.error("⚠️ Passwords do not match")
        elif len(password) < 6:
            st.error("⚠️ Password must be at least 6 characters long")
        elif "@" not in email:
            st.error("⚠️ Please enter a valid email address")
        else:
            # Check if username already exists
            if any(user['username'] == username for user in st.session_state.registered_users):
                st.error("⚠️ Username already exists")
            else:
                # Register user
                st.session_state.registered_users.append({
                    'full_name': full_name,
                    'email': email,
                    'username': username,
                    'password': password
                })
                st.success("✅ Account created successfully! You can now sign in to the Emergency System.")
                st.balloons()

# Login link
st.markdown("""
<div class="login-link">
    <a href="app.py">Already have an account? Sign In</a>
</div>
""", unsafe_allow_html=True)

# Debug: Show registered users (remove in production)
if st.session_state.registered_users:
    with st.expander("🔍 Registered Users (Debug)"):
        for user in st.session_state.registered_users:
            st.write(f"**{user['full_name']}** (@{user['username']}) - {user['email']}")