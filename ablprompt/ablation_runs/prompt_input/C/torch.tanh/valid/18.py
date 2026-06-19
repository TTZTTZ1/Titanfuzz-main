import torch

# Create a random input tensor
input_tensor = torch.randn(3, 3, requires_grad=True)

# Compute the hyperbolic tangent of the input tensor
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)