import torch

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Find the indices of the minimum values across dimension 1
indices = torch.argmin(tensor, dim=1, keepdim=True)

print(indices)