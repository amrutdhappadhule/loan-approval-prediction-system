import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


def save_application(data):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO loan_applications (
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
        Number_of_Late_Payments,
        loan_status,
        approval_probability
    )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """

    cursor.execute(query, data)

    connection.commit()

    cursor.close()
    connection.close()