import torch
import torch.nn as nn

# Example usage of GroupNorm
input_tensor = torch.randn(10, 64, 32, 32)  # Batch size=10, Channels=64, Height=32, Width=32
group_norm_layer = nn.GroupNorm(num_groups=8, num_channels=64)
output_tensor = group_norm_layer(input_tensor)
print(output_tensor.shape)  # Should be torch.Size([10, 64, 32, 32])