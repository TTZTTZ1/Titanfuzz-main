import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define the MaxPool3d layer
max_pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=(0, 0, 0))

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)