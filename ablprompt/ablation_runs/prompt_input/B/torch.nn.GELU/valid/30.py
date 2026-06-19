import torch
from torch.nn import GELU

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply GELU activation
gelu_layer = GELU(approximate='tanh')
output_tensor = gelu_layer(input_tensor)

print(output_tensor)