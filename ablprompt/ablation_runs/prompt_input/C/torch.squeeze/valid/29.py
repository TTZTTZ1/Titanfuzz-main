import torch

# Create a tensor with an extra dimension of size 1
tensor = torch.randn(2, 1, 3, 4)

# Squeeze out the first dimension of size 1
squeezed_tensor = torch.squeeze(tensor, 1)

print("Original Tensor Shape:", tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)