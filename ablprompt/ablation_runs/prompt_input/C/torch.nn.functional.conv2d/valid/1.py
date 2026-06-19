import torch
import torch.nn.functional as F

# Create random tensors for input and weights
input_tensor = torch.randn(1, 3, 5, 5)
weight_tensor = torch.randn(9, 3, 3, 3)

# Apply 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=1, stride=1, dilation=1, groups=1)

print(output_tensor.shape)