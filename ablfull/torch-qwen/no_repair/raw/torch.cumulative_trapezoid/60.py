import torch

# Prepare input data
y = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
x = None
dx = 0.5
dim = 1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)