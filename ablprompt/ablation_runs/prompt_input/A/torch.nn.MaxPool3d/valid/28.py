import torch
from torch.nn import MaxPool3d

# Create a dummy input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define the max pooling layer
max_pool_layer = MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply the max pooling operation
output_tensor = max_pool_layer(input_tensor)

print(output_tensor.shape)