
# Triage Streamlit App

This is a Streamlit-based web application for triage assessment.  
It allows users to log in, submit triage case details, and get predictions using a trained machine learning model.



## Features

- User Login and Registration
- Triage Case Report Form
- Machine Learning Model Integration (KTAS)
- Simple and interactive UI using Streamlit

---

## Project Structure
├── app.py # Main Streamlit app
├── home.py # Home page
├── login.py # Login page
├── register.py # Register page
├── case_report.py # Triage case input
├── forget_password.py # Password reset page
├── ktas_model.pkl # Trained ML model
├── requirements.txt # Dependencies
├── images/ # Images (if any)

## How to Run the App

### 1. Install Dependencies

```bash
pip install -r requirements.txt

streamlit run app.py
The app will open in your browser at http://localhost:8501.

# Model

The app uses a pre-trained KTAS machine learning model

The model file is saved as ktas_model.pkl

It helps predict triage levels based on input data

# Deployment

This app can be deployed on Streamlit Community Cloud using this GitHub repository.

Author

Khushal Patel
GitHub: https://github.com/Khushal8320
