import torch
import torch.nn as nn

# Define a simple 3D tensor
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Create an instance of MaxPool3d
maxpool = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply max pooling to the input tensor
output_tensor = maxpool(input_tensor)

print(output_tensor)