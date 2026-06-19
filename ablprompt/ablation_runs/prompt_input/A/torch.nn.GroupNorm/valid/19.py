import torch
import torch.nn as nn

# Create a random input tensor of shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(10, 3, 224, 224)

# Define the number of channels and the group size for GroupNorm
num_channels = 3
group_size = 3

# Initialize the GroupNorm layer
group_norm_layer = nn.GroupNorm(group_size, num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 3, 224, 224])