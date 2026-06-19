import torch

# Create a random tensor
input_tensor = torch.randn(5, 5)

# Use torch.nonzero with as_tuple=True to get indices of non-zero elements
indices = torch.nonzero(input_tensor > 0, as_tuple=True)

print(indices)