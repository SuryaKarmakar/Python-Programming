import pandas as pd

data = {
    "StudentID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math_Score": [85, 92, 78, 90, 88],
    "Science_Score": [89, 91, 92, 85, 91],
}

df = pd.DataFrame(data)

# Filter students with Math scores greater than or equal to 90
high_math_scores = df[df["Math_Score"] >= 90]
print(high_math_scores)

# Filter data to select students with Math scores and Science scores both >= 90
high_math_and_science = df[(df["Math_Score"] >= 90) & (df["Science_Score"] >= 90)]
print(high_math_and_science)

# Filter data to select students with names starting with 'A'
names_starting_with_A = df[df["Name"].str.startswith("A")]
print(names_starting_with_A)

# Subset data to select only the 'Math_Score' column
only_high_math_scores = df[df["Math_Score"] >= 90][["Math_Score"]]
print(only_high_math_scores)
