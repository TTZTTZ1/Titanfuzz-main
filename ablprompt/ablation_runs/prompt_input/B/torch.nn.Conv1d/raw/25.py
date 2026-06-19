import torch
from torch.nn import Conv1d

# Example usage of Conv1d
input_tensor = torch.randn(1, 16, 50)  # Batch of 1, 16 channels, length 50
conv_layer = Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True)
output_tensor = conv_layer(input_tensor)
print(output_tensor.shape)  # Expected shape: (1, 33, 24)