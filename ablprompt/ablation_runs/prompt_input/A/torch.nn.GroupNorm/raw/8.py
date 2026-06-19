import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 3, 28, 28)

# Initialize GroupNorm layer with 3 channels and 7 groups
group_norm = nn.GroupNorm(num_groups=7, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)