import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(5, 5, dtype=torch.complex64)

# Compute the cosine of the tensor
output_tensor = torch.cos(input_tensor)

print(output_tensor)