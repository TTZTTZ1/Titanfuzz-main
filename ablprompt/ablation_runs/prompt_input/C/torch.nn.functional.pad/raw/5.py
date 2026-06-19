import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(2, 3, 4)

# Define the padding scheme
pad = (1, 1, 2, 2, 0, 0)  # Padding for dimensions (H, W, C)

# Apply padding using 'constant' mode with a specific value
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=5.0)

print(padded_tensor.shape)  # Output should be (2, 7, 8)