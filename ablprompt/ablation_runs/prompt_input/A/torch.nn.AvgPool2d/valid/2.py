import torch
from torch import nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the average pooling layer
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)

# Apply the average pooling operation
output_tensor = avg_pool(input_tensor)

print(output_tensor)