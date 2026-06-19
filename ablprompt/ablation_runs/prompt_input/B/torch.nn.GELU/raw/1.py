import torch
from torch import nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply GELU activation
gelu_layer = nn.GELU(approximate='tanh')
output_tensor = gelu_layer(input_tensor)

print(output_tensor)