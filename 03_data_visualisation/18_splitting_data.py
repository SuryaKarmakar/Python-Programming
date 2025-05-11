import pandas as pd

# Sample data
data = {"Category": ["A", "B", "A", "B", "A"], "Value": [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)

# Split data into two subsets based on 'Category'
subset_A = df[df["Category"] == "A"]
subset_B = df[df["Category"] == "B"]

print("Subset A:")
print(subset_A)

print("Subset B:")
print(subset_B)
