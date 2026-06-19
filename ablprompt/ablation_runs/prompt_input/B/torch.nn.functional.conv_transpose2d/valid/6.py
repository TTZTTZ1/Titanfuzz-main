import torch
from torch.nn.functional import conv_transpose2d

# Create random input and weight tensors
input_tensor = torch.randn(1, 3, 64, 64)
weight_tensor = torch.randn(3, 3, 5, 5)

# Perform 2D transposed convolution
output_tensor = conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1)

print(output_tensor.shape)  # Expected shape: [1, 3, 128, 128]