import torch
from torch.nn import AdaptiveAvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define the adaptive average pooling layer
pooling_layer = AdaptiveAvgPool2d((16, 16))

# Apply the pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print(output_tensor.shape)  # Output should be [1, 3, 16, 16]