import torch

# Create a random tensor
x = torch.randn(5, 3)

# Define the indices to select
indices = torch.tensor([0, 2, 4])

# Use torch.index_select to select rows 0, 2, and 4
selected_tensor = torch.index_select(x, 0, indices)

print(selected_tensor)