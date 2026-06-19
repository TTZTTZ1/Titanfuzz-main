import torch

# Create a tensor with an extra dimension of size 1
input_tensor = torch.randn(3, 1, 4, 5)

# Squeeze the tensor to remove the dimension of size 1
squeezed_tensor = torch.squeeze(input_tensor, dim=1)

print("Original Tensor Shape:", input_tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)