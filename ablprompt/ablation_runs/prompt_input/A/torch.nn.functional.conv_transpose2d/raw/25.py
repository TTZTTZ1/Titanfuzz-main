import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the weight for the transpose convolution
weight = torch.randn(3, 3, 5, 5)

# Perform the transpose convolution
output_tensor = F.conv_transpose2d(input_tensor, weight, stride=2, padding=2)

print(output_tensor.shape)