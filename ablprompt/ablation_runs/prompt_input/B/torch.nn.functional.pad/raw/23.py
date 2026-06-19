import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding parameters
pad = (1, 1, 2, 2, 3, 3)  # Padding for each dimension (last to first)

# Apply padding using 'reflect' mode
padded_tensor = F.pad(input_tensor, pad, mode='reflect')

print(padded_tensor.shape)  # Output should be (3, 8, 10)