import torch

# Create a sample input tensor
input_tensor = torch.randn(5, 3)

# Define the dimension to index
dim = 0

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to extract the desired rows
selected_tensor = torch.index_select(input_tensor, dim, indices)

print(selected_tensor)