import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 8, 4, 4)

# Initialize GroupNorm with 2 groups
group_norm = nn.GroupNorm(num_groups=2, num_channels=8)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be torch.Size([1, 8, 4, 4])