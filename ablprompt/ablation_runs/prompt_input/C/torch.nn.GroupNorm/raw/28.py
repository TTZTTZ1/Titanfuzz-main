import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 64, 8, 8)

# Initialize GroupNorm with 8 groups and 64 channels
group_norm = nn.GroupNorm(num_groups=8, num_channels=64)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be torch.Size([10, 64, 8, 8])