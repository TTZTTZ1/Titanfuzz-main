import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 64, 32, 32)

# Initialize GroupNorm with 8 groups and apply affine transformations
group_norm = nn.GroupNorm(num_groups=8, num_channels=64, affine=True)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 64, 32, 32])