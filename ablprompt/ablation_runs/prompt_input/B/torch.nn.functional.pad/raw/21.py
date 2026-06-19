import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding and mode
pad = (1, 1, 2, 2)
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode=mode)

print(padded_tensor.shape)