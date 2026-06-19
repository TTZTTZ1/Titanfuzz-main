import torch
from torch.nn import functional as F

# Create a sample tensor
tensor = torch.randn(2, 3, 4)

# Define padding and mode
pad = (1, 1, 2, 2, 0, 0)  # Padding for dimensions (H, W, C)
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(tensor, pad, mode=mode)

print(padded_tensor.shape)  # Output should be [2, 7, 8, 4]