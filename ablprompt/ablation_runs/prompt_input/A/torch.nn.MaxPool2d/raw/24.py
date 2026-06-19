import torch
import torch.nn as nn

# Create an instance of MaxPool2d
maxpool = nn.MaxPool2d(kernel_size=2, stride=2)

# Example input tensor
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size 1, 3 channels, 4x4 spatial dimensions

# Apply max pooling
output_tensor = maxpool(input_tensor)

print(output_tensor)