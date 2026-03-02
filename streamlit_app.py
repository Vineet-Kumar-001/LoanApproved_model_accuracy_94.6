import streamlit as st
import requests

# ---------------------------------------------
# Page Config
# ---------------------------------------------
st.set_page_config(page_title="Loan Prediction App 💳", layout="centered")

st.title("💰 Loan Approval Prediction")
st.write("Enter applicant details below:")

# ---------------------------------------------
# Input Fields
# ---------------------------------------------
age = st.number_input("Age", min_value=18, max_value=70, value=30)
income = st.number_input("Income", min_value=0.0, value=50000.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=20000.0)
credit_score = st.number_input("Credit Score", min_value=300.0, max_value=850.0, value=700.0)
years_exp = st.number_input("Years of Experience", min_value=0, value=5)

gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["High School", "PhD", "Masters" , "Bachelors"])
city = st.text_input("City").strip().title()
employment = st.selectbox("Employment Type", ["Salaried", "Self-Employed", "Unemployed"])

# ---------------------------------------------
# Prediction Button
# ---------------------------------------------
if st.button("Predict Loan Approval"):

    input_data = {
        "Age": age,
        "Income": income,
        "LoanAmount": loan_amount,
        "CreditScore": credit_score,
        "YearsExperience": years_exp,
        "Gender": gender,
        "Education": education,
        "City": city,
        "EmploymentType": employment
    }

    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json=input_data
        )

        if response.status_code == 200:
            result = response.json()

            if result["LoanApproved"] == 1:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

        else:
            st.error(f"API Error: {response.status_code}")

    except Exception as e:
        st.error(f"Connection Error: {e}")