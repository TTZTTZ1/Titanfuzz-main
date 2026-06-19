import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define the GELU layer with tanh approximation
gelu_layer = nn.GELU(approximate="tanh")

# Apply the GELU activation function to the input tensor
output_tensor = gelu_layer(input_tensor)

print(output_tensor)