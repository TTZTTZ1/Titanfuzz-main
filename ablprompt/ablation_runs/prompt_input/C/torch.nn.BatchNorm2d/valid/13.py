import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(32, 64, 7, 7)

# Initialize BatchNorm2d layer with 64 features
batch_norm_layer = nn.BatchNorm2d(64)

# Apply batch normalization to the input tensor
output_tensor = batch_norm_layer(input_tensor)

print(output_tensor.shape)