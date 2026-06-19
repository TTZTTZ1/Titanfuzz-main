import torch
import torch.nn as nn

# Create a GroupNorm layer with 2 groups for an input tensor with 8 channels
group_norm_layer = nn.GroupNorm(num_groups=2, num_channels=8)

# Example input tensor with shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(4, 8, 32, 32)

# Apply the GroupNorm layer to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([4, 8, 32, 32])