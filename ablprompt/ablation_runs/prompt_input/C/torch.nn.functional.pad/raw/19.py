import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding
pad = (1, 2, 0, 1)

# Apply padding using 'reflect' mode
padded_tensor = F.pad(input_tensor, pad, mode='reflect')

print(padded_tensor.shape)