import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Initialize the GELU module with the 'tanh' approximation
gelu_module = nn.GELU(approximate='tanh')

# Apply the GELU activation function to the input tensor
output_tensor = gelu_module(input_tensor)

print(output_tensor)