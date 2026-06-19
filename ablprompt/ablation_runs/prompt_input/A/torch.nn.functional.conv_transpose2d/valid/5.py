import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the weight for the transposed convolution
weight = torch.randn(3, 1, 4, 4)

# Perform the transposed convolution
output_tensor = F.conv_transpose2d(input_tensor, weight, stride=2, padding=1)

print(output_tensor)