import torch
import torch.nn as nn

# Create a GELU layer with tanh approximation
gelu_layer = nn.GELU(approximate='tanh')

# Generate a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the GELU activation
output_tensor = gelu_layer(input_tensor)

print(output_tensor)