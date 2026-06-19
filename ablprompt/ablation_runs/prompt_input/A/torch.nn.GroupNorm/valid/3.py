import torch
import torch.nn as nn

# Create a sample input tensor
input_tensor = torch.randn(10, 3, 28, 28)  # Batch size of 10, 3 channels, 28x28 spatial dimensions

# Initialize GroupNorm layer with 3 groups and an affine transformation
group_norm_layer = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)