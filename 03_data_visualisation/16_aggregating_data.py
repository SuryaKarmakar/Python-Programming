# The average sales per month can be calculated from daily sales data.
import pandas as pd

# Sample daily sales data
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-02-01", "2023-02-02"],
    "Sales": [100, 120, 90, 80, 110],
}
df = pd.DataFrame(data)
print("Original Data")
print(df)

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group data by month and calculate the average sales
monthly_avg_sales = df.groupby(df["Date"].dt.to_period("M")).agg({"Sales": "mean"})

print(monthly_avg_sales)
