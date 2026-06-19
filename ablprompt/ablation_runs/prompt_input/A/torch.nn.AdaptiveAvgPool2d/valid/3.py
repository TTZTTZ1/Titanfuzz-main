import torch
from torch.nn import AdaptiveAvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define the output size for adaptive average pooling
output_size = (7, 7)

# Create an instance of AdaptiveAvgPool2d
adaptive_avg_pool = AdaptiveAvgPool2d(output_size)

# Apply the adaptive average pooling to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)