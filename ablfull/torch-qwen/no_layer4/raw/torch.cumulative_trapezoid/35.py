import torch

# Prepare input data
y = torch.tensor([1, 4, 5, 8])
dx = 0.5
dim = 0

# Call the API
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)
print(result)