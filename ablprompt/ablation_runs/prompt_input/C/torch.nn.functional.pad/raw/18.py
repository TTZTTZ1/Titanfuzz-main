import torch
from torch.nn import functional as F

# Create a sample tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding and mode
pad = (1, 1, 2, 2)  # Padding for dimensions (height, width)
mode = 'constant'
value = 0.5

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, pad, mode=mode, value=value)

print(padded_tensor.shape)  # Output should be (2, 7, 8)