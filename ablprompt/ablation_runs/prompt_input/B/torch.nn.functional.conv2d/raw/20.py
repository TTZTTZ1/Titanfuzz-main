import torch

# Create random tensors for input and weight
input_tensor = torch.randn(1, 3, 32, 32)
weight_tensor = torch.randn(3, 3, 3, 3)

# Perform 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, stride=2, padding='same', dilation=1, groups=1)

print(output_tensor.shape)