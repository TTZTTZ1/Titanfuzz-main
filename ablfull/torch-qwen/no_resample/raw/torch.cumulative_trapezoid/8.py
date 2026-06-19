import torch

# Generate input data
y = torch.tensor([1.0, 2.0, 4.0, 7.0], dtype=torch.float)
dx = 0.5
dim = 0

# Call the API
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)
print(result)