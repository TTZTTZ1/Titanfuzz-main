import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 1, 4, 4, 4)
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Define a MaxPool3d layer with kernel size 2 and stride 2
max_pool_layer = nn.MaxPool3d(kernel_size=2, stride=2)

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)