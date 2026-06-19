import torch

# Prepare valid input data
y = torch.tensor([1, 4, 5], dtype=torch.float)
x = torch.tensor([0, 1, 2], dtype=torch.float)
dx = 1.0
dim = 0

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)