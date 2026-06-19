import torch
from torch.nn import AvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the AvgPool2d layer
pool = AvgPool2d(kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)