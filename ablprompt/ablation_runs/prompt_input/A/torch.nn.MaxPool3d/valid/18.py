import torch
import torch.nn as nn

# Define a simple 3D tensor
input_tensor = torch.randn(1, 1, 20, 20, 20)

# Create a MaxPool3d layer with kernel size of 2 and stride of 2
max_pool_layer = nn.MaxPool3d(kernel_size=2, stride=2)

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool_layer(input_tensor)

print(output_tensor.shape)