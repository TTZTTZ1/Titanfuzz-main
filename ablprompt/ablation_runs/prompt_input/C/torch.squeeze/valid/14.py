import torch

# Create a tensor with some dimensions of size 1
input_tensor = torch.randn(1, 3, 1, 4)

# Squeeze all dimensions of size 1
squeezed_tensor = torch.squeeze(input_tensor)

print("Original tensor shape:", input_tensor.shape)
print("Squeezed tensor shape:", squeezed_tensor.shape)