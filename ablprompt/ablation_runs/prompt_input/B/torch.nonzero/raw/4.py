import torch

# Create a random tensor with some zero values
x = torch.randint(0, 5, (3, 4, 5)).to(torch.float32)

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(x > 2, as_tuple=True)

# Print the result
print(indices)