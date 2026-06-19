import torch

# Create a tensor with some singleton dimensions
tensor = torch.randn(1, 3, 4, 1)

# Squeeze out the singleton dimensions
squeezed_tensor = torch.squeeze(tensor)

print("Original tensor shape:", tensor.shape)
print("Squeezed tensor shape:", squeezed_tensor.shape)