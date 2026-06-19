import torch

# Create a tensor with some values
tensor = torch.tensor([[1, 0, 2], [0, 3, 0], [4, 0, 5]])

# Use torch.nonzero to find the indices of non-zero elements
non_zero_indices = torch.nonzero(tensor)

print(non_zero_indices)