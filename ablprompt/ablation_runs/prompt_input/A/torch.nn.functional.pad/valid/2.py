import torch
import torch.nn.functional as F

# Create a tensor to pad
input_tensor = torch.randn(2, 3)

# Define padding parameters
pad = (1, 1, 0, 0)  # Padding of (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print("Original Tensor:")
print(input_tensor)
print("\nPadded Tensor:")
print(padded_tensor)