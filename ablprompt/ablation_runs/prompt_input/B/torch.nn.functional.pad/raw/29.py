import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding size and mode
pad_size = (1, 1, 2, 2)  # Padding for the last two dimensions
pad_mode = 'reflect'

# Apply padding
padded_tensor = pad(input_tensor, pad_size, mode=pad_mode)

print(padded_tensor.shape)