import torch

# Create a random tensor of shape (5, 3, 2)
x = torch.randn(5, 3, 2)

# Define indices to select along the second dimension
indices = torch.tensor([0, 2])

# Use torch.index_select to select the specified indices along the second dimension
result = torch.index_select(x, 1, indices)

print(result)