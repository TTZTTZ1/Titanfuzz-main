import torch
import torch.nn.functional as F

# Example tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Padding parameters
pad = (10, 10, 5, 5)  # padding of (left, right, top, bottom)
mode = 'constant'
value = 0.0

# Applying padding
padded_tensor = F.pad(input_tensor, pad, mode=mode, value=value)

print(padded_tensor.shape)