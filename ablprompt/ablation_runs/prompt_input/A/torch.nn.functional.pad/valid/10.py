import torch
import torch.nn.functional as F

# Example tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Padding parameters: (padding_left, padding_right, padding_top, padding_bottom)
pad_values = (10, 10, 5, 5)

# Using torch.nn.functional.pad to pad the input tensor
padded_tensor = F.pad(input_tensor, pad=pad_values, mode='constant', value=0)

print(padded_tensor.shape)  # Output should be [1, 3, 244, 244]