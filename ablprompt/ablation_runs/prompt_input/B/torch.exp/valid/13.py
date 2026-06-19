import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(3, 3, dtype=torch.complex64)

# Compute the exponential of the input tensor
output_tensor = torch.exp(input_tensor)

print(output_tensor)