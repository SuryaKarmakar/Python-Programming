# importing pandas and numpy
import pandas as pd
import numpy as np

# dictionary of lists
dict = {
    "First Score": [100, 90, np.nan, 95],
    "Second Score": [30, 45, 56, np.nan],
    "Third Score": [np.nan, 40, 80, 98],
}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

# 1: Filling null values with a single value
print(df.fillna(0))

# 2: Filling null values with the previous ones
print(df.fillna(method="ffill"))

# 3: Filling null value with the next ones
print(df.fillna(method="bfill"))

# 4: interpolate() function to fill the missing values using the linear method.
print(df.interpolate(method="linear", limit_direction="forward"))
