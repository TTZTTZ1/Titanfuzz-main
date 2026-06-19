import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 3, 224, 224)

# Define GroupNorm layer with num_groups=3 and num_channels=3
group_norm = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)