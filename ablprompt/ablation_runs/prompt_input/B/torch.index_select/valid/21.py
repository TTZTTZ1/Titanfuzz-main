import torch

# Create a random tensor of shape (5, 3, 2)
x = torch.randn(5, 3, 2)

# Define indices for dimension 1
indices = torch.tensor([0, 2])

# Use torch.index_select to select slices along dimension 1
selected_tensor = torch.index_select(x, 1, indices)

print(selected_tensor.shape)  # Output should be (5, 2, 2)