import torch

# Create a random tensor of shape (5, 3)
x = torch.randn(5, 3)

# Define the indices to select from the first dimension
indices = torch.tensor([0, 2, 4])

# Use torch.index_select to select rows 0, 2, and 4 from the tensor x
selected_tensor = torch.index_select(x, 0, indices)

print(selected_tensor)