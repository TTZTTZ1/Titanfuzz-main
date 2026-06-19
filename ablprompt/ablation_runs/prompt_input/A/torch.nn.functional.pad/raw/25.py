import torch
import torch.nn.functional as F

# Create a tensor
input_tensor = torch.randn(3, 4)

# Define padding parameters
pad = (1, 1, 2, 2)  # pad (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print("Original Tensor:", input_tensor)
print("Padded Tensor:", padded_tensor)