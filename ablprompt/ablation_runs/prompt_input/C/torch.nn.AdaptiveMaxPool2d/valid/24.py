import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
adaptive_max_pool = nn.AdaptiveMaxPool2d((3, 3))

# Example input tensor with shape (1, 10, 16, 16)
input_tensor = torch.randn(1, 10, 16, 16)

# Apply the adaptive max pooling
output_tensor = adaptive_max_pool(input_tensor)

print("Input Shape:", input_tensor.shape)
print("Output Shape:", output_tensor.shape)