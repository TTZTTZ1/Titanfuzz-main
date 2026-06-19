import torch
import torch.nn as nn

# Example tensor with shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(10, 64, 32, 32)

# Create a GroupNorm layer with 8 groups
group_norm_layer = nn.GroupNorm(num_groups=8, num_channels=64)

# Apply GroupNorm to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 64, 32, 32])