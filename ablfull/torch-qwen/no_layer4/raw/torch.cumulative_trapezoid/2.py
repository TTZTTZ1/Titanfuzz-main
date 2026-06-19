import torch

# Prepare valid input data
y = torch.tensor([1, 2, 4, 7], dtype=torch.float)
x = torch.tensor([0, 1, 2, 3], dtype=torch.float)
dx = 1.0
dim = -1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)

print(result)