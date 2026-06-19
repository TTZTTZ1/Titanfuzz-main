import torch
import torch.nn.functional as F

# Create a tensor
input_tensor = torch.randn(2, 3)

# Define padding parameters
padding = (1, 1, 0, 0)  # Padding for each side in the format (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, padding, mode='constant', value=0)

print(padded_tensor)