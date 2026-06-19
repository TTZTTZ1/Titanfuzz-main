import torch

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Find the indices of the minimum values along the second dimension
min_indices = torch.argmin(tensor, dim=1, keepdim=True)

print(min_indices)