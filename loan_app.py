import streamlit as st
import pandas as pd
import joblib  # For loading the .pkl model

# Load the local model file
@st.cache_resource
def load_model():
    """Load the model from a local .pkl file."""
    try:
        model = joblib.load("model-in-prod.pkl")
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# Title and Description
st.title("Loan Prediction Application")
st.write("Provide the loan details to get a prediction.")

# Input Form
with st.form(key="loan_form"):
    Gender = st.selectbox("Gender (0=Female, 1=Male)", [0, 1])
    Married = st.selectbox("Married (0=No, 1=Yes)", [0, 1])
    Dependents = st.selectbox("Dependents (0, 1, 2, 3+)", [0, 1, 2, 3])
    Education = st.selectbox("Education (0=Not Graduate, 1=Graduate)", [0, 1])
    Self_Employed = st.selectbox("Self Employed (0=No, 1=Yes)", [0, 1])
    ApplicantIncome = st.number_input("Applicant Income", min_value=0, value=5000, step=500)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0.0, value=0.0, step=500.0)
    LoanAmount = st.number_input("Loan Amount (in thousands)", min_value=0.0, value=100.0, step=10.0)
    Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0.0, value=360.0, step=10.0)
    Credit_History = st.selectbox("Credit History (0.0=No, 1.0=Yes)", [0.0, 1.0])
    Property_Area = st.selectbox("Property Area (0=Urban, 1=Semiurban, 2=Rural)", [0, 1, 2])

    submit_button = st.form_submit_button(label="Predict")

# Handle Prediction
if submit_button and model:
    # Prepare input data
    input_data = pd.DataFrame([{
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area,
    }])

    try:
        # Predict using the loaded model
        prediction = model.predict(input_data)
        result = "Loan Approved" if int(prediction[0]) == 1 else "Loan Denied"
        st.subheader(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
