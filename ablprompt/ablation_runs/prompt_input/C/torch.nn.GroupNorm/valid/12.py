import torch
import torch.nn as nn

# Create a GroupNorm layer with 4 groups and 16 channels
group_norm = nn.GroupNorm(num_groups=4, num_channels=16)

# Example input tensor with shape (2, 16, 8, 8)
input_tensor = torch.randn(2, 16, 8, 8)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([2, 16, 8, 8])