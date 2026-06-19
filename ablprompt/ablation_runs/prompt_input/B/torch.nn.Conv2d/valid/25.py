import torch
from torch.nn import Conv2d

# Example usage of torch.nn.Conv2d
input_tensor = torch.randn(1, 3, 32, 32)  # Batch size=1, 3 input channels, 32x32 image
conv_layer = Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1, bias=True)
output_tensor = conv_layer(input_tensor)
print(output_tensor.shape)  # Expected output shape: torch.Size([1, 64, 32, 32])