import torch
import torch.nn as nn

# Create an example input tensor
input_tensor = torch.randn(10, 3, 28, 28)

# Define the GroupNorm layer
group_norm_layer = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply the GroupNorm layer to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)