import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding
pad_size = (1, 1, 2, 2)  # Padding for the last two dimensions

# Apply padding using 'reflect' mode
padded_tensor = pad(input_tensor, pad_size, mode='reflect')

print(padded_tensor)