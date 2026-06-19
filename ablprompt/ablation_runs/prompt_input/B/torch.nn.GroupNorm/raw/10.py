import torch
import torch.nn as nn

# Example input tensor
input_tensor = torch.randn(10, 64, 32, 32)

# Create a GroupNorm layer with 8 groups and affine transformations
group_norm_layer = nn.GroupNorm(num_groups=8, num_channels=64, affine=True)

# Apply the GroupNorm layer to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Should be torch.Size([10, 64, 32, 32])