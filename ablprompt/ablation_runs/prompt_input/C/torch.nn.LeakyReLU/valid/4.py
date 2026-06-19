import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Example input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply LeakyReLU to the input tensor
output_tensor = leaky_relu(input_tensor)

# Print the output tensor
print(output_tensor)