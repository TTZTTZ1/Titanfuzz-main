import torch

# Create a tensor with an extra dimension of size 1
tensor = torch.randn(1, 3, 4)

# Squeeze the first dimension (index 0)
squeezed_tensor = torch.squeeze(tensor, dim=0)

print(squeezed_tensor.shape)  # Output should be torch.Size([3, 4])