import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(3, 4) + 1j * torch.randn(3, 4)

# Compute the absolute value of the tensor
abs_tensor = torch.abs(input_tensor)

print(abs_tensor)