import torch

# Create a random input tensor
input_tensor = torch.randn(3, 3, dtype=torch.float32)

# Compute the hyperbolic tangent of the input tensor
output_tensor = torch.tanh(input_tensor)

print(output_tensor)