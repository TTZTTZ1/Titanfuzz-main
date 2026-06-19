import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding
pad_values = (1, 1, 2, 2)

# Apply padding
padded_tensor = pad(input_tensor, pad_values, mode='reflect')

print(padded_tensor.shape)  # Output should be (2, 7, 8)