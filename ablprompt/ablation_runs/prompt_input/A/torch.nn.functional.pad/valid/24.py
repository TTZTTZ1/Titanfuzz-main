import torch
import torch.nn.functional as F

# Create a tensor
tensor = torch.randn(3, 4)

# Define padding parameters
padding = (1, 2)  # Padding of 1 on each side along dimension 1 and 2

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(tensor, padding, "constant", value=0)

print(padded_tensor)