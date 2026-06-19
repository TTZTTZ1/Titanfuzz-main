import torch

# Create a tensor
tensor = torch.tensor([[10, 50], [30, 20]])

# Find the indices of the minimum values along dimension 1
min_indices = torch.argmin(tensor, dim=1)

print(min_indices)