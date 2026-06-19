import torch
import torch.nn as nn

# Create a GELU layer
gelu_layer = nn.GELU(approximate='tanh')

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the GELU layer
output_tensor = gelu_layer(input_tensor)

# Compute the gradient
output_tensor.sum().backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradient of Input Tensor:", input_tensor.grad)