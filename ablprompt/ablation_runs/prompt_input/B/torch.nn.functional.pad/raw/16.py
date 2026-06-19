import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding
pad = (1, 1, 2, 2, 0, 0)

# Apply padding using 'constant' mode
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print(padded_tensor.shape)  # Expected output: torch.Size([2, 5, 6, 4])