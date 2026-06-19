import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the index of the minimum value along dimension 1
min_indices = torch.argmin(x, dim=1, keepdim=True)

print(min_indices)