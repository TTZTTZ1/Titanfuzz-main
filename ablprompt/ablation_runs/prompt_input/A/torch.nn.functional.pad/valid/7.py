import torch
import torch.nn.functional as F

# Example tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Padding parameters
pad = (10, 10, 5, 5)  # padding of (left, right, top, bottom)
mode = 'constant'     # padding mode
value = 0             # constant value if mode is 'constant'

# Applying padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, pad, mode, value)

print(padded_tensor.shape)