import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 7, 9)

# Define the MaxPool3d layer
max_pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)