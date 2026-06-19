import torch
import torch.nn as nn

# Example usage of GroupNorm
input_tensor = torch.randn(10, 64, 8, 8)  # Batch size 10, 64 channels, 8x8 spatial dimensions
group_norm = nn.GroupNorm(num_groups=32, num_channels=64)
normalized_output = group_norm(input_tensor)

print(normalized_output.shape)  # Should be the same as input shape: torch.Size([10, 64, 8, 8])