import torch

# Prepare valid input data
y = torch.tensor([1.0, 2.0, 4.0, 7.0])
x = None
dx = 1.0
dim = -1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)