import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding
pad_tuple = (1, 1, 2, 2)

# Apply padding
padded_tensor = pad(input_tensor, pad_tuple, mode='reflect')

print(padded_tensor)