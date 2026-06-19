import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 3, 5, 5)
input_tensor = torch.randn(1, 3, 5, 5)

# Create a random weight tensor for the convolution of shape (16, 3, 3, 3)
weight_tensor = torch.randn(16, 3, 3, 3)

# Perform the convolution operation
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=1)

print(output_tensor.shape)  # Output should be [1, 16, 7, 7]