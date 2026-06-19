import torch

# Create a random tensor of floats between -5 and 5
input_tensor = torch.randn(10, 10) * 10

# Compute the hyperbolic tangent of the input tensor
output_tensor = torch.tanh(input_tensor)

print(output_tensor)