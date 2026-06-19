import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 3, 4, 4)
input_tensor = torch.randn(1, 3, 4, 4)

# Create a random weight tensor of shape (16, 3, 3, 3)
weight_tensor = torch.randn(16, 3, 3, 3)

# Perform convolution using conv2d function
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=1)

print(output_tensor.shape)  # Output should be (1, 16, 4, 4)