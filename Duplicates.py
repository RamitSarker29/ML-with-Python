# Q2. Duplicate Rows - Identify and Remove

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "Age":  [25, 30, 25, 35, 30],
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Identify duplicates
print("\nDuplicate rows:\n", df[df.duplicated()])

# Remove duplicates
df_clean = df.drop_duplicates()
print("\nAfter removing duplicates:\n", df_clean)