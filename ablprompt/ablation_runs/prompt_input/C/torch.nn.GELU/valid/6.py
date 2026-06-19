import torch
import torch.nn as nn

# Create a GELU layer with tanh approximation
gelu_layer = nn.GELU(approximate='tanh')

# Generate random input tensor
input_tensor = torch.randn(3, 4)

# Apply GELU activation
output_tensor = gelu_layer(input_tensor)

print(output_tensor)