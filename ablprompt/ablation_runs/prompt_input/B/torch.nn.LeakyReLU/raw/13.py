import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Apply the LeakyReLU activation to the input tensor
output_tensor = leaky_relu(input_tensor)

print(output_tensor)