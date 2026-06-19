import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the AvgPool2d layer
pooling_layer = nn.AvgPool2d(kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))

# Apply the pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print(output_tensor.shape)