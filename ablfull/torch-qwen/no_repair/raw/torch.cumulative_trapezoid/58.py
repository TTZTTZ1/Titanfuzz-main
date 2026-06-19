import torch

# Prepare valid input data
y = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
dx = 1.0
dim = 1

# Call the API
result = torch.cumulative_trapezoid(y, dx=dx, dim=dim)

print(result)