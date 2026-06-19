import torch

# Create a random tensor
x = torch.randn(5, 3, 4)

# Define indices to select along the second dimension
indices = torch.tensor([0, 2])

# Use torch.index_select to extract the desired slices
selected_tensor = torch.index_select(x, 1, indices)

print(selected_tensor.shape)  # Expected shape: [5, 2, 4]