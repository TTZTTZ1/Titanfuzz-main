import torch

# Create a random input tensor
input_tensor = torch.randn(5, 5, dtype=torch.float32)

# Compute the hyperbolic tangent using torch.tanh
output_tensor = torch.tanh(input_tensor)

print(output_tensor)