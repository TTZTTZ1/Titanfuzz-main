import torch

# Create a random tensor with some zero values
tensor = torch.randint(0, 5, (3, 4, 5)).to(torch.float32)

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(tensor > 2, as_tuple=True)

# Print the indices
print(indices)