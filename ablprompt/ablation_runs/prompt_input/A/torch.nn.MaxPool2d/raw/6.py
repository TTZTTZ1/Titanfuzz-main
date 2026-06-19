import torch
import torch.nn as nn

# Create a MaxPool2d layer
maxpool = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)

# Example input tensor
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size of 1, 3 channels, 5x5 spatial dimensions

# Apply the MaxPool2d layer to the input tensor
output_tensor = maxpool(input_tensor)

print(output_tensor)