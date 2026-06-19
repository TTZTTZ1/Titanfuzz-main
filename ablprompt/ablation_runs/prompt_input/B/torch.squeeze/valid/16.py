import torch

# Create a tensor with some singleton dimensions
tensor = torch.randn(2, 1, 3, 1, 4)

# Squeeze out all singleton dimensions
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor.shape)