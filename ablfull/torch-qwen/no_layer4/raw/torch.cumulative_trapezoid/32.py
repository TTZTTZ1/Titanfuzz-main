import torch

# Prepare valid input data
y = torch.tensor([1, 2, 4, 7])
x = torch.tensor([0, 1, 2, 3])
dx = 1.0
dim = -1

# Call the target API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)