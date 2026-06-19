import torch
import torch.nn.functional as F

# Example tensor to pad
tensor = torch.randn(2, 3)

# Padding parameters: (padding_left, padding_right, padding_top, padding_bottom)
pad = (1, 1, 0, 0)

# Using torch.nn.functional.pad
padded_tensor = F.pad(tensor, pad, "constant", value=0)

print(padded_tensor)