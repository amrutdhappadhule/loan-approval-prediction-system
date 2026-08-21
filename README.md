# Intelligent Loan Approval Prediction System

## 1. Project Overview

The Intelligent Loan Approval Prediction System is a machine learning-based application designed to predict whether a loan application is likely to be approved or rejected based on applicant, financial, employment, credit, and loan-related information.

The project combines a trained machine learning model with a FastAPI backend and Streamlit frontend to provide an end-to-end loan prediction system.

## 2. Problem Statement

Traditional loan evaluation can involve manual assessment of applicant information, which may be time-consuming and inconsistent.

This project aims to develop a machine learning-based system that can analyze applicant information and provide a predicted loan decision along with an approval probability.

## 3. Objectives

- Analyze applicant and loan-related information.
- Perform data preprocessing and feature engineering.
- Train and evaluate machine learning models.
- Select and save the trained model for prediction.
- Provide a reusable prediction function.
- Develop a REST API using FastAPI.
- Develop an interactive frontend using Streamlit.
- Integrate the frontend with the prediction API.
- Prepare the application for cloud deployment.

## 4. Key Features

- Applicant information processing
- Financial and employment feature processing
- Credit-related feature processing
- Feature engineering
- Machine learning-based prediction
- Approval probability
- FastAPI REST API
- Streamlit web interface
- Saved model and preprocessing artifacts
- API error handling
- Local deployment-ready architecture

## 5. System Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  | HTTP POST Request
  v
FastAPI Backend
  |
  v
Prediction Function
  |
  v
Preprocessing & Scaling
  |
  v
Trained ML Model
  |
  v
Loan Status + Approval Probability
  |
  v
Streamlit Frontend
```

## 6. Machine Learning Workflow

The machine learning workflow follows a structured data science process, starting from understanding the problem and dataset and continuing through preprocessing, feature engineering, model training, evaluation, and deployment.

### Workflow

```text
Problem Definition
       ↓
Data Collection
       ↓
Data Validation
       ↓
Exploratory Data Analysis
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Feature Selection
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Saving
       ↓
Reusable Prediction
       ↓
FastAPI Integration
       ↓
Streamlit Integration
```

## 7. Feature Engineering

Feature engineering was performed to create additional meaningful features from the original applicant and loan-related attributes.

### Annual Income

Annual income is calculated from the applicant's monthly income.

Annual Income = Monthly Income × 12

### Loan-to-Income Ratio

The Loan-to-Income Ratio represents the loan amount relative to the applicant's annual income.

Loan-to-Income Ratio = Loan Amount / Annual Income

### EMI-to-Income Ratio

The EMI-to-Income Ratio represents the proportion of monthly income used for the monthly EMI.

EMI-to-Income Ratio = Monthly EMI / Monthly Income

### Disposable Income

Disposable income represents the income remaining after deducting the monthly EMI.

Disposable Income = Monthly Income − Monthly EMI

### Additional Engineered Features

The project also includes categorical and derived features such as:

- Age Group
- Income Category
- Employment Stability
- Credit Score Category
- Debt Burden Category
- Late Payment Category
- Loan Amount Category
- Interest Rate Category

These features help represent different financial, employment, credit, and loan-risk characteristics for the machine learning model.

## 8. Prediction System

The prediction system provides a reusable function for making loan approval predictions from applicant information.

The system loads the trained machine learning model and the preprocessing artifacts required to reproduce the feature structure used during training.

The following artifacts are stored in the models/ directory:

```
models/
├── loan_approval_model.pkl
├── standard_scaler.pkl
├── selected_features.pkl
└── preprocessing_config.json
```

The prediction process performs the required feature construction, encoding, preprocessing, and scaling before passing the prepared data to the trained model.

The system returns the predicted loan status and approval probability.

### Example Response

```json
{
  "loan_status": "Approved",
  "approval_probability": 83.79
}
```

## 9. Backend – FastAPI

The backend of the application is developed using FastAPI.

FastAPI provides a REST API through which the frontend can send applicant information to the machine learning prediction system.

The backend is responsible for:

- Receiving loan application data.
- Validating the incoming request.
- Passing the data to the prediction function.
- Generating the machine learning prediction.
- Returning the loan status and approval probability as JSON.

### Prediction Endpoint

```
POST /predict
```

### Example Response

```json
{
  "loan_status": "Approved",
  "approval_probability": 83.79
}
```

FastAPI also provides interactive API documentation that can be used to test the endpoint during development.

## 10. Frontend – Streamlit

The frontend is developed using Streamlit to provide an interactive web interface for the loan prediction system.

The application allows users to enter applicant information such as personal details, employment information, income, loan details, EMI information, and credit-related information.

After submitting the information, Streamlit sends the data to the FastAPI backend through an HTTP request.

The prediction returned by the backend is then displayed to the user as:

- Loan Approval Status
- Approval Probability

## 11. System Architecture

The complete application follows a frontend–backend–machine-learning architecture.

```
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                HTTP POST /predict
                      │
                      ▼
              FastAPI Backend
                      │
                      ▼
              Prediction Function
                      │
                      ▼
           Feature Preparation
                      │
                      ▼
             Standard Scaler
                      │
                      ▼
             Trained ML Model
                      │
                      ▼
          Prediction + Probability
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
                   User
