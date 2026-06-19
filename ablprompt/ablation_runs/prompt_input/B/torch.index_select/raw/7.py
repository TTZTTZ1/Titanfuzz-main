import torch

# Create a random tensor
x = torch.randn(5, 3, 4)

# Define indices to select
indices = torch.tensor([0, 2])

# Perform index selection on the first dimension
selected_tensor = torch.index_select(x, 0, indices)

print(selected_tensor.shape)  # Should print torch.Size([2, 3, 4])