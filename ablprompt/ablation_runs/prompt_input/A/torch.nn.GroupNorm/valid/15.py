import torch
import torch.nn as nn

# Create a random input tensor of shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(10, 3, 224, 224)

# Define the number of channels and groups for GroupNorm
num_channels = 3
num_groups = 3

# Initialize the GroupNorm layer
group_norm = nn.GroupNorm(num_groups, num_channels)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([10, 3, 224, 224])