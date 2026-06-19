import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(5, 5) + 1j * torch.randn(5, 5)

# Compute the cosine of the input tensor
output_tensor = torch.cos(input_tensor)

print(output_tensor)