import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define AvgPool2d layer with specific parameters
pool_layer = nn.AvgPool2d(kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))

# Apply the pooling operation
output_tensor = pool_layer(input_tensor)

print(output_tensor.shape)