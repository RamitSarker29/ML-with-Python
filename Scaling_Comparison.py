# Q9. Min-Max Scaling vs Standardization - Comparison

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.DataFrame({"Feature": [10, 20, 30, 40, 50]})
print("Original:\n", df)

mm_scaler  = MinMaxScaler()
std_scaler = StandardScaler()

df["Min-Max Scaled"] = mm_scaler.fit_transform(df[["Feature"]])
df["Z-Score Scaled"] = std_scaler.fit_transform(df[["Feature"]])

print("\nComparison:\n", df.round(4))