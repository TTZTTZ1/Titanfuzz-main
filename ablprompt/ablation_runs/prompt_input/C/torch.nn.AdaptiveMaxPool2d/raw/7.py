import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 4)
max_pool = nn.AdaptiveMaxPool2d((3, 4))

# Create a random input tensor with shape (1, 10, 6, 8)
input_tensor = torch.randn(1, 10, 6, 8)

# Apply the adaptive max pooling layer to the input tensor
output_tensor = max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)