import torch
import torch.nn as nn

# Example usage of GroupNorm
input_tensor = torch.randn(10, 6, 4, 4)  # Batch size 10, 6 channels, 4x4 spatial dimensions
group_norm = nn.GroupNorm(num_groups=3, num_channels=6)
output_tensor = group_norm(input_tensor)
print(output_tensor.shape)  # Should be torch.Size([10, 6, 4, 4])