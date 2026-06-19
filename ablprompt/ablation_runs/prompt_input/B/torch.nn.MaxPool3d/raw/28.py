import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 7, 9)

# Define MaxPool3d layer
max_pool = nn.MaxPool3d(kernel_size=(2, 3, 4), stride=(1, 2, 2), padding=(1, 1, 1), dilation=(1, 1, 1))

# Apply max pooling
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)