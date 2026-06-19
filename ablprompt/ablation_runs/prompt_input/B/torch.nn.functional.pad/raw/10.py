import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding
pad_values = (1, 1, 2, 2)

# Apply padding
output_tensor = pad(input_tensor, pad_values, mode='reflect')

print(output_tensor)