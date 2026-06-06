# Q5. Outlier Detection using Z-Score Method

import numpy as np

data = [10, 12, 11, 13, 14, 100, 12, 11, 10, 9, -90]

mean = np.mean(data)
std  = np.std(data)

print("Dataset: ", data)
print(f"Mean:    {mean:.2f}")
print(f"Std Dev: {std:.2f}")

outliers = [x for x in data if abs((x - mean) / std) > 2]
print("\nOutliers (|Z-score| > 2):", outliers)