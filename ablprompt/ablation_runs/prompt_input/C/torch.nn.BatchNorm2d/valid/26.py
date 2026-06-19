import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(32, 64, 32, 32)

# Initialize BatchNorm2d layer with 64 channels
bn_layer = nn.BatchNorm2d(num_features=64)

# Apply batch normalization to the input tensor
output_tensor = bn_layer(input_tensor)

print(output_tensor.shape)