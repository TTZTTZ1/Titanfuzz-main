import torch
import torch.nn as nn

# Create an instance of Softplus with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=30.0)

# Generate a random input tensor
input_tensor = torch.randn(5, requires_grad=True)

# Apply Softplus activation
output_tensor = softplus(input_tensor)

# Compute the gradient
output_tensor.sum().backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradient:", input_tensor.grad)