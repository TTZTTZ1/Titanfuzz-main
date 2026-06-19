import torch

# Create a sample tensor
input_tensor = torch.randn(5, 3)

# Define the dimension to select along
dim_to_select = 0

# Define the indices to select
indices_to_select = torch.tensor([0, 2])

# Use torch.index_select to extract the desired rows
selected_tensor = torch.index_select(input_tensor, dim_to_select, indices_to_select)

print("Original Tensor:")
print(input_tensor)
print("Selected Tensor:")
print(selected_tensor)