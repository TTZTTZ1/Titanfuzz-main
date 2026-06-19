import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding parameters
pad = (1, 1, 2, 2)  # Padding for the first two dimensions

# Apply padding using 'reflect' mode
padded_tensor = F.pad(input_tensor, pad, mode='reflect')

print(padded_tensor)