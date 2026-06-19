import torch

# Create a tensor
tensor = torch.tensor([[1, 0, 2], [0, 3, 0], [4, 0, 5]])

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(tensor)

print(indices)