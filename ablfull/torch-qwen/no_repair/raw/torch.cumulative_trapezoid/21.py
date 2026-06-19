import torch

# Prepare valid input data
y = torch.tensor([1, 4, 9, 16], dtype=torch.float)
dx = 2.0
dim = 0

# Call the API
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)

print(result)