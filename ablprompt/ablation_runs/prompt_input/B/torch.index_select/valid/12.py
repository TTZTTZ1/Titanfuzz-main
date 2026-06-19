import torch

# Create a random tensor
x = torch.randn(5, 3, 4)

# Define indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to select rows 0 and 2 along dimension 1
result = torch.index_select(x, 1, indices)

print(result.shape)  # Expected output: torch.Size([5, 2, 4])