import torch
import torch.nn.functional as F

# Create a random input tensor and a weight tensor for the convolutional transpose operation
input_tensor = torch.randn(1, 3, 4, 4)
weight_tensor = torch.randn(3, 1, 2, 2)

# Perform the convolutional transpose operation
output_tensor = F.conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1)

print(output_tensor.shape)  # Output shape should be (1, 3, 8, 8)