import torch

# Prepare input data
y = torch.tensor([[1.0, 2.0, 4.0], [5.0, 6.0, 8.0]])
x = torch.tensor([0.0, 1.0, 2.0])
dx = 1.0
dim = 1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)