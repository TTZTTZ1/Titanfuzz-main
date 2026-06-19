import torch
import torch.nn.functional as F

# Create a tensor to be padded
tensor = torch.randn(2, 3)

# Define padding parameters
pad = (1, 1, 0, 0)  # Padding of 1 on both sides of each dimension

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(tensor, pad, "constant", value=0)

print("Original Tensor:", tensor)
print("Padded Tensor:", padded_tensor)