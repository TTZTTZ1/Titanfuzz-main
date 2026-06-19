import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 6, 6)

# Create a random weight tensor
weight_tensor = torch.randn(3, 3, 4, 4)

# Perform the transposed convolution
output_tensor = F.conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1, output_padding=0, groups=1, dilation=1)

print(output_tensor)