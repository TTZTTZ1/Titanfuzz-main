import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define padding and mode
pad = (1, 1, 2, 2)  # Padding for the last two dimensions
mode = 'reflect'

# Apply padding
padded_tensor = F.pad(input_tensor, pad, mode=mode)

print("Original Tensor:")
print(input_tensor)
print("\nPadded Tensor:")
print(padded_tensor)