import torch
from torch import nn

# Create a random tensor
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Define the MaxPool3d layer
maxpool_layer = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply the MaxPool3d layer to the input tensor
output_tensor = maxpool_layer(input_tensor)

print(output_tensor)