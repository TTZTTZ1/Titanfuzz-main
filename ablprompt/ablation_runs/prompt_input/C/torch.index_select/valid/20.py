import torch

# Create a random tensor
input_tensor = torch.randn(5, 3, 4)

# Define the dimension to select along
dim_to_select = 1

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to extract the desired part of the tensor
selected_tensor = torch.index_select(input_tensor, dim_to_select, indices)

print(selected_tensor.shape)  # Should print torch.Size([5, 2, 4])