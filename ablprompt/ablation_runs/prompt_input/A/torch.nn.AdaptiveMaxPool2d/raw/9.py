import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 64, 64)
input_tensor = torch.randn(1, 3, 64, 64)

# Define an AdaptiveMaxPool2d layer with output size (8, 8)
adaptive_maxpool = nn.AdaptiveMaxPool2d((8, 8))

# Apply the adaptive max pooling to the input tensor
output_tensor = adaptive_maxpool(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 8, 8])