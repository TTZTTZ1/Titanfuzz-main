import torch
import torch.nn as nn

# Create a GroupNorm layer with 4 groups and 8 channels
group_norm = nn.GroupNorm(num_groups=4, num_channels=8)

# Example input tensor of shape (2, 8, 3, 3)
input_tensor = torch.randn(2, 8, 3, 3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be (2, 8, 3, 3)