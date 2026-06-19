import torch

# Create a sample tensor
x = torch.randn(5, 3, 4)

# Define the dimension along which to select
dim = 1

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to extract the desired elements
result = torch.index_select(x, dim, indices)

print(result)