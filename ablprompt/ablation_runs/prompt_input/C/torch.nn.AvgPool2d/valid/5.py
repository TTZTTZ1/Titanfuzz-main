import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define AvgPool2d layer
avg_pool = nn.AvgPool2d(kernel_size=3, stride=2, padding=1, ceil_mode=False, count_include_pad=True, divisor_override=None)

# Apply the AvgPool2d layer
output_tensor = avg_pool(input_tensor)

print(output_tensor.shape)