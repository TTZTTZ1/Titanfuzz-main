import torch
import torch.nn as nn

# Define an AdaptiveMaxPool2d layer with specified output size
output_size = (3, 3)
adaptive_max_pool = nn.AdaptiveMaxPool2d(output_size)

# Create a random input tensor with shape (batch_size, channels, height, width)
input_tensor = torch.randn(1, 64, 8, 9)

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)