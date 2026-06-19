import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define padding
pad = (1, 1, 2, 2)  # Padding for the last two dimensions

# Apply padding using 'constant' mode
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print(padded_tensor.shape)  # Output should be (3, 6, 8)