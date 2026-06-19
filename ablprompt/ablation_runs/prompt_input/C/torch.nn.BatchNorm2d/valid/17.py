import torch
import torch.nn as nn

# Create a random input tensor with shape (32, 3, 64, 64)
input_tensor = torch.randn(32, 3, 64, 64)

# Initialize BatchNorm2d layer with 3 feature channels
bn_layer = nn.BatchNorm2d(num_features=3)

# Apply batch normalization to the input tensor
output_tensor = bn_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([32, 3, 64, 64])