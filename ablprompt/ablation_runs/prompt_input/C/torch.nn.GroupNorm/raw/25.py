import torch
import torch.nn as nn

# Create a random input tensor with shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(16, 64, 32, 32)

# Initialize GroupNorm with 8 groups and apply affine transformations
group_norm = nn.GroupNorm(num_groups=8, num_channels=64, eps=1e-05, affine=True)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([16, 64, 32, 32])