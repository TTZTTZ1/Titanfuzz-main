import torch

# Generate input data
y = torch.tensor([1, 4, 9, 16])
x = torch.tensor([0, 1, 2, 3])
dx = 1.0
dim = -1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)