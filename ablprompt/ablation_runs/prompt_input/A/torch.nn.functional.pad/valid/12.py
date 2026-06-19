import torch
import torch.nn.functional as F

# Create a sample tensor
input_tensor = torch.randn(2, 3, 4)

# Define padding parameters
padding = (1, 1)  # Padding for each dimension: (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, padding, mode='constant', value=0)

print(padded_tensor)