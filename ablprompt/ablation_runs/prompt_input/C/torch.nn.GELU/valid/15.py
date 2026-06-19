import torch
import torch.nn as nn

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Initialize the GELU layer
gelu_layer = nn.GELU(approximate='tanh')

# Apply the GELU activation function
output_tensor = gelu_layer(input_tensor)

print(output_tensor)