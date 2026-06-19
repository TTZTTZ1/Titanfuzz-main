import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(32, 64, 56, 56)

# Initialize BatchNorm2d layer
bn_layer = nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

# Apply batch normalization
output_tensor = bn_layer(input_tensor)

print(output_tensor.shape)  # Should be (32, 64, 56, 56)