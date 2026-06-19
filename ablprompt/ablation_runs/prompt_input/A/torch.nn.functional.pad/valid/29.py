import torch
import torch.nn.functional as F

# Create a tensor
input_tensor = torch.randn(2, 3)

# Define padding parameters
padding = (1, 1, 2, 2)  # pad last dim by (1, 1) and second to last by (2, 2)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, padding)

print(padded_tensor)