import torch

# Create a sample tensor
tensor = torch.tensor([[0, 0, 0], [0, 1, 0], [1, 0, 0]])

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

print(indices)