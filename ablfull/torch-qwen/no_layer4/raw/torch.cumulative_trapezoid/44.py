import torch

# Prepare valid input data
y = torch.tensor([1.0, 2.5, 4.0])
x = torch.tensor([0.0, 1.0, 2.0])  # Optional: if not provided, dx should be used
dx = 1.0
dim = -1

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x, dx=dx, dim=dim)
print(result)