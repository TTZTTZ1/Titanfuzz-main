import torch

# Prepare input data
y = torch.tensor([1.0, 2.5, 4.0])
x = None  # Using None as per constraint
dx = 0.5
dim = 0

# Call the API
result = torch.cumulative_trapezoid(y, x, dx, dim)
print(result)