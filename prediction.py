import pandas as pd
import numpy as np
import pickle
import json

with open("models/loan_approval_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

with open("models/standard_scaler.pkl", "rb") as file:
    loaded_scaler = pickle.load(file)

with open("models/selected_features.pkl", "rb") as file:
    selected_features = pickle.load(file)

with open("models/preprocessing_config.json", "r") as file:
    pl_loan_data = json.load(file)


def predict_loan(
    Age,
    Gender,
    Marital_Status,
    Dependents,
    Education,
    Employment_Type,
    Years_of_Employment,
    Monthly_Income,
    Loan_Amount,
    Loan_Term,
    Interest_Rate,
    Loan_Purpose,
    Existing_Loan,
    Monthly_EMI,
    Debt_to_Income_Ratio,
    Credit_Score,
    Previous_Default,
    Number_of_Late_Payments
):
    
    # Create empty feature array
    test_array = np.zeros(len(selected_features))

    # Direct numerical features
    test_array[0] = Age
    test_array[1] = Dependents
    test_array[2] = Years_of_Employment
    test_array[3] = Monthly_Income
    test_array[4] = Loan_Amount
    test_array[5] = Loan_Term
    test_array[6] = Interest_Rate
    test_array[7] = Monthly_EMI
    test_array[8] = Debt_to_Income_Ratio
    test_array[9] = Credit_Score
    test_array[10] = Number_of_Late_Payments

    # Derived features
    Annual_Income = Monthly_Income * 12
    Loan_To_Income_Ratio = Loan_Amount / Annual_Income
    EMI_To_Income_Ratio = Monthly_EMI / Monthly_Income
    Disposable_Income = Monthly_Income - Monthly_EMI

    test_array[11] = Annual_Income
    test_array[12] = Loan_To_Income_Ratio
    test_array[13] = EMI_To_Income_Ratio
    test_array[14] = Disposable_Income

    # Binary features
    test_array[15] = pl_loan_data["existing_loan_mapping"][Existing_Loan]
    test_array[16] = pl_loan_data["previous_default_mapping"][Previous_Default]

    # Gender
    test_array[17] = pl_loan_data["gender_mapping"][Gender]

    # Marital Status
    marital_index = {
        "Divorced": 18,
        "Married": 19,
        "Single": 20,
        "Unknown": 21,
        "Widowed": 22
    }

    test_array[marital_index[Marital_Status]] = 1

    # Education
    test_array[23] = pl_loan_data["education_mapping"][Education]

    # Employment Type
    employment_index = {
        "Business Owner": 24,
        "Salaried": 25,
        "Self-Employed": 26,
        "Unemployed": 27
    }

    test_array[employment_index[Employment_Type]] = 1

    # Loan Purpose Frequency
    test_array[28] = pl_loan_data["loan_purpose_frequency"][Loan_Purpose]

    # Age Group
    age_bins = pl_loan_data["age_bins"]

    if Age < age_bins[1]:
        age_group = "Young"
    elif Age < age_bins[2]:
        age_group = "Adult"
    elif Age < age_bins[3]:
        age_group = "Middle"
    else:
        age_group = "Senior"

    test_array[29] = pl_loan_data["age_group_mapping"][age_group]

    # Income Category
    income_quantiles = pl_loan_data["income_quantiles"]

    if Monthly_Income <= income_quantiles[0]:
        income_category = "Low Income"
    elif Monthly_Income <= income_quantiles[1]:
        income_category = "Medium Income"
    elif Monthly_Income <= income_quantiles[2]:
        income_category = "High Income"
    else:
        income_category = "Very High Income"

    test_array[30] = pl_loan_data["income_mapping"][income_category]

    # Employment Stability
    rules = pl_loan_data["category_rules"]

    if Years_of_Employment <= rules["employment_stability"]["new_employee_max"]:
        stability = "New Employee"
    elif Years_of_Employment <= rules["employment_stability"]["experienced_employee_max"]:
        stability = "Experienced Employee"
    else:
        stability = "Highly Experienced Employee"

    test_array[31] = pl_loan_data["employment_stability_mapping"][stability]

    # Credit Score Category
    if Credit_Score <= 549:
        credit_category = "Poor"
    elif Credit_Score <= 649:
        credit_category = "Fair"
    elif Credit_Score <= 749:
        credit_category = "Good"
    else:
        credit_category = "Very Good"

    test_array[32] = pl_loan_data["credit_score_mapping"][credit_category]

    # Debt Burden Category
    if Debt_to_Income_Ratio <= rules["debt_burden"]["low_risk_max"]:
        debt_category = "Low Risk"
    elif Debt_to_Income_Ratio <= rules["debt_burden"]["moderate_risk_max"]:
        debt_category = "Moderate Risk"
    else:
        debt_category = "High Risk"

    test_array[33] = pl_loan_data["debt_burden_mapping"][debt_category]

    # Late Payment Category
    if Number_of_Late_Payments == rules["late_payment"]["no_delay"]:
        late_category = "No Delay"
    elif Number_of_Late_Payments <= rules["late_payment"]["few_delays_max"]:
        late_category = "Few Delays"
    else:
        late_category = "Frequent Delays"

    test_array[34] = pl_loan_data["late_payment_mapping"][late_category]

    # Loan Amount Category
    if Loan_Amount <= rules["loan_amount"]["small_max"]:
        loan_category = "Small Loan"
    elif Loan_Amount <= rules["loan_amount"]["medium_max"]:
        loan_category = "Medium Loan"
    else:
        loan_category = "Large Loan"

    test_array[35] = pl_loan_data["loan_amount_mapping"][loan_category]

    # Interest Rate Category
    if Interest_Rate < rules["interest_rate"]["low_max"]:
        interest_category = "Low Interest"
    elif Interest_Rate <= rules["interest_rate"]["medium_max"]:
        interest_category = "Medium Interest"
    else:
        interest_category = "High Interest"

    test_array[36] = pl_loan_data["interest_rate_mapping"][interest_category]

    # Scale features
    test_df = pd.DataFrame([test_array], columns=selected_features)
    scaled_array = loaded_scaler.transform(test_df)

    # Prediction
    prediction = loaded_model.predict(scaled_array)[0]

    # Probability
    approval_probability = loaded_model.predict_proba(scaled_array)[0][1]

    # Final result
    loan_status = "Approved" if prediction == 1 else "Rejected"

    return {
        "loan_status": loan_status,
        "approval_probability": round(float(approval_probability)* 100,2)
    }