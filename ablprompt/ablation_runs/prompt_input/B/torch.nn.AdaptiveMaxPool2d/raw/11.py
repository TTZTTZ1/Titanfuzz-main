import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 4)
max_pool = nn.AdaptiveMaxPool2d((3, 4))

# Generate a random input tensor with shape (2, 5, 10, 12)
input_tensor = torch.randn(2, 5, 10, 12)

# Apply the adaptive max pooling layer
output_tensor = max_pool(input_tensor)

print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)