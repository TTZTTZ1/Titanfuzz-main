import torch
import torch.nn as nn

# Define a random input tensor
input_tensor = torch.randn(1, 3, 20, 20)

# Create an AdaptiveMaxPool2d layer with output size (10, 10)
adaptive_max_pool = nn.AdaptiveMaxPool2d((10, 10))

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)