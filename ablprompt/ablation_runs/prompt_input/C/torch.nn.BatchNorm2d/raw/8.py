import torch
import torch.nn as nn

# Create a random input tensor with shape (32, 64, 3, 3)
input_tensor = torch.randn(32, 64, 3, 3)

# Initialize BatchNorm2d layer with 64 channels
batch_norm_layer = nn.BatchNorm2d(num_features=64)

# Apply batch normalization to the input tensor
output_tensor = batch_norm_layer(input_tensor)

print(output_tensor.shape)  # Output should be (32, 64, 3, 3)