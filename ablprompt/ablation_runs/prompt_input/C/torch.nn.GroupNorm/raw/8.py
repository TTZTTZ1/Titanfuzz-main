import torch
import torch.nn as nn

# Example usage of GroupNorm
input_tensor = torch.randn(10, 64, 32, 32)  # Batch size 10, 64 channels, 32x32 spatial dimensions
group_norm_layer = nn.GroupNorm(num_groups=8, num_channels=64)
normalized_output = group_norm_layer(input_tensor)

print(normalized_output.shape)  # Should be torch.Size([10, 64, 32, 32])