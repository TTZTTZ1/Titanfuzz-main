import torch
from torch.nn import AdaptiveAvgPool2d

# Create a random input tensor of shape (1, 3, 5, 5)
input_tensor = torch.randn(1, 3, 5, 5)

# Define the adaptive average pooling layer to reduce the spatial dimensions to (2, 2)
pooling_layer = AdaptiveAvgPool2d((2, 2))

# Apply the pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)