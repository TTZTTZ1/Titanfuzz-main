import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the LeakyReLU activation
output_tensor = leaky_relu(input_tensor)

# Print the output
print("Output:", output_tensor)

# Compute the gradient
output_tensor.sum().backward()

# Print the gradients
print("Gradients:", input_tensor.grad)