from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prediction import predict_loan
from api.schemas import LoanApplicant
from api.database import save_application

app = FastAPI(
    title="Loan Approval Prediction API",
    description="API for predicting loan approval using a trained machine learning model.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "message": "Loan Approval API is running"
    }

@app.post("/predict")
def predict(applicant: LoanApplicant):

    result = predict_loan(
        applicant.Age,
        applicant.Gender,
        applicant.Marital_Status,
        applicant.Dependents,
        applicant.Education,
        applicant.Employment_Type,
        applicant.Years_of_Employment,
        applicant.Monthly_Income,
        applicant.Loan_Amount,
        applicant.Loan_Term,
        applicant.Interest_Rate,
        applicant.Loan_Purpose,
        applicant.Existing_Loan,
        applicant.Monthly_EMI,
        applicant.Debt_to_Income_Ratio,
        applicant.Credit_Score,
        applicant.Previous_Default,
        applicant.Number_of_Late_Payments
    )

    save_data = (
        applicant.Age,
        applicant.Gender,
        applicant.Marital_Status,
        applicant.Dependents,
        applicant.Education,
        applicant.Employment_Type,
        applicant.Years_of_Employment,
        applicant.Monthly_Income,
        applicant.Loan_Amount,
        applicant.Loan_Term,
        applicant.Interest_Rate,
        applicant.Loan_Purpose,
        applicant.Existing_Loan,
        applicant.Monthly_EMI,
        applicant.Debt_to_Income_Ratio,
        applicant.Credit_Score,
        applicant.Previous_Default,
        applicant.Number_of_Late_Payments,
        result["loan_status"],
        result["approval_probability"]
    )

    save_application(save_data)

    return result