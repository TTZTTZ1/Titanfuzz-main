import torch
from torch.nn import functional as F

# Create a sample tensor
tensor = torch.randn(4, 4)

# Define padding and mode
pad = (1, 1, 2, 2)  # Padding for the last two dimensions
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(tensor, pad, mode=mode)

print(padded_tensor)