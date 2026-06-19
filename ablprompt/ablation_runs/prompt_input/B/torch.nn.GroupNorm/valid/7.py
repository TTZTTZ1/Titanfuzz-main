import torch
import torch.nn as nn

# Create a random input tensor with shape (batch_size, num_channels, height, width)
batch_size, num_channels, height, width = 4, 8, 32, 32
input_tensor = torch.randn(batch_size, num_channels, height, width)

# Initialize GroupNorm with 2 groups and enable affine transformations
group_norm = nn.GroupNorm(num_groups=2, num_channels=num_channels, eps=1e-05, affine=True)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([4, 8, 32, 32])