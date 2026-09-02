import streamlit as st
import requests
from textwrap import dedent

st.set_page_config(
    page_title="Loan Approval AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM UI STYLE
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
}

/* Hide Streamlit default menu/footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1e293b 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-title {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 5px;
}

.sidebar-subtitle {
    font-size: 13px;
    color: #cbd5e1 !important;
    line-height: 1.6;
}

/* Main hero */
.hero {
    padding: 35px 20px 25px 20px;
    text-align: center;
}

.hero-badge {
    display: inline-block;
    padding: 7px 16px;
    border-radius: 30px;
    background: #e0e7ff;
    color: #4338ca;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 15px;
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #111827;
    margin: 0;
}

.hero-subtitle {
    font-size: 16px;
    color: #64748b;
    margin-top: 10px;
}

/* Section headers */
.section-header {
    margin-top: 25px;
    margin-bottom: 12px;
}

.section-title {
    font-size: 22px;
    font-weight: 750;
    color: #111827;
    margin-bottom: 3px;
}

.section-description {
    font-size: 13px;
    color: #64748b;
}

/* Input labels */
label {
    font-weight: 600 !important;
}

/* Input boxes */
div[data-baseweb="input"] {
    border-radius: 10px;
}

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* Button */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 52px;
    font-size: 16px;
    font-weight: 700;
    border: none;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    box-shadow: 0 8px 20px rgba(79, 70, 229, 0.25);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(79, 70, 229, 0.35);
}

/* Result cards */
.result-card {
    margin-top: 25px;
    padding: 30px;
    border-radius: 20px;
    background: white;
    box-shadow: 0 10px 35px rgba(15, 23, 42, 0.10);
    text-align: center;
}

.result-approved {
    border: 2px solid #22c55e;
}

.result-rejected {
    border: 2px solid #ef4444;
}

.result-status {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 8px;
}

.result-probability {
    font-size: 48px;
    font-weight: 800;
    color: #4f46e5;
}

.result-label {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 15px;
}

/* Metrics */
div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 5px 20px rgba(15, 23, 42, 0.06);
}

/* Divider */
hr {
    margin-top: 25px;
    margin-bottom: 25px;
}

/* Small info cards */
.info-card {
    padding: 15px;
    border-radius: 12px;
    background: rgba(255,255,255,0.08);
    margin-top: 12px;
}

.info-title {
    font-weight: 700;
    font-size: 14px;
}

.info-text {
    font-size: 12px;
    color: #cbd5e1 !important;
    margin-top: 4px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🏦 Loan AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'Intelligent Loan Approval System'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="info-card">'
        '<div class="info-title">🤖 Machine Learning</div>'
        '<div class="info-text">Predicts loan approval using a trained ML model.</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-card">'
        '<div class="info-title">⚡ FastAPI Backend</div>'
        '<div class="info-text">Handles prediction requests and validation.</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-card">'
        '<div class="info-title">🗄️ MySQL Database</div>'
        '<div class="info-text">Stores submitted loan applications and predictions.</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("Loan Approval Prediction System")


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("### ✨ AI POWERED LOAN ASSESSMENT")

st.title("🏦 Loan Approval System")

st.write(
    "Enter applicant details and let our machine learning model "
    "evaluate the loan application."
)

st.divider()


# ============================================================
# APPLICANT INFORMATION
# ============================================================

st.markdown(
    """
<div class="section-header">
    <div class="section-title">👤 Applicant Information</div>
    <div class="section-description">
        Basic information about the loan applicant
    </div>
</div>
""", unsafe_allow_html=True)

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


# ============================================================
# EMPLOYMENT & INCOME
# ============================================================

st.markdown(
    """
<div class="section-header">
    <div class="section-title">💼 Employment & Income</div>
    <div class="section-description">
        Employment and financial information
    </div>
</div>
""", unsafe_allow_html=True)

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


# ============================================================
# LOAN DETAILS
# ============================================================

st.markdown(
    """
<div class="section-header">
    <div class="section-title">🏦 Loan Details</div>
    <div class="section-description">
        Information about the requested loan
    </div>
</div>
""", unsafe_allow_html=True)

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


# ============================================================
# CREDIT & RISK
# ============================================================

st.markdown(
    """
<div class="section-header">
    <div class="section-title">🛡️ Credit & Risk</div>
    <div class="section-description">
        Credit history and financial risk information
    </div>
</div>
""", unsafe_allow_html=True)

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


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "✨  Predict Loan Approval",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION LOGIC
# ============================================================

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

            # ------------------------------------------------
            # RESULT
            # ------------------------------------------------

            st.divider()

            if loan_status == "Approved":
                st.success("🎉 Loan Approved")
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