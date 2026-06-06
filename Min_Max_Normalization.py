# Q3. Min-Max Normalization

values = [12, 25, 40, 55, 70]

x_min = min(values)
x_max = max(values)

normalized = [(x - x_min) / (x_max - x_min) for x in values]

print("Original values: ", values)
print("x_min:", x_min, " | x_max:", x_max)
print("Normalized values:", [round(v, 4) for v in normalized])