import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(4, 4) + 1j * torch.randn(4, 4)

# Compute the sine of the tensor
output_tensor = torch.sin(input_tensor)

print(output_tensor)