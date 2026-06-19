import torch

# Create a random tensor
x = torch.randn(3, 4)

# Find the indices of the minimum values across dimension 1
indices = torch.argmin(x, dim=1)

print(indices)