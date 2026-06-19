import torch

# Create a tensor with an extra dimension of size 1
tensor = torch.randn(2, 1, 3)

# Squeeze out the single-dimensional entries from the shape of the tensor
squeezed_tensor = torch.squeeze(tensor)

print("Original Tensor Shape:", tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)