import torch
from torch.nn import functional as F

# Create a sample tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding and mode
pad = (1, 2, 0, 1)  # Padding for dimensions (height, width, depth)
mode = 'constant'
value = 0.5

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode=mode, value=value)

print(padded_tensor.shape)