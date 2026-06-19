import torch
import torch.nn as nn

# Create an input tensor
input_tensor = torch.randn(10, 3, 224, 224)

# Define GroupNorm layer with num_groups=3 and num_channels=3
group_norm_layer = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)