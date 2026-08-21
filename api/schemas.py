from pydantic import BaseModel, Field
from typing import Literal


class LoanApplicant(BaseModel):

    Age: int = Field(ge=18)

    Gender: Literal[
        "Male",
        "Female",
        "Unknown"
    ]

    Marital_Status: Literal[
        "Divorced",
        "Married",
        "Single",
        "Unknown",
        "Widowed"
    ]

    Dependents: int = Field(ge=0)

    Education: Literal[
        "High School",
        "Graduate",
        "Post Graduate",
        "Doctorate"
    ]

    Employment_Type: Literal[
        "Business Owner",
        "Salaried",
        "Self-Employed",
        "Unemployed"
    ]

    Years_of_Employment: float = Field(ge=0)

    Monthly_Income: float = Field(gt=0)

    Loan_Amount: float = Field(gt=0)

    Loan_Term: int = Field(gt=0)

    Interest_Rate: float = Field(gt=0)

    Loan_Purpose: Literal[
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

    Existing_Loan: Literal[
        "Yes",
        "No"
    ]

    Monthly_EMI: float = Field(gt=0)

    Debt_to_Income_Ratio: float = Field(ge=0)

    Credit_Score: int = Field(
        ge=300,
        le=900
    )

    Previous_Default: Literal[
        "Yes",
        "No"
    ]

    Number_of_Late_Payments: int = Field(ge=0)