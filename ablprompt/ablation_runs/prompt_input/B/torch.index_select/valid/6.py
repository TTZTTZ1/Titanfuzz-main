import torch

# Create a random tensor of shape (5, 3, 2)
input_tensor = torch.randn(5, 3, 2)

# Define indices to select along dimension 1
indices = torch.tensor([0, 2])

# Use torch.index_select to select the specified indices along dimension 1
output_tensor = torch.index_select(input_tensor, 1, indices)

print(output_tensor)