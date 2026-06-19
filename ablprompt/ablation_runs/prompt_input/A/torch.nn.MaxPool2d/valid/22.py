import torch
import torch.nn as nn

# Create an instance of MaxPool2d
maxpool = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)

# Example input tensor (batch size 1, channels 1, height 4, width 4)
input_tensor = torch.randn(1, 1, 4, 4)

# Apply max pooling
output_tensor = maxpool(input_tensor)

print(output_tensor)