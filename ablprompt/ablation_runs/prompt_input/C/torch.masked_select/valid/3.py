import torch

# Create a random tensor and a boolean mask
input_tensor = torch.randn(4, 5)
mask = torch.rand(4, 5) > 0.5

# Use torch.masked_select to get elements where the mask is True
result = torch.masked_select(input_tensor, mask)

print(result)