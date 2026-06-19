import torch
from torch.nn import AvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the average pooling layer
pooling_layer = AvgPool2d(kernel_size=2, stride=2, padding=0)

# Apply the pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print(output_tensor)