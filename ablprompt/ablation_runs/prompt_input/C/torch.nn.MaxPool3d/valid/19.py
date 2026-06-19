import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 8, 8, 8)

# Define the MaxPool3d layer
max_pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=0, dilation=1, return_indices=False, ceil_mode=False)

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)