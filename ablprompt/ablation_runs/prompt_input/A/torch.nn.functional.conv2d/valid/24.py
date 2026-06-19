import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 3, 5, 5)
input_tensor = torch.randn(1, 3, 5, 5)

# Create a random weight tensor of shape (3, 3, 3, 3) for convolution
weight_tensor = torch.randn(3, 3, 3, 3)

# Perform 2D convolution using torch.nn.functional.conv2d
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=1)

print(output_tensor)