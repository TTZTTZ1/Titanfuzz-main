import torch

# Create a sample input tensor
x = torch.randn(5, 3)

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to select rows 0 and 2 from the input tensor
selected_tensor = torch.index_select(x, 0, indices)

print(selected_tensor)