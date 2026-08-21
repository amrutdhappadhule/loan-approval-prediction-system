from prediction import predict_loan


result = predict_loan(
    35, "Female", "Married", 2, "Graduate", "Salaried",
    6.5, 50000, 300000, 36, 12.5, "Education",
    "Yes", 10000, 0.35, 720, "No", 1
)

print(result)