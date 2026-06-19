import torch
import torch.nn as nn

# Create a GELU layer
gelu_layer = nn.GELU(approximate="tanh")

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the GELU activation function
output_tensor = gelu_layer(input_tensor)

print(output_tensor)