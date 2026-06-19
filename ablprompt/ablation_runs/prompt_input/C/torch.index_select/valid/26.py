import torch

# Create a sample tensor
x = torch.randn(5, 3)

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to extract rows 0 and 2
selected_tensor = torch.index_select(x, 0, indices)

print(selected_tensor)