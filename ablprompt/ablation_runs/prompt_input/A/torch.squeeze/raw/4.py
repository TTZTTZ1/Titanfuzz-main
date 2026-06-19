import torch

# Create a tensor with an unnecessary singleton dimension
tensor = torch.randn(1, 3, 4)

# Use torch.squeeze to remove the singleton dimension
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor)