import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Define the SiLU layer
silu_layer = nn.SiLU()

# Apply the SiLU layer to the input tensor
output_tensor = silu_layer(input_tensor)

# Compute the gradient
output_tensor.sum().backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradient of Input Tensor:", input_tensor.grad)