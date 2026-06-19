import torch
from torch.nn import functional as F

# Create a random input tensor
input_tensor = torch.randn(3, 4, 5)

# Define the padding scheme
pad = (1, 1, 2, 2, 3, 3)  # Padding for each dimension (left, right, top, bottom, front, back)

# Apply padding using the 'constant' mode with a value of 0
padded_tensor = F.pad(input_tensor, pad, mode='constant', value=0)

print("Original Tensor Shape:", input_tensor.shape)
print("Padded Tensor Shape:", padded_tensor.shape)