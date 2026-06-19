import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
m = nn.AdaptiveMaxPool2d((3, 3))

# Define a random input tensor with shape (1, 10, 10)
input_tensor = torch.randn(1, 10, 10)

# Apply the adaptive max pooling
output_tensor = m(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)