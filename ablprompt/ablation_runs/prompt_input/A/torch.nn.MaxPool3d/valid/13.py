import torch
from torch import nn

# Create a random input tensor of shape (1, 1, 2, 4, 6)
input_tensor = torch.randn(1, 1, 2, 4, 6)

# Define a MaxPool3d layer with kernel size of 2 and stride of 2
max_pool = nn.MaxPool3d(kernel_size=2, stride=2)

# Apply the max pooling operation to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 1, 1, 2, 3])