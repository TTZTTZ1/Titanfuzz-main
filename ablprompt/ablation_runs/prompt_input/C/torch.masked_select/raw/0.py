import torch

# Create a random tensor and a boolean mask
input_tensor = torch.randn(4, 4)
mask = (input_tensor > 0).byte()

# Use torch.masked_select to get elements from input_tensor where mask is True
result = torch.masked_select(input_tensor, mask)

print(result)