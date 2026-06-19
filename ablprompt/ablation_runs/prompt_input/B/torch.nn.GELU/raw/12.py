import torch
import torch.nn as nn

# Create a GELU layer with tanh approximation
gelu_layer = nn.GELU(approximate='tanh')

# Generate some random input data
input_data = torch.randn(3, 4, 5)

# Apply the GELU activation function
output_data = gelu_layer(input_data)

print(output_data)