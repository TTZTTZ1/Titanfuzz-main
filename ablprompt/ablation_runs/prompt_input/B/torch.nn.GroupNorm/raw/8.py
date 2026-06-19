import torch
import torch.nn as nn

# Create a GroupNorm layer with 2 groups for a 4-channel input
group_norm = nn.GroupNorm(num_groups=2, num_channels=4)

# Example input tensor of shape (1, 4, 2, 2)
input_tensor = torch.randn(1, 4, 2, 2)

# Apply GroupNorm
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should be (1, 4, 2, 2)