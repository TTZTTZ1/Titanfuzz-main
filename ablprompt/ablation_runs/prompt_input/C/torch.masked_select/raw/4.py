import torch

# Create a random tensor of size 5x3
input_tensor = torch.randn(5, 3)

# Create a boolean mask of the same shape as input_tensor
mask = (input_tensor > 0).byte()

# Use torch.masked_select to get elements from input_tensor where the corresponding element in mask is True
selected_elements = torch.masked_select(input_tensor, mask)

print(selected_elements)