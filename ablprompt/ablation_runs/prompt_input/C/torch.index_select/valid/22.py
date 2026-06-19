import torch

# Create a random tensor
x = torch.randn(5, 3, 4)

# Define the dimension along which to index
dim = 1

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to extract the desired slices
result = torch.index_select(x, dim, indices)

print(result)