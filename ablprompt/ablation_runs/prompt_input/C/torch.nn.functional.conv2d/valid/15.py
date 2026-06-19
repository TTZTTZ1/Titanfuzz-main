import torch
import torch.nn.functional as F

# Create random tensors for input and weight
input_tensor = torch.randn(1, 3, 32, 32)
weight_tensor = torch.randn(64, 3, 5, 5)

# Perform 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=2, stride=1, dilation=1, groups=1)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 64, 32, 32])