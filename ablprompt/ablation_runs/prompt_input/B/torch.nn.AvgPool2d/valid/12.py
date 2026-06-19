import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define AvgPool2d layer with specific parameters
pooling_layer = nn.AvgPool2d(kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))

# Apply the pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print(output_tensor.shape)