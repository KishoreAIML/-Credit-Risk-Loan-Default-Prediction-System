import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

st.set_page_config(page_title="Loan Prediction", layout="wide")
st.title("Credit Risk & Loan Default Prediction System")

st.markdown("Enter values exactly. Any numeric value is allowed.")

with st.form("prediction_form"):

    left, right = st.columns(2)

    with left:
        Interest_rate_spread = st.text_input("Interest_rate_spread", "0")
        Credit_Score = st.text_input("Credit_Score", "700")
        Negative_Amortization = st.selectbox("Negative_Amortization", ['not_neg', 'neg_amm'])
        lump_sum_payment = st.selectbox("lump_sum_payment", ['not_lpsm', 'lpsm'])
        credit_type = st.selectbox("credit_type", ['CIB', 'EQUI', 'EXP', 'CRIF'])
        Coapplicant_Credit_Type = st.selectbox("Coapplicant_Credit_Type", ['EXP', 'CIB'])

    with right:
        submission_of_application = st.selectbox("submission_of_application", ["to_inst", "not_inst"])
        LTV = st.text_input("LTV", "80")
        DTI = st.text_input("DTI", "30")
        rate_of_interest = st.text_input("rate_of_interest", "8")
        loan_amount = st.text_input("loan_amount", "1000000")
        Upfront_charges = st.text_input("Upfront_charges", "0")
        property_value = st.text_input("property_value", "0")

    submit = st.form_submit_button("Predict")

if submit:
    try:
        Interest_rate_spread = float(Interest_rate_spread)
        Credit_Score = float(Credit_Score)
        LTV = float(LTV)
        DTI = float(DTI)
        rate_of_interest = float(rate_of_interest)
        loan_amount = float(loan_amount)
        Upfront_charges = float(Upfront_charges)
        property_value = float(property_value)
    except ValueError:
        st.error("Please enter valid numeric values")
        st.stop()

    input_data = pd.DataFrame({
        "Interest_rate_spread": [Interest_rate_spread],
        "Credit_Score": [Credit_Score],
        "Negative_Amortization": [Negative_Amortization],
        "lump_sum_payment": [lump_sum_payment],
        "credit_type": [credit_type],
        "Coapplicant_Credit_Type": [Coapplicant_Credit_Type],
        "submission_of_application": [submission_of_application],
        "LTV": [LTV],
        "DTI": [DTI],
        "rate_of_interest": [rate_of_interest],
        "loan_amount": [loan_amount],
        "Upfront_charges": [Upfront_charges],
        "property_value": [property_value]
    })

    eps = 1e-6

    input_data["LTC"] = input_data["loan_amount"] / (input_data["property_value"] + input_data["Upfront_charges"] + eps)

    input_data["Interest Paid"] = input_data["rate_of_interest"] * input_data["loan_amount"]
    input_data["Total payment"] = input_data["Interest Paid"] + input_data["Upfront_charges"]

    input_data["ARP"] = (input_data["Total payment"] / (input_data["loan_amount"] + eps)) * 100

    input_data = input_data[[
        "LTV", "DTI", "LTC", "ARP",
        "Interest_rate_spread", "Credit_Score",
        "Negative_Amortization", "lump_sum_payment",
        "credit_type", "Coapplicant_Credit_Type",
        "submission_of_application"
    ]]


    input_data.replace([np.inf, -np.inf], np.nan, inplace=True)
    input_data.fillna(0, inplace=True)

    num_cols = input_data.select_dtypes(include=[np.number]).columns
    input_data[num_cols] = input_data[num_cols].clip(-1e12, 1e12)

    encoded_input = encoder.transform(input_data)
    input_scaled = scaler.transform(encoded_input)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    if prediction == 0:
        st.success(f"Low Risk Applicant")
    else:
        st.error(f"High Risk Applicant")

    st.info(f"Default Probability: {probability:.2%}")


