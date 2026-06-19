import torch

# Create a random tensor with some zero values
tensor = torch.randint(0, 5, (3, 4))

# Use torch.nonzero to find the indices of non-zero elements
indices = torch.nonzero(tensor)

print("Indices of non-zero elements:", indices)