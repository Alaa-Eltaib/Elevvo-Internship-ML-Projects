import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

# Dark UI styling
st.markdown("""
    <style>
    .stApp {background-color: #0E1117;}
    .stButton>button {background-color:#1F6FEB;color:white;border-radius:10px;height:3em;width:100%;}
    .stTextInput>div>div>input {background-color:#1A1D23;color:white;border-radius:10px;height:2.5em;}
    .stNumberInput>div>div>input {background-color:#1A1D23;color:white;border-radius:10px;height:2.5em;}
    .stSelectbox>div>div>div>select {background-color:#1A1D23;color:white;border-radius:10px;height:2.5em;}
    </style>
""", unsafe_allow_html=True)

st.title("🏦 Loan Approval Predictor")
st.write("Fill the applicant details below:")

# Columns layout
col1, col2 = st.columns(2)

with col1:
    no_of_dependents = st.number_input("Number of Dependents", min_value=0)
    education = st.selectbox("Education Level", ["graduate", "not_graduate"])
    self_employed = st.selectbox("Self Employed", ["yes", "no"])
    income_annum = st.number_input("Annual Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)

with col2:
    loan_term = st.number_input("Loan Term (months)", min_value=1)
    cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900)
    residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
    commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
    luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
    bank_asset_value = st.number_input("Bank Assets Value", min_value=0)

# Load model
MODEL_PATH = "loan_model.pkl"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    st.warning("Model file not found. Place 'loan_model.pkl' in the same folder as app.py.")
    st.stop()

if st.button("Predict Loan Approval"):
    input_df = pd.DataFrame([{
        'no_of_dependents': no_of_dependents,
        'education': education,
        'self_employed': self_employed,
        'income_annum': income_annum,
        'loan_amount': loan_amount,
        'loan_term': loan_term,
        'cibil_score': cibil_score,
        'residential_assets_value': residential_assets_value,
        'commercial_assets_value': commercial_assets_value,
        'luxury_assets_value': luxury_assets_value,
        'bank_asset_value': bank_asset_value
    }])

    try:
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")
    except Exception as e:
        st.error(f"Error while predicting: {e}")
