import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Create a boolean mask
mask = input_tensor > 0

# Use torch.masked_select to get elements from input_tensor where the mask is True
result = torch.masked_select(input_tensor, mask)

print(result)