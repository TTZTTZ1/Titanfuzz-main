import torch
from torch.nn import MaxPool3d

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Define the max pooling layer
max_pool = MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply the max pooling operation
output_tensor = max_pool(input_tensor)

print(output_tensor)