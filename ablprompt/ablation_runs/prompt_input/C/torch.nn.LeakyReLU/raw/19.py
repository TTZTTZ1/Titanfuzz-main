import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom negative slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Create a random input tensor
input_tensor = torch.randn(3, 5)

# Apply the LeakyReLU activation function
output_tensor = leaky_relu(input_tensor)

print(output_tensor)