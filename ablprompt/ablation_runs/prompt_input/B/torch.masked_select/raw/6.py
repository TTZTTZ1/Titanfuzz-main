import torch

# Create a random tensor and a mask
input_tensor = torch.randn(4, 3)
mask = (input_tensor > 0).byte()

# Use torch.masked_select to select elements from the input tensor where the mask is True
result = torch.masked_select(input_tensor, mask)

print(result)