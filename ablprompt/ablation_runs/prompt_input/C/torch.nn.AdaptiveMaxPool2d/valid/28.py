import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size 5x7
m = nn.AdaptiveMaxPool2d((5, 7))

# Generate a random input tensor with shape (1, 64, 8, 9)
input_tensor = torch.randn(1, 64, 8, 9)

# Apply the adaptive max pooling
output_tensor = m(input_tensor)

print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)