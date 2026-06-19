import torch
from torch.nn.functional import conv_transpose2d

# Example input tensor
input_tensor = torch.randn(1, 3, 6, 6)

# Example weight tensor
weight_tensor = torch.randn(3, 3, 4, 4)

# Perform 2D transposed convolution
output_tensor = conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1, output_padding=1, groups=3)

print(output_tensor.shape)