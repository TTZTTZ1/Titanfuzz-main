import torch
import torch.nn as nn

# Create a random input tensor with shape (batch_size, num_channels, height, width)
batch_size, num_channels, height, width = 8, 16, 4, 4
input_tensor = torch.randn(batch_size, num_channels, height, width)

# Initialize GroupNorm with 4 groups and enable affine transformations
group_norm = nn.GroupNorm(num_groups=4, num_channels=num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be (8, 16, 4, 4)