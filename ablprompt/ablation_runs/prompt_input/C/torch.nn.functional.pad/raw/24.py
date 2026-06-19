import torch
from torch.nn import functional as F

# Create a sample tensor
input_tensor = torch.randn(4, 4)

# Define the padding
pad = (1, 1, 2, 2)  # Padding for the last two dimensions

# Apply padding using different modes
padded_tensor_constant = F.pad(input_tensor, pad, mode='constant', value=0)
padded_tensor_reflect = F.pad(input_tensor, pad, mode='reflect')
padded_tensor_replicate = F.pad(input_tensor, pad, mode='replicate')
padded_tensor_circular = F.pad(input_tensor, pad, mode='circular')

print("Padded Tensor (Constant):", padded_tensor_constant)
print("Padded Tensor (Reflect):", padded_tensor_reflect)
print("Padded Tensor (Replicate):", padded_tensor_replicate)
print("Padded Tensor (Circular):", padded_tensor_circular)