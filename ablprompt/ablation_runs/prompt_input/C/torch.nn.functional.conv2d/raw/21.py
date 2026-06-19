import torch
from torch.nn.functional import conv2d

# Create random tensors for input, weight, and bias
input_tensor = torch.randn(1, 3, 5, 5)
weight_tensor = torch.randn(8, 3, 3, 3)
bias_tensor = torch.randn(8)

# Apply 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)