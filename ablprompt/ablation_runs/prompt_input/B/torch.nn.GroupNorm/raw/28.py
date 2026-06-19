import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 6, 4, 4)

# Initialize GroupNorm with 3 groups and 6 channels
group_norm = nn.GroupNorm(num_groups=3, num_channels=6)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 6, 4, 4])