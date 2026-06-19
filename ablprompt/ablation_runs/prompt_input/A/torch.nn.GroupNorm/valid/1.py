import torch
import torch.nn as nn

# Create an input tensor of shape (10, 3, 256, 256)
input_tensor = torch.randn(10, 3, 256, 256)

# Initialize GroupNorm layer with 3 channels and number of groups equal to the number of channels
group_norm_layer = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 3, 256, 256])