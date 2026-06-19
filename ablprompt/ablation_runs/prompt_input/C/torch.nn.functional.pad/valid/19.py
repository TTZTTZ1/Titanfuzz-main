import torch
import torch.nn.functional as F

# Create a sample tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding and mode
pad = (1, 1, 2, 2, 0, 0)  # Padding for each dimension (left, right, top, bottom, front, back)
mode = 'constant'
value = 5.0

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode=mode, value=value)

print(padded_tensor.shape)