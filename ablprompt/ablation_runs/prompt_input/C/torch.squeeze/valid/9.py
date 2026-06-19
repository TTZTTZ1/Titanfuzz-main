import torch

# Create a tensor with some dimensions of size 1
tensor = torch.randn(1, 3, 4, 1)

# Squeeze all dimensions of size 1
squeezed_tensor = torch.squeeze(tensor)

print("Original Tensor Shape:", tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)