import torch
import torch.nn as nn

# Create a random 5D tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define MaxPool3d layer with kernel size of 2 and stride of 2
maxpool_layer = nn.MaxPool3d(kernel_size=2, stride=2)

# Apply MaxPool3d to the input tensor
output_tensor = maxpool_layer(input_tensor)

print(output_tensor.shape)