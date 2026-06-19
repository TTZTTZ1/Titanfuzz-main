import torch

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Find the indices of the minimum values across the last dimension
min_indices = torch.argmin(tensor, dim=2)

print(min_indices)