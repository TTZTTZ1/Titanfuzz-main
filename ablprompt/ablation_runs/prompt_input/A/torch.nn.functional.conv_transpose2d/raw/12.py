import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Define the convolutional transpose parameters
weight = torch.randn(3, 1, 2, 2)
bias = torch.randn(3)
stride = (2, 2)
padding = (0, 0)
output_padding = (0, 0)
groups = 1
dilation = (1, 1)

# Call the conv_transpose2d function
output_tensor = F.conv_transpose2d(input_tensor, weight, bias, stride, padding, output_padding, groups, dilation)

print(output_tensor)