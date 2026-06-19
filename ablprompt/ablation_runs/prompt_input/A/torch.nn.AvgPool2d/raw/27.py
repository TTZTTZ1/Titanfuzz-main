import torch
from torch.nn import AvgPool2d

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Define the kernel size and stride for the average pooling
kernel_size = (2, 2)
stride = (2, 2)

# Create an instance of AvgPool2d
avg_pool = AvgPool2d(kernel_size=kernel_size, stride=stride)

# Apply the average pooling to the input tensor
output_tensor = avg_pool(input_tensor)

print(output_tensor)