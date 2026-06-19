import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define padding and mode
pad = (1, 1, 2, 2)  # Padding for the first two dimensions
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode=mode)

print(padded_tensor)