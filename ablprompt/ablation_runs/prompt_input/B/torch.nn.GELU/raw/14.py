import torch
from torch.nn import GELU

# Create an instance of GELU with the 'tanh' approximation
gelu = GELU(approximate='tanh')

# Generate a random input tensor
input_tensor = torch.randn(3, 4)

# Apply GELU to the input tensor
output_tensor = gelu(input_tensor)

print(output_tensor)