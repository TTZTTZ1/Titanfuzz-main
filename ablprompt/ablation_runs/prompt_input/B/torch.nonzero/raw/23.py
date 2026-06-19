import torch

# Create a random tensor with some zero elements
x = torch.randn(5, 5)

# Use nonzero to find indices of non-zero elements
indices = torch.nonzero(x > 0, as_tuple=True)

print("Indices of non-zero elements:", indices)