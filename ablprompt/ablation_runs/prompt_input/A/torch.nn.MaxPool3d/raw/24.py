import torch
import torch.nn as nn

# Create a random 5D tensor
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Define the MaxPool3d layer with kernel size of 2 and stride of 2
maxpool_layer = nn.MaxPool3d(kernel_size=2, stride=2)

# Apply the MaxPool3d layer to the input tensor
output_tensor = maxpool_layer(input_tensor)

print(output_tensor)