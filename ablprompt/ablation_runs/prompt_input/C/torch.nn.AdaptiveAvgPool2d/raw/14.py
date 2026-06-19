import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 4)
pool = nn.AdaptiveAvgPool2d((3, 4))

# Example input tensor with shape (1, 6, 8)
input_tensor = torch.randn(1, 6, 8)

# Apply the pool layer
output_tensor = pool(input_tensor)

print("Input Shape:", input_tensor.shape)
print("Output Shape:", output_tensor.shape)