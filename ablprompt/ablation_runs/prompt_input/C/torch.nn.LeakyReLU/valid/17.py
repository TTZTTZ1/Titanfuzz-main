import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Define an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the LeakyReLU activation function
output = leaky_relu(input_tensor)

# Print the output
print("Input:", input_tensor)
print("Output:", output)

# Compute the gradient
output.sum().backward()

# Print the gradients
print("Gradient of input:", input_tensor.grad)