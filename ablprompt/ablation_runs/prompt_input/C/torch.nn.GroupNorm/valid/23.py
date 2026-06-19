import torch
import torch.nn as nn

# Example usage of GroupNorm
input_tensor = torch.randn(10, 64, 7, 7)  # Batch size 10, 64 channels, 7x7 spatial dimensions
group_norm = nn.GroupNorm(num_groups=8, num_channels=64)

output_tensor = group_norm(input_tensor)
print(output_tensor.shape)  # Should be torch.Size([10, 64, 7, 7])