```

This separation allows the machine learning prediction logic to remain independent from the user interface.

## 12. Project Structure

```
loan-approval-prediction-system/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── models/
│   ├── loan_approval_model.pkl
│   ├── standard_scaler.pkl
│   ├── selected_features.pkl
│   └── preprocessing_config.json
│
├── jupyter_notebook_model_training/
│   ├── 1. theory about ml project.ipynb
│   ├── 2. pl project code origional.ipynb
│   ├── 3. testing prediction.ipynb
│   ├── 4. reusable prediction.ipynb
│   └── personal_loan_dataset.csv
│
├── prediction.py
├── test_prediction.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 13. Technologies Used

The project uses Python-based machine learning and web technologies.

**Programming Language**

- Python

**Data Science and Machine Learning**

- NumPy
- Pandas
- Scikit-learn

**Backend**

- FastAPI
- Uvicorn

**Frontend**

- Streamlit

**API Communication**

- Requests

**Development Tools**

- Jupyter Notebook
- VS Code
- Git
- GitHub

## 14. Installation and Setup

Clone the repository:

```
git clone <repository-url>
```

Navigate to the project directory:

```
cd loan-approval-prediction-system
```

Create a virtual environment:

```
python -m venv .pl_loan
```

Activate the virtual environment on Windows:

```
.pl_loan\Scripts\activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## 15. Running the Application Locally

The application consists of a FastAPI backend and a Streamlit frontend.

### Start the FastAPI Backend

Run:

```
uvicorn api.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

### Start the Streamlit Frontend

Open another terminal, activate the virtual environment, and run:

```
streamlit run frontend/app.py
```

The Streamlit application will open in the browser.

Both the FastAPI backend and Streamlit frontend must be running for the complete application to work locally.

## 16. API Testing

FastAPI provides interactive API documentation for testing the backend.

After starting the FastAPI server, open:

```
http://127.0.0.1:8000/docs
```

The /predict endpoint can be used to submit applicant information and verify the returned prediction.

## 17. Example Prediction

The following is an example applicant used to test the prediction system:

- Age: 35
- Gender: Female
- Marital Status: Married
- Dependents: 2
- Education: Graduate
- Employment Type: Salaried
- Years of Employment: 6.5
- Monthly Income: 50000
- Loan Amount: 300000
- Loan Term: 36
- Interest Rate: 12.5
- Loan Purpose: Education
- Existing Loan: Yes
- Monthly EMI: 10000
- Debt-to-Income Ratio: 0.35
- Credit Score: 720
- Previous Default: No
- Number of Late Payments: 1

Example output:

```json
{
  "loan_status": "Approved",
  "approval_probability": 83.79
}
```

## 18. Future Enhancements

The system can be extended with additional functionality to make it more robust and closer to a production-level financial application.

Planned enhancements include:

- Improved frontend UI/UX
- Reset/Clear form functionality
- Comprehensive input validation
- Model explainability
- Authentication and authorization
- Database integration
- Application history and reporting
- Monitoring and logging
- Additional model optimization
- Larger and more diverse training datasets
- Integration with additional financial verification services
- Docker containerization
- Cloud deployment

## 19. Limitations

The prediction generated by this system depends on the dataset, features, preprocessing techniques, and machine learning model used during development.

The approval probability should be considered a model output for decision support and should not be interpreted as a guaranteed loan approval.

Real-world financial institutions may require additional information, credit bureau data, document verification, regulatory checks, risk assessment, and human review before making a final lending decision.

Therefore, this application is intended as a machine learning-based loan prediction and decision-support system rather than a complete replacement for a real-world loan underwriting process.

## 20. Author

Amrut Dhappadhule
Email : amrutdhappadhule6595@gmail.com
