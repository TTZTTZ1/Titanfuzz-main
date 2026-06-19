import torch
import torch.nn.functional as F

# Define input tensor, weight, and bias
input_tensor = torch.randn(1, 3, 4, 4)
weight = torch.randn(3, 3, 2, 2)
bias = torch.randn(3)

# Call conv_transpose2d function
output_tensor = F.conv_transpose2d(input_tensor, weight, bias=bias, stride=2, padding=1)

print(output_tensor.shape)  # Output shape should be (1, 3, 8, 8)