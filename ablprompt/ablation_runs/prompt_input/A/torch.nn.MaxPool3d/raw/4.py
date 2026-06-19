import torch
import torch.nn as nn

# Create a random tensor
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Define the MaxPool3d layer
maxpool = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply the MaxPool3d layer to the input tensor
output_tensor = maxpool(input_tensor)

print(output_tensor)