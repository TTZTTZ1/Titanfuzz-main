import torch
from torch.nn import functional as F

# Create a sample tensor
input_tensor = torch.randn(2, 3, 4)

# Define the padding
pad = (1, 1, 2, 2, 0, 0)  # Padding for dimensions (H, W, D)

# Apply padding using 'constant' mode with a value of 0
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print(padded_tensor.shape)  # Output should be (2, 7, 8)