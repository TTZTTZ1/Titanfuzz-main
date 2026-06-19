import torch

# Create a random tensor of complex numbers
input_tensor = torch.randn(5, 5, dtype=torch.complex128)

# Compute the cosine of the tensor
output_tensor = torch.cos(input_tensor)

print(output_tensor)