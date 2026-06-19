import torch

# Prepare input data
y = torch.tensor([1, 2, 4, 7, 11])
x = torch.tensor([0, 1, 2, 3, 4])  # x can be None to use dx instead
dx = 1.0
dim = -1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)