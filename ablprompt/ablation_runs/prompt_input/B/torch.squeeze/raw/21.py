import torch

# Create a tensor with some dimensions of size 1
tensor = torch.randn(1, 3, 1, 4)

# Squeeze the tensor to remove dimensions of size 1
squeezed_tensor = torch.squeeze(tensor)

print("Original tensor shape:", tensor.shape)
print("Squeezed tensor shape:", squeezed_tensor.shape)