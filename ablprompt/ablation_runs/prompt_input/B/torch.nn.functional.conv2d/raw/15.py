import torch

# Create random tensors for input and weight
input_tensor = torch.randn(1, 3, 5, 5)
weight_tensor = torch.randn(8, 3, 3, 3)

# Apply 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, stride=2, padding=1, dilation=1, groups=1)

print(output_tensor.shape)