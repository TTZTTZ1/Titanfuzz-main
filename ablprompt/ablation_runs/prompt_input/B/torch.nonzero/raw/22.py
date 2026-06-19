import torch

# Create a random tensor with some zero values
tensor = torch.randn(5, 5).to(torch.float32)
tensor[2, 2] = 0
tensor[3, 3] = 0

# Use torch.nonzero to find the indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

# Print the indices
print(indices)