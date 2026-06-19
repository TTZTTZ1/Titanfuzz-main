import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 4)
pool = nn.AdaptiveAvgPool2d((3, 4))

# Generate a random input tensor of shape (1, 64, 8, 10)
input_tensor = torch.randn(1, 64, 8, 10)

# Apply the pooling operation
output_tensor = pool(input_tensor)

print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)