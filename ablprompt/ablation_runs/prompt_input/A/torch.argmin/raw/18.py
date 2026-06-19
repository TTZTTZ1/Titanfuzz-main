import torch

# Create a tensor
tensor = torch.tensor([[10, 20], [30, 40]])

# Use torch.argmin to find the indices of the minimum values along dimension 1
min_indices = torch.argmin(tensor, dim=1)

print(min_indices)  # Output: tensor([0, 0])