import torch
from torch.nn.functional import pad

# Create a sample tensor
input_tensor = torch.randn(4, 4)

# Define padding and mode
pad_sizes = (1, 1, 2, 2)  # Padding for the first two dimensions
mode = 'reflect'

# Apply padding
padded_tensor = pad(input_tensor, pad_sizes, mode=mode)

print(padded_tensor)