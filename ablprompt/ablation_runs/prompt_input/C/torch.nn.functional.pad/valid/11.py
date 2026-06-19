import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding sizes
pad_sizes = (1, 1, 2, 2, 3, 3)

# Apply padding using 'constant' mode with a specific value
padded_tensor = F.pad(input_tensor, pad_sizes, mode='constant', value=0.5)

print(padded_tensor.shape)