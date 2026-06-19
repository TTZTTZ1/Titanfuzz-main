import torch

# Create a tensor with some dimensions of size 1
input_tensor = torch.randn(1, 3, 4, 1)

# Squeeze the tensor to remove dimensions of size 1
squeezed_tensor = torch.squeeze(input_tensor)

print(squeezed_tensor.shape)