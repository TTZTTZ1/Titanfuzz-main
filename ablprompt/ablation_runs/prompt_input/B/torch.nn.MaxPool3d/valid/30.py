import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 7, 9)

# Define MaxPool3d layer with custom parameters
max_pool = nn.MaxPool3d(kernel_size=(2, 3, 4), stride=(1, 2, 2), padding=(1, 1, 1), dilation=1, return_indices=False, ceil_mode=True)

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)