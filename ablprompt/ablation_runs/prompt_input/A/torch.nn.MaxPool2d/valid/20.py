import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the MaxPool2d layer
maxpool = nn.MaxPool2d(kernel_size=2, stride=2)

# Apply the MaxPool2d layer to the input tensor
output_tensor = maxpool(input_tensor)

print(output_tensor)