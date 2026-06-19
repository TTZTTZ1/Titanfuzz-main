import torch
import torch.nn as nn

# Create a tensor with shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(10, 128, 32, 32)

# Initialize GroupNorm with 4 groups and 128 channels
group_norm = nn.GroupNorm(num_groups=4, num_channels=128)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be torch.Size([10, 128, 32, 32])