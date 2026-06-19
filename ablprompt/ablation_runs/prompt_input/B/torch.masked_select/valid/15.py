import torch

# Create a random tensor and a boolean mask
input_tensor = torch.randn(5, 3)
mask = input_tensor > 0

# Use torch.masked_select to get elements from input_tensor where mask is True
selected_elements = torch.masked_select(input_tensor, mask)

print(selected_elements)