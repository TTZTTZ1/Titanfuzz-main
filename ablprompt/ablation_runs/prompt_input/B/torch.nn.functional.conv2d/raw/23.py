import torch
import torch.nn.functional as F

# Create random input tensor and weight tensor
input_tensor = torch.randn(1, 3, 32, 32)
weight_tensor = torch.randn(3, 3, 5, 5)

# Apply 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)