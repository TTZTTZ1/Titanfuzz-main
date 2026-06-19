import torch
from torch.nn.functional import pad

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Define padding
pad_values = (1, 1, 2, 2, 3, 3)

# Apply padding
padded_tensor = pad(tensor, pad_values, mode='constant', value=0)

print(padded_tensor.shape)