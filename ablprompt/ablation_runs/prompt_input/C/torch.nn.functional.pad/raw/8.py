import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding sizes
pad_sizes = (1, 1, 2, 2)  # Padding for the first two dimensions

# Apply padding using 'reflect' mode
padded_tensor = pad(input_tensor, pad_sizes, mode='reflect')

print(padded_tensor)