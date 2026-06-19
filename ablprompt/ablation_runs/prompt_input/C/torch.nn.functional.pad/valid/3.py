import torch
import torch.nn.functional as F

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Define padding
pad = (1, 1, 2, 2, 3, 3)

# Apply padding using 'constant' mode
padded_tensor = F.pad(tensor, pad, mode='constant', value=0)

print(padded_tensor.shape)  # Output should be (3, 8, 10)