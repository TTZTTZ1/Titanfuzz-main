import torch
import torch.nn as nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define GELU layer
gelu_layer = nn.GELU(approximate='tanh')

# Apply GELU activation
output_tensor = gelu_layer(input_tensor)

print(output_tensor)