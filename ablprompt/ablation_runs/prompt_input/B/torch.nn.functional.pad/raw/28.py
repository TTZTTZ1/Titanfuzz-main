import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding
pad_values = (1, 1, 2, 2, 3, 3)

# Apply padding
output_tensor = pad(input_tensor, pad_values, mode='reflect')

print(output_tensor.shape)