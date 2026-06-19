import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define padding
pad_tuple = (1, 1, 2, 2)  # Padding for the last two dimensions

# Apply padding using 'constant' mode
padded_tensor = pad(input_tensor, pad_tuple, mode='constant', value=0)

print(padded_tensor.shape)  # Output should be (5, 6)