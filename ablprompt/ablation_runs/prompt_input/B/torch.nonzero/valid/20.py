import torch

# Create a random tensor with some zero values
x = torch.rand(5, 5) < 0.5

# Get indices of non-zero elements as a tuple of 1D tensors
indices = torch.nonzero(x, as_tuple=True)

# Print the indices
print(indices)