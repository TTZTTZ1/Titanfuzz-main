import torch
import torch.nn as nn

# Create a GELU layer with the 'tanh' approximation
gelu_layer = nn.GELU(approximate='tanh')

# Example input tensor
input_tensor = torch.randn(3, 4)

# Apply the GELU layer to the input tensor
output_tensor = gelu_layer(input_tensor)

print(output_tensor)