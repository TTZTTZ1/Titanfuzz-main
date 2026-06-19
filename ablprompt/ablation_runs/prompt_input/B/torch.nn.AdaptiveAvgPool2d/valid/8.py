import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 3)
pool = nn.AdaptiveAvgPool2d((3, 3))

# Create a random input tensor with shape (1, 64, 8, 8)
input_tensor = torch.randn(1, 64, 8, 8)

# Apply the adaptive average pooling
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Should be (1, 64, 3, 3)