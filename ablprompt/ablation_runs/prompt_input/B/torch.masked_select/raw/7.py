import torch

# Create a random tensor and a corresponding boolean mask
input_tensor = torch.randn(5, 3)
mask = torch.rand(5, 3) > 0.5

# Use torch.masked_select to select elements from the input tensor based on the mask
selected_elements = torch.masked_select(input_tensor, mask)

print(selected_elements)