import torch

# Prepare input data
y = torch.tensor([[1, 2], [3, 4]])
dx = 0.5

# Call the API
result = torch.cumulative_trapezoid(y, dx=dx)
print(result)