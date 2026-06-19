import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(3, 3) + 1j * torch.randn(3, 3)

# Compute the absolute value of the tensor
output_tensor = torch.abs(input_tensor)

print(output_tensor)