import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
adaptive_max_pool = nn.AdaptiveMaxPool2d((3, 3))

# Create a random input tensor of shape (1, 10, 16, 16)
input_tensor = torch.randn(1, 10, 16, 16)

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)