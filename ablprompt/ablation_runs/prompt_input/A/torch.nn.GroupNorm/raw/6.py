import torch
import torch.nn as nn

# Create an input tensor of shape (batch_size, channels, height, width)
input_tensor = torch.randn(16, 3, 224, 224)

# Define the number of groups and channels
num_groups = 8
num_channels = 3

# Initialize GroupNorm layer
group_norm = nn.GroupNorm(num_groups, num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([16, 3, 224, 224])