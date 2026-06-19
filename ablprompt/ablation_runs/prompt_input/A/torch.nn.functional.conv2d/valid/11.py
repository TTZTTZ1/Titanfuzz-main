import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 3, 5, 5)
input_tensor = torch.randn(1, 3, 5, 5)

# Create a random weight tensor of shape (8, 3, 3, 3)
weight_tensor = torch.randn(8, 3, 3, 3)

# Perform convolution operation
output_tensor = F.conv2d(input_tensor, weight_tensor, stride=1, padding=0)

print(output_tensor.shape)  # Output should be (1, 8, 3, 3)