import torch

# Create a tensor with some zero and non-zero values
tensor = torch.tensor([[0, 1, 2], [3, 0, 5]])

# Use torch.nonzero to find the indices of non-zero elements
non_zero_indices = torch.nonzero(tensor)

print(non_zero_indices)