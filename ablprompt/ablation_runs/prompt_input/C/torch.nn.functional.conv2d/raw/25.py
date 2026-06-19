import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Create a random weight tensor
weight_tensor = torch.randn(64, 3, 3, 3)

# Perform 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, padding=1, groups=3)

print(output_tensor.shape)