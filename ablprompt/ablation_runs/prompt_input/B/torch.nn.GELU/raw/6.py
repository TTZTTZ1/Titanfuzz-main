import torch
import torch.nn as nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define the GELU layer with the 'tanh' approximation
gelu_layer = nn.GELU(approximate='tanh')

# Apply the GELU activation function
output_tensor = gelu_layer(input_tensor)

print(output_tensor)