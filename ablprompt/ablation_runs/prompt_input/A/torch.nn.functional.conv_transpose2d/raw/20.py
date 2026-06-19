import torch
import torch.nn.functional as F

# Create some input data and weight for the convolutional transpose operation
input_data = torch.randn(1, 3, 6, 6)  # Batch size of 1, 3 channels, 6x6 spatial dimensions
weight = torch.randn(3, 1, 4, 4)    # 3 output channels, 1 input channel, 4x4 kernel size

# Perform the convolutional transpose operation
output_data = F.conv_transpose2d(input_data, weight, stride=2, padding=1)

print(output_data.shape)