import torch
import torch.nn as nn

# Create a GroupNorm layer with 2 groups for 8 channels
group_norm = nn.GroupNorm(num_groups=2, num_channels=8)

# Example input tensor of shape (2, 8, 4, 4)
input_tensor = torch.randn(2, 8, 4, 4)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be torch.Size([2, 8, 4, 4])