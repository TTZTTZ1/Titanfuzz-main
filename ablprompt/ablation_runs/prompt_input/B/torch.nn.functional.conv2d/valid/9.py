import torch
from torch.nn.functional import conv2d

# Create random input and weight tensors
input_tensor = torch.randn(1, 3, 32, 32)
weight_tensor = torch.randn(3, 3, 5, 5)

# Apply 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, stride=1, padding=2, dilation=1, groups=1)

print(output_tensor.shape)