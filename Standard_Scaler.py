# Q8. Feature Scaling using StandardScaler (Scikit-learn)

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "Height": [160, 170, 180, 155, 175],
    "Weight": [55, 65, 75, 50, 70],
})
print("Original:\n", df)

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("\nScaled using StandardScaler:\n", df_scaled.round(4))