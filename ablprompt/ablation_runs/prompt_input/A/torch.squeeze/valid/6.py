import torch

# Create a tensor with an extra dimension of size 1
tensor = torch.randn(1, 3, 4)

# Use torch.squeeze to remove the first dimension
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor.shape)