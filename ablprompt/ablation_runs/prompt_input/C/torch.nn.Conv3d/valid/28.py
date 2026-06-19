import torch
from torch.nn import Conv3d

# Example usage of torch.nn.Conv3d
input_tensor = torch.randn(1, 3, 4, 5, 6)  # Batch size 1, 3 input channels, 4x5x6 spatial dimensions
conv_layer = Conv3d(in_channels=3, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))
output_tensor = conv_layer(input_tensor)
print(output_tensor.shape)  # Expected output shape: torch.Size([1, 8, 4, 5, 6])