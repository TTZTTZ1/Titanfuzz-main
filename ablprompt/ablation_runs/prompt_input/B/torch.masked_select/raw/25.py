import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Create a boolean mask
mask = input_tensor > 0

# Use torch.masked_select to select elements from the input tensor where the mask is True
selected_elements = torch.masked_select(input_tensor, mask)

print(selected_elements)