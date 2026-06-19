import torch

# Create random input and weight tensors
input_tensor = torch.randn(1, 3, 32, 32)
weight_tensor = torch.randn(8, 3, 5, 5)

# Perform 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, bias=None, stride=1, padding=2, dilation=1, groups=1)

print(output_tensor.shape)