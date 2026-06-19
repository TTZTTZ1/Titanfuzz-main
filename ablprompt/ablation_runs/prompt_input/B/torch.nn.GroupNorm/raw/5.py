import torch
import torch.nn as nn

# Example usage of GroupNorm
input_tensor = torch.randn(10, 64, 32, 32)  # Batch size 10, 64 channels, 32x32 spatial dimensions
group_norm = nn.GroupNorm(num_groups=8, num_channels=64)
output_tensor = group_norm(input_tensor)
print(output_tensor.shape)  # Expected output shape: torch.Size([10, 64, 32, 32])