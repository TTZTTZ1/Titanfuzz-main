import torch
from torch.nn import AvgPool2d

# Create an input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Define the average pooling layer
pooling_layer = AvgPool2d(kernel_size=2, stride=2)

# Apply the pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print(output_tensor)