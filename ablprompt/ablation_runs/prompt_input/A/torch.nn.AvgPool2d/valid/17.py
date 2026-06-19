import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define an AvgPool2d layer with kernel size of 2 and stride of 1
avg_pool = nn.AvgPool2d(kernel_size=2, stride=1)

# Apply the AvgPool2d layer to the input tensor
output_tensor = avg_pool(input_tensor)

print(output_tensor)