import torch
from torch.nn import MaxPool3d

# Define a random input tensor
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Create an instance of MaxPool3d with kernel size (2, 2, 2)
max_pool = MaxPool3d(kernel_size=(2, 2, 2))

# Apply the max pooling operation
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 3, 2, 2, 2]