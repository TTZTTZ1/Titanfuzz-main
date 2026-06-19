import torch

# Create a random tensor
x = torch.randn(5, 3, 4)

# Define indices for selection
indices = torch.tensor([0, 2])

# Use torch.index_select to select slices along dimension 1
selected_tensor = torch.index_select(x, 1, indices)

print(selected_tensor.shape)  # Expected output: torch.Size([5, 2, 4])