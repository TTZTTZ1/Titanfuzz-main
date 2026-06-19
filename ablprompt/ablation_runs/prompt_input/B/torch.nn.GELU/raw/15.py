import torch
from torch.nn import GELU

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply GELU activation
gelu = GELU(approximate='tanh')
output_tensor = gelu(input_tensor)

print(output_tensor)