import torch
import torch.nn.functional as F

# Create some dummy input data and weight
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size of 1, 3 channels, 5x5 image
weight = torch.randn(3, 3, 3, 3)      # 3 output channels, 3x3 kernel, 3 input channels

# Perform convolution
output_tensor = F.conv2d(input_tensor, weight)

print(output_tensor)