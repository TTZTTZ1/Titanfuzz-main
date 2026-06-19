import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding values
pad_values = (2, 2, 1, 1, 0, 0)

# Apply padding using 'constant' mode
padded_tensor = F.pad(input_tensor, pad_values, mode='constant', value=0)

print(padded_tensor.shape)