# Q6. Label Encoding on Categorical Data

from sklearn.preprocessing import LabelEncoder

colors = ["Red", "Blue", "Green", "Blue"]

le = LabelEncoder()
encoded = le.fit_transform(colors)

print("Original: ", colors)
print("Encoded:  ", list(encoded))
print("Mapping:  ", dict(zip(le.classes_, le.transform(le.classes_))))