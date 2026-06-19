import torch
from torch.nn import functional as F

# Define input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define weight tensor
weight_tensor = torch.randn(3, 3, 5, 5)

# Perform 2D transposed convolution
output_tensor = F.conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=2, output_padding=1, groups=3)

print(output_tensor.shape)