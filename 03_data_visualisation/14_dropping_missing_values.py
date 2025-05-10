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

# 1: Dropping rows with at least 1 null value.
print(df.dropna())

# 2: Dropping rows if all values in that row are missing.
dict2 = {
    "First Score": [np.nan, 90, 100, 95],
    "Second Score": [np.nan, 45, 56, 30],
    "Third Score": [np.nan, 40, 80, 98],
}
df2 = pd.DataFrame(dict2)

print(df2.dropna(how="all"))

# 3: Dropping columns with at least 1 null value.
dict3 = {
    "First Score": [100, np.nan, np.nan, 95],
    "Second Score": [30, np.nan, 45, 56],
    "Third Score": [52, np.nan, 80, 98],
    "Fourth Score": [60, 67, 68, 65],
}
df3 = pd.DataFrame(dict3)

print(df3.dropna(axis=1))
