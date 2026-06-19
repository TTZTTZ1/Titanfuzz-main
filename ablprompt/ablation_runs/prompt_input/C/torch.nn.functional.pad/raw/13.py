import torch
import torch.nn.functional as F

# Create a sample tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding and mode
pad = (1, 1, 2, 2, 3, 3)  # Padding for each dimension (left, right, top, bottom, front, back)
mode = 'constant'
value = 0.5

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode, value)

print(padded_tensor.shape)  # Output should be (3, 8, 10)