import pandas as pd

# Sample data
data = {"Category": ["A", "B", "A", "B", "A"], "Value": [10, 20, 15, 25, 30]}

df = pd.DataFrame(data)
print(df)

# Group data by 'Category'
grouped = df.groupby("Category")

# Calculate the sum for each group
group_sum = grouped["Value"].sum()
print(group_sum)
