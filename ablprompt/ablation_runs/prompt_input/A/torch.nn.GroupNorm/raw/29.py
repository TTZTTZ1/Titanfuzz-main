import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 3, 224, 224)

# Define the number of groups and channels for GroupNorm
num_groups = 3
num_channels = 3

# Create an instance of GroupNorm
group_norm = nn.GroupNorm(num_groups, num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)