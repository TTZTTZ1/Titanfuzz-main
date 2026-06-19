import torch

# Create a random tensor with complex numbers
a = torch.randn(3, 3) + 1j * torch.randn(3, 3)

# Compute the sine of the tensor
result = torch.sin(a)

print(result)