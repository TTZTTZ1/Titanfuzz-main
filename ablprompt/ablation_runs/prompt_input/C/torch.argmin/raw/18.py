import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the index of the minimum value across dimension 1
min_index = torch.argmin(x, dim=1, keepdim=True)

print(min_index)