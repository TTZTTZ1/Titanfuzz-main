import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding
pad = (1, 1, 2, 2, 3, 3)

# Apply padding using different modes
padded_constant = F.pad(input_tensor, pad, mode='constant', value=0)
padded_reflect = F.pad(input_tensor, pad[:4], mode='reflect')
padded_replicate = F.pad(input_tensor, pad[:4], mode='replicate')
padded_circular = F.pad(input_tensor, pad[:4], mode='circular')

print("Padded with Constant:", padded_constant.shape)
print("Padded with Reflect:", padded_reflect.shape)
print("Padded with Replicate:", padded_replicate.shape)
print("Padded with Circular:", padded_circular.shape)