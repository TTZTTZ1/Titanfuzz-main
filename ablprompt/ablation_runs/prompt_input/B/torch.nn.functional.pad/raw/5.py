import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define the padding size and mode
pad_size = (1, 1, 2, 2)  # Padding for the first two dimensions
mode = 'reflect'

# Apply padding
padded_tensor = pad(input_tensor, pad_size, mode=mode)

print(padded_tensor)