import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Create an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the LeakyReLU layer to the input tensor
output_tensor = leaky_relu(input_tensor)

# Print the output tensor
print("Output Tensor:", output_tensor)

# Compute the gradient of the output tensor with respect to the input tensor
output_tensor.sum().backward()

# Print the gradients of the input tensor
print("Gradients of Input Tensor:", input_tensor.grad)