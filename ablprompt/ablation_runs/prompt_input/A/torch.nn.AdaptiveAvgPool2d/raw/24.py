import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define AdaptiveAvgPool2d layer
output_size = (7, 7)
adaptive_avg_pool = nn.AdaptiveAvgPool2d(output_size)

# Apply the adaptive average pooling
output_tensor = adaptive_avg_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)