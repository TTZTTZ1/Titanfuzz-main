import torch

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Find the indices of the maximum values along dimension 1
max_indices = torch.argmax(tensor, dim=1)

print(max_indices)