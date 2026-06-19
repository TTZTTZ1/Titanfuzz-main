import torch
import torch.nn as nn

# Create a sample input tensor
input_tensor = torch.randn(10, 3, 224, 224)

# Define the number of groups and channels
num_groups = 3
num_channels = input_tensor.size(1)

# Initialize GroupNorm layer
group_norm = nn.GroupNorm(num_groups, num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)