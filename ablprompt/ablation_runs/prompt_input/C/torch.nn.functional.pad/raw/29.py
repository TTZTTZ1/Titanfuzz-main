import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding
pad = (1, 1, 2, 2)

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print(padded_tensor)