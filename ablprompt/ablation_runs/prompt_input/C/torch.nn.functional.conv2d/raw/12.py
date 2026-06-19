import torch
import torch.nn.functional as F

# Create random tensors for input and weights
input_tensor = torch.randn(1, 3, 5, 5)
weight_tensor = torch.randn(3, 3, 3, 3)

# Perform 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, stride=1, padding='same')

print(output_tensor.shape)  # Output should be [1, 3, 5, 5]