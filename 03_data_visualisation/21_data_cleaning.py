import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Fill missing values for 'Age' with the mean age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# 3. Standardise Email format and handle NaN values in 'Email'
df["Email"] = df["Email"].str.lower()

# 4. Remove rows with invalid emails (simple validation), handling NaN values in the condition
df = df[df["Email"].str.contains("@", na=False)]

# Save the cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed.")
