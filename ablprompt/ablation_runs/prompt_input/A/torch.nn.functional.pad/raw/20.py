import torch
import torch.nn.functional as F

# Create a tensor
input_tensor = torch.randn(3, 4)

# Define padding
padding = (1, 2)  # Padding for each side: (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, padding, mode='constant', value=0)

print("Original Tensor:", input_tensor)
print("Padded Tensor:", padded_tensor)