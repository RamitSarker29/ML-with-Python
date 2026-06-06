# Q10. Convert Numeric Strings to Integer Type

import pandas as pd

df = pd.DataFrame({"Age": ["21", "25", "19", "30", "28"]})
print("Before conversion:\n", df)
print("Dtype:", df["Age"].dtype)

df["Age"] = df["Age"].astype(int)

print("\nAfter conversion:\n", df)
print("Dtype:", df["Age"].dtype)