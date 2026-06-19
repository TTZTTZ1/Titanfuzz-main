import torch

# Create a random tensor
x = torch.randn(5, 5, 5)

# Define the dimension along which to index
dim = 1

# Define the indices to select
indices = torch.tensor([0, 2, 4])

# Use torch.index_select to extract the desired elements
result = torch.index_select(x, dim, indices)

print(result.shape)  # Should print torch.Size([5, 3, 5])