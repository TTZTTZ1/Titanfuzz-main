import torch
import torch.nn.functional as F

# Create input tensor and weight for convolutional transpose operation
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, 3 channels, 4x4 spatial dimensions
weight = torch.randn(3, 1, 2, 2)       # 3 output channels, 1 input channel, kernel size of 2x2

# Perform the convolutional transpose operation
output_tensor = F.conv_transpose2d(input_tensor, weight, stride=2)

print(output_tensor)