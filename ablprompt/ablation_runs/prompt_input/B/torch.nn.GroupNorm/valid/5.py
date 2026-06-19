import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(16, 64, 8, 8)

# Initialize GroupNorm with 8 groups and learnable affine parameters
group_norm = nn.GroupNorm(num_groups=8, num_channels=64, affine=True)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be the same as input_tensor.shape: (16, 64, 8, 8)