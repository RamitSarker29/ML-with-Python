# Q1. Missing Values - Detect, Replace, Drop

import pandas as pd
import numpy as np

data = {
    "Name":   ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age":    [25, np.nan, 30, np.nan, 22],
    "Salary": [50000, 60000, np.nan, 55000, np.nan],
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Detect missing values
print("\nMissing values (True/False):\n", df.isnull())
print("\nMissing value count per column:\n", df.isnull().sum())

# Replace with mean / median
df_filled = df.copy()
df_filled["Age"].fillna(df["Age"].mean(), inplace=True)
df_filled["Salary"].fillna(df["Salary"].median(), inplace=True)
print("\nAfter filling (Age → mean, Salary → median):\n", df_filled)

# Drop rows with any missing value
df_dropped = df.dropna()
print("\nAfter dropping rows with missing values:\n", df_dropped)