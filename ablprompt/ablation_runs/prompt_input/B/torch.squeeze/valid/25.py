import torch

# Create a tensor with some dimensions of size 1
tensor = torch.randn(1, 3, 1, 4, 5)

# Squeeze all dimensions of size 1
squeezed_tensor = torch.squeeze(tensor)

print(squeezed_tensor.shape)