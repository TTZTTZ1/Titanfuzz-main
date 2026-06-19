import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define MaxPool3d layer with custom parameters
max_pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply max pooling
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)