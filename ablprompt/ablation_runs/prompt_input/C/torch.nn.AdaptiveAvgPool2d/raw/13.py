import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 4)
pool = nn.AdaptiveAvgPool2d((3, 4))

# Create a random input tensor of shape (1, 64, 8, 12)
input_tensor = torch.randn(1, 64, 8, 12)

# Apply the adaptive average pooling
output_tensor = pool(input_tensor)

print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)