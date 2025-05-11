# importing pandas and numpy
import pandas as pd

# dictionary of lists
data = {
    "Year": [2010, 2011, 2012],
    "Sales_A": [100, 120, 130],
    "Sales_B": [90, 110, 140],
}

# creating a dataframe from dictionary
df = pd.DataFrame(data)

print(df)

# transposing data
transposed_df = df.T
print(transposed_df)

# melting data
melted_df = pd.melt(df, id_vars="Year", var_name="Product", value_name="Sales")
print(melted_df)
