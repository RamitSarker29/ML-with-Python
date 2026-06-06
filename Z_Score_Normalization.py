# Q4. Z-Score Normalization

import numpy as np

dataset = [10, 20, 30, 40, 50, 60, 70]

mean = np.mean(dataset)
std  = np.std(dataset)

z_scores = [(x - mean) / std for x in dataset]

print("Dataset:  ", dataset)
print(f"Mean:     {mean:.2f}")
print(f"Std Dev:  {std:.2f}")
print("Z-Scores: ", [round(z, 4) for z in z_scores])