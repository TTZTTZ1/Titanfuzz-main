import torch
import torch.nn.functional as F

# Create a sample tensor
tensor = torch.randn(3, 4, 5)

# Define padding and mode
pad = (2, 2, 1, 1)  # Padding for each dimension (left, right, top, bottom)
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(tensor, pad, mode=mode)

print(padded_tensor.shape)  # Output should be [3, 8, 7] after padding