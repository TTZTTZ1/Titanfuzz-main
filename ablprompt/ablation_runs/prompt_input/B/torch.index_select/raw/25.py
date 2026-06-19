import torch

# Create a random tensor of shape (5, 3, 2)
x = torch.randn(5, 3, 2)

# Define indices to select along the first dimension
indices = torch.tensor([0, 2, 4])

# Use torch.index_select to select the specified slices along the first dimension
result = torch.index_select(x, 0, indices)

print(result.shape)  # Should print torch.Size([3, 3, 2])