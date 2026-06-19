import torch
from torch.nn import AdaptiveMaxPool2d

# Create an input tensor
input_tensor = torch.randn(1, 3, 24, 24)

# Define the adaptive max pooling layer
output_size = (8, 8)
adaptive_max_pool = AdaptiveMaxPool2d(output_size)

# Apply the adaptive max pooling layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)