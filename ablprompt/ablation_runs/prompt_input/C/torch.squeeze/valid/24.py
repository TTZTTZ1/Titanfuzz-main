import torch

# Create a tensor with some singleton dimensions
input_tensor = torch.randn(1, 3, 1, 4, 1)

# Squeeze the tensor to remove all singleton dimensions
squeezed_tensor = torch.squeeze(input_tensor)

print("Original Tensor Shape:", input_tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)