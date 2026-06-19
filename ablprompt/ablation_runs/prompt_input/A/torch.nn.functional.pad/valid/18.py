import torch
import torch.nn.functional as F

# Create a tensor to be padded
tensor = torch.randn(2, 3)

# Define padding values (pad=(left, right, top, bottom))
padding = (1, 1, 2, 2)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(tensor, pad=padding, mode='constant', value=0)

print("Original Tensor:")
print(tensor)
print("Padded Tensor:")
print(padded_tensor)