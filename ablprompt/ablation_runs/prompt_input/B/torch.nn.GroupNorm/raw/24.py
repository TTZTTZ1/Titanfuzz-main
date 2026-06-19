import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(16, 8, 32, 32)

# Define GroupNorm with 4 groups and 8 channels
group_norm = nn.GroupNorm(num_groups=4, num_channels=8)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be the same as input_tensor.shape