import torch
import torch.nn as nn

# Create a random input tensor with shape (batch_size, num_channels, height, width)
batch_size, num_channels, height, width = 4, 8, 32, 32
input_tensor = torch.randn(batch_size, num_channels, height, width)

# Initialize GroupNorm with 2 groups
group_norm = nn.GroupNorm(num_groups=2, num_channels=num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be the same as input_tensor.shape