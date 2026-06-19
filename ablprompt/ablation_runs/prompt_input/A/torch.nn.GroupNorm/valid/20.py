import torch
import torch.nn as nn

# Create a random input tensor of shape (10, 3, 28, 28)
input_tensor = torch.randn(10, 3, 28, 28)

# Initialize GroupNorm layer with num_groups=3 and num_channels=3
group_norm_layer = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm_layer(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([10, 3, 28, 28])