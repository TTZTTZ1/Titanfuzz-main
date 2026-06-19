import torch

# Create a random tensor of shape (5, 3)
x = torch.randn(5, 3)

# Define indices to select rows 0, 2, and 4
indices = torch.tensor([0, 2, 4])

# Use torch.index_select to select the specified rows
selected_rows = torch.index_select(x, 0, indices)

print(selected_rows)