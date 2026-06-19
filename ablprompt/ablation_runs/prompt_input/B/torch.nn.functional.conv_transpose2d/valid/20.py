import torch
from torch.nn.functional import conv_transpose2d

# Define input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define weight tensor
weight_tensor = torch.randn(3, 3, 5, 5)

# Perform transposed convolution
output_tensor = conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1, output_padding=1)

print(output_tensor.shape)  # Expected shape: [1, 3, 128, 128]