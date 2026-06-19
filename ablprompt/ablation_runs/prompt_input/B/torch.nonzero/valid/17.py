import torch

# Create a random tensor
tensor = torch.rand(5, 5) > 0.5

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

print("Indices of non-zero elements:", indices)