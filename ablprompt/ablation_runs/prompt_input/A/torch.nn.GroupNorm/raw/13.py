import torch
import torch.nn as nn

# Create a random input tensor of shape (batch_size, channels, height, width)
input_tensor = torch.randn(10, 3, 224, 224)

# Define the GroupNorm layer with 3 groups and an affine transformation
group_norm_layer = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply the GroupNorm layer to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Output should be the same shape as input_tensor