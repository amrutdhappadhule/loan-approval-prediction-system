import streamlit as st
import requests

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

with st.sidebar:
    st.header("🏦 Loan Approval System")

    st.write(
        "This application uses a machine learning model "
        "to predict loan approval."
    )

    st.divider()

    st.subheader("System")
    st.write("• Machine Learning")
    st.write("• FastAPI Backend")
    st.write("• Streamlit Frontend")

    st.divider()

    st.caption("Loan Approval Prediction System")

st.markdown("""
<style>

.main-title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666666;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🏦 Loan Approval Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter applicant details to predict loan approval</div>',
    unsafe_allow_html=True
)

st.header("Applicant Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Unknown"]
    )

with col3:
    marital_status = st.selectbox(
        "Marital Status",
        ["Divorced", "Married", "Single", "Unknown", "Widowed"]
    )

col4, col5 = st.columns(2)

with col4:
    dependents = st.number_input(
        "Dependents",
        min_value=0,
        max_value=20,
        value=2
    )

with col5:
    education = st.selectbox(
        "Education",
        ["High School", "Graduate", "Post Graduate", "Doctorate"]
    )
    
st.header("Employment & Income")

col1, col2, col3 = st.columns(3)

with col1:
    employment_type = st.selectbox(
        "Employment Type",
        [
            "Business Owner",
            "Salaried",
            "Self-Employed",
            "Unemployed"
        ]
    )

with col2:
    years_of_employment = st.number_input(
        "Years of Employment",
        min_value=0.0,
        max_value=50.0,
        value=6.5,
        step=0.5
    )

with col3:
    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1.0,
        value=50000.0,
        step=1000.0
    )
    
st.header("Loan Details")

col1, col2, col3 = st.columns(3)

with col1:
    loan_amount = st.number_input(
        "Loan Amount",
        min_value=1.0,
        value=300000.0,
        step=10000.0
    )

with col2:
    loan_term = st.number_input(
        "Loan Term (Months)",
        min_value=1,
        max_value=120,
        value=36
    )

with col3:
    interest_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.01,
        value=12.5,
        step=0.1
    )

col4, col5, col6 = st.columns(3)

with col4:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        [
            "Debt Consolidation",
            "Business",
            "Home Renovation",
            "Education",
            "Medical",
            "Other",
            "Wedding",
            "Travel",
            "Unknown"
        ]
    )

with col5:
    existing_loan = st.selectbox(
        "Existing Loan",
        ["Yes", "No"]
    )

with col6:
    monthly_emi = st.number_input(
        "Monthly EMI",
        min_value=1.0,
        value=10000.0,
        step=500.0
    )
    
st.header("Credit & Risk")

col1, col2, col3 = st.columns(3)

with col1:
    debt_to_income_ratio = st.number_input(
        "Debt-to-Income Ratio",
        min_value=0.0,
        value=0.35,
        step=0.01
    )

with col2:
    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=799,
        value=720
    )

with col3:
    previous_default = st.selectbox(
        "Previous Default",
        ["Yes", "No"]
    )

number_of_late_payments = st.number_input(
    "Number of Late Payments",
    min_value=0,
    value=1
)

st.divider()

predict_button = st.button(
    "Predict Loan Approval",
    type="primary",
    use_container_width=True
)

if predict_button:

    data = {
        "Age": age,
        "Gender": gender,
        "Marital_Status": marital_status,
        "Dependents": dependents,
        "Education": education,
        "Employment_Type": employment_type,
        "Years_of_Employment": years_of_employment,
        "Monthly_Income": monthly_income,
        "Loan_Amount": loan_amount,
        "Loan_Term": loan_term,
        "Interest_Rate": interest_rate,
        "Loan_Purpose": loan_purpose,
        "Existing_Loan": existing_loan,
        "Monthly_EMI": monthly_emi,
        "Debt_to_Income_Ratio": debt_to_income_ratio,
        "Credit_Score": credit_score,
        "Previous_Default": previous_default,
        "Number_of_Late_Payments": number_of_late_payments
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            loan_status = result["loan_status"]
            approval_probability = result["approval_probability"]

            st.divider()
            st.subheader("Loan Decision")

            if loan_status == "Approved":
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Approval Probability",
                    f"{approval_probability:.2f}%"
                )

            with col2:
                st.metric(
                    "Loan Status",
                    loan_status
                )

            st.progress(
                min(max(approval_probability / 100, 0.0), 1.0)
            )

        else:
            error_data = response.json()

            st.error("Invalid loan application details.")

            if "detail" in error_data:
                for error in error_data["detail"]:
                    field = error["loc"][-1]
                    message = error["msg"]

                    st.warning(
                        f"{field}: {message}"
                    )

    except requests.exceptions.RequestException:
        st.error(
            "Unable to connect to the Loan Approval API. "
            "Please make sure the FastAPI server is running."
        )