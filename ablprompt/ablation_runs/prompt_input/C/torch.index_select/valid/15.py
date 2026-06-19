import torch

# Create a sample input tensor
x = torch.randn(5, 3, 4)

# Define the dimension along which to select
dim = 1

# Create a 1-D index tensor
indices = torch.tensor([0, 2])

# Use torch.index_select to extract a new tensor
selected_tensor = torch.index_select(x, dim, indices)

print(selected_tensor)