import torch

# Create a random tensor with some zero values
input_tensor = torch.randint(0, 5, (3, 4))

# Use torch.nonzero to find the indices of non-zero elements
indices = torch.nonzero(input_tensor)

print("Indices of non-zero elements:", indices)