import pandas as pd

# Sample dataset creation
data = {
    "customer_id": range(1, 6),
    "age": [25, 45, 35, 55, 20],
    "annual_income": [30000, 60000, 45000, 80000, 20000],
    "total_transactions": [12, 15, 10, 8, 20],
    "total_spent": [1200, 1500, 1000, 1600, 2000],
    "signup_date": [
        "2019-06-01",
        "2018-07-15",
        "2019-08-09",
        "2017-06-24",
        "2020-03-02",
    ],
}

df = pd.DataFrame(data)

# Convert 'signup_date' to datetime
df["signup_date"] = pd.to_datetime(df["signup_date"])

# Feature Engineering
# 1. Spending per transaction
df["spending_per_transaction"] = df["total_spent"] / df["total_transactions"]

# 2. Customer tenure (in years)
df["customer_tenure"] = (pd.Timestamp("now") - df["signup_date"]).dt.days / 365.25

# 3. Age group
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 24, 34, 44, 54, 64, 100],
    labels=["0-24", "25-34", "35-44", "45-54", "55-64", "65+"],
)

# 4. Income to spending ratio
df["income_to_spending_ratio"] = df["annual_income"] / df["total_spent"]

# Display the DataFrame with new features
print(df)
