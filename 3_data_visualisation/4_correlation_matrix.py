# Step 1: Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load Your Dataset
data = {
    "Age": [30, 40, 25, 35, 28],
    "Income": [50000, 60000, 45000, 55000, 52000],
    "Savings": [20000, 30000, 15000, 25000, 22000],
}
df = pd.DataFrame(data)

# Step 3: Calculate the Correlation Matrix
correlation_matrix = df.corr()

# Step 4: Visualise the Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
