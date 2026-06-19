import torch

# Create a tensor with some singleton dimensions
tensor = torch.randn(2, 1, 3, 1, 4)

# Squeeze the tensor, removing all singleton dimensions
squeezed_tensor = torch.squeeze(tensor)

print("Original Tensor Shape:", tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)