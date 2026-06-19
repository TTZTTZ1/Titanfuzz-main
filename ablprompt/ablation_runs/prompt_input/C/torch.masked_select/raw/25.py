import torch

# Create a random tensor
input_tensor = torch.randn(4, 5)

# Create a boolean mask
mask = (input_tensor > 0).byte()

# Use torch.masked_select to filter elements based on the mask
result = torch.masked_select(input_tensor, mask)

print(result)