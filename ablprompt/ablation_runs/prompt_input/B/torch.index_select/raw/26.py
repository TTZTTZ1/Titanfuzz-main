import torch

# Create a random tensor
x = torch.randn(5, 3, 4)

# Define indices to select
indices = torch.tensor([0, 2])

# Perform index selection along dimension 1
result = torch.index_select(x, 1, indices)

print(result.shape)  # Expected output shape: torch.Size([5, 2, 4])