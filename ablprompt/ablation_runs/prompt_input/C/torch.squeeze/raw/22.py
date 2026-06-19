import torch

# Create a tensor with some dimensions of size 1
input_tensor = torch.randn(1, 3, 1, 4, 1)

# Squeeze the tensor, removing all dimensions of size 1
squeezed_tensor = torch.squeeze(input_tensor)

print("Original Tensor Shape:", input_tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)