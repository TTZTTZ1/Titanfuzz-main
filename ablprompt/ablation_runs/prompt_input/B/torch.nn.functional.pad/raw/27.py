import torch
from torch.nn.functional import pad

# Create a random tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding
pad_tuple = (1, 1, 2, 2)

# Apply padding
output_tensor = pad(input_tensor, pad_tuple, mode='reflect')

print(output_tensor.shape)  # Should be [2, 5, 6]