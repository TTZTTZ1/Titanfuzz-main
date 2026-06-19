import torch
import torch.nn.functional as F

# Create a tensor to pad
tensor = torch.randn(2, 3)

# Define padding parameters
padding = (1, 1, 0, 0)  # Padding for each dimension: (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(tensor, padding, mode='constant', value=0)

print("Original Tensor:")
print(tensor)
print("Padded Tensor:")
print(padded_tensor)