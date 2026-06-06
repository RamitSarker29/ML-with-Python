# Q7. One-Hot Encoding on City column

import pandas as pd

df = pd.DataFrame({"City": ["Kolkata", "Delhi", "Mumbai", "Chennai"]})
print("Original:\n", df)

df_encoded = pd.get_dummies(df, columns=["City"])
print("\nOne-Hot Encoded:\n", df_encoded)