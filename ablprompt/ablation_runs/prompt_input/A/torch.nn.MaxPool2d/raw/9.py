import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define a MaxPool2d layer
maxpool_layer = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)

# Apply the MaxPool2d layer to the input tensor
output_tensor = maxpool_layer(input_tensor)

print(output_tensor)