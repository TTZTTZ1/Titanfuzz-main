import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Use torch.argmax to find the indices of the maximum values along a dimension
max_indices = torch.argmax(tensor, dim=1)

print(max_indices)  # Output: tensor([1, 1])