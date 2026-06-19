import torch
from torch.nn import MaxPool2d

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the max pooling layer
max_pool = MaxPool2d(kernel_size=2, stride=2)

# Apply the max pooling operation
output_tensor = max_pool(input_tensor)

print(output_tensor)