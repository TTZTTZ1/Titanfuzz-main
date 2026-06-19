import torch
import torch.nn.functional as F

# Create a tensor to pad
input_tensor = torch.randn(2, 3)

# Define padding parameters
pad = (1, 1, 0, 0)  # Padding for each dimension: (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, pad)

print("Original Tensor:", input_tensor)
print("Padded Tensor:", padded_tensor)