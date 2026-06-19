import torch

# Create a random tensor with some zero values
tensor = torch.rand(5, 5) < 0.5

# Get the indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

# Print the indices
print(indices)