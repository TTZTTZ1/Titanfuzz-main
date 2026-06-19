import torch

# Create a tensor with an extra dimension of size 1
tensor = torch.randn(2, 1, 3)

# Squeeze the tensor to remove the single-dimensional entries from the shape
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor)