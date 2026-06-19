import torch

# Create a random tensor
x = torch.randn(5, 5)

# Define indices to select
indices = torch.tensor([0, 2, 4])

# Use torch.index_select to select rows
selected_rows = torch.index_select(x, 0, indices)

print(selected_rows)