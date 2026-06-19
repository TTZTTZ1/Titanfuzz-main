import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding parameters
pad = (1, 1, 2, 2, 3, 3)  # Padding for each dimension: (left, right, top, bottom, front, back)

# Apply padding using 'reflect' mode
output_tensor = F.pad(input_tensor, pad, mode='reflect')

print(output_tensor.shape)