import torch
import torch.nn as nn

# Create a tensor with shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(16, 64, 32, 32)

# Initialize GroupNorm with 8 groups
group_norm = nn.GroupNorm(num_groups=8, num_channels=64)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be (16, 64, 32, 32)