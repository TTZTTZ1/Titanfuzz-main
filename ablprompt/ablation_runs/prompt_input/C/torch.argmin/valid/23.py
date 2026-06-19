import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the indices of the minimum values across dimension 1
min_indices = torch.argmin(x, dim=1, keepdim=True)

print(min_indices)