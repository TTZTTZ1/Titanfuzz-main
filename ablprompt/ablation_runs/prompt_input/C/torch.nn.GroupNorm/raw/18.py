import torch
import torch.nn as nn

# Create a random input tensor with shape (batch_size, num_channels, height, width)
input_tensor = torch.randn(4, 8, 32, 32)

# Initialize GroupNorm with num_groups=2 and num_channels=8
group_norm = nn.GroupNorm(num_groups=2, num_channels=8)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([4, 8, 32, 32])