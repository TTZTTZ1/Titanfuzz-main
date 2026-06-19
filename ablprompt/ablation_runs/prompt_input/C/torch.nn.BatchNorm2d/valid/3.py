import torch
import torch.nn as nn

# Create a random input tensor with shape (N, C, H, W)
input_tensor = torch.randn(32, 64, 32, 32)

# Initialize BatchNorm2d layer with 64 features
batch_norm = nn.BatchNorm2d(num_features=64)

# Apply batch normalization to the input tensor
output_tensor = batch_norm(input_tensor)

print(output_tensor.shape)  # Expected output shape: (32, 64, 32, 32)