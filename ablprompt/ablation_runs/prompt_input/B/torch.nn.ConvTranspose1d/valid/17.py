import torch
from torch.nn import ConvTranspose1d

# Example usage of ConvTranspose1d
input_tensor = torch.randn(1, 16, 32)  # Batch size 1, 16 input channels, sequence length 32
conv_transpose = ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 8, 64])