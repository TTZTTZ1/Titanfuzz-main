import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding
pad = (1, 1, 2, 2, 3, 3)

# Apply padding using 'replicate' mode
padded_tensor = F.pad(input_tensor, pad, mode='replicate')

print(padded_tensor.shape)  # Expected output: torch.Size([3, 8, 10])