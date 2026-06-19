import torch

# Create a random tensor and a boolean mask
input_tensor = torch.randn(3, 4)
mask = torch.rand(3, 4) > 0.5

# Use torch.masked_select to filter elements based on the mask
filtered_elements = torch.masked_select(input_tensor, mask)

print(filtered_elements)