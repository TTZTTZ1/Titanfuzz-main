import torch

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Find the index of the minimum value along dimension 1
min_index = torch.argmin(tensor, dim=1)

print(min_index)