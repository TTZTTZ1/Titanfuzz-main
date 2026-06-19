import torch
import torch.nn as nn

# Define a simple 3D tensor
input_tensor = torch.randn(1, 1, 2, 4, 6)

# Create a MaxPool3d layer with kernel size of (2, 2, 2)
maxpool_layer = nn.MaxPool3d(kernel_size=(2, 2, 2))

# Apply the max pooling operation
output_tensor = maxpool_layer(input_tensor)

print(output_tensor.shape)  # Output should be [1, 1, 1, 2, 3]