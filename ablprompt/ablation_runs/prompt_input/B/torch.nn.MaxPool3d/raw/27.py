import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define MaxPool3d layer with custom parameters
max_pool_layer = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(1, 1, 1), padding=(1, 1, 1), dilation=(1, 1, 1))

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool_layer(input_tensor)

print(output_tensor.shape)