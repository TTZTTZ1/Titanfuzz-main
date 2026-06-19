import torch
import torch.nn.functional as F

# Create a random tensor
tensor = torch.randn(4, 4)

# Define padding and mode
pad = (1, 1, 2, 2)
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(tensor, pad, mode=mode)

print(padded_tensor.shape)  # Output should be (6, 8)