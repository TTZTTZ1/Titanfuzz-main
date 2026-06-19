import torch
import torch.nn.functional as F

# Create input tensor and weight for the convolutional transpose operation
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size of 1, 3 channels, 5x5 spatial dimensions
weight = torch.randn(3, 1, 4, 4)       # 3 output channels, 1 input channel, 4x4 kernel

# Perform the convolutional transpose operation
output_tensor = F.conv_transpose2d(input_tensor, weight)

print(output_tensor)