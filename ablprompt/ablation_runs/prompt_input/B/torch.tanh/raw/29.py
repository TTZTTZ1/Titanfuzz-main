import torch

# Create a random input tensor of type float32
input_tensor = torch.randn(5, 5, dtype=torch.float32)

# Compute the hyperbolic tangent of the input tensor
output_tensor = torch.tanh(input_tensor)

print(output_tensor)