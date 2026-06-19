import torch
import torch.nn as nn

# Define the number of groups and channels
num_groups = 4
num_channels = 16

# Create an instance of GroupNorm
group_norm = nn.GroupNorm(num_groups, num_channels)

# Create a random input tensor
input_tensor = torch.randn(2, num_channels, 8, 8)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be the same as input_tensor.shape