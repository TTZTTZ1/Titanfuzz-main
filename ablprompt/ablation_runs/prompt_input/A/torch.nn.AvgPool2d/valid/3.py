import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the AvgPool2d layer
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)

# Apply the AvgPool2d layer to the input tensor
output_tensor = avg_pool(input_tensor)

print(output_tensor.shape)