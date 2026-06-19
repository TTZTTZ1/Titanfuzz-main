import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(32, 64, 28, 28)

# Define BatchNorm2d layer with specific parameters
batch_norm_layer = nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

# Apply batch normalization to the input tensor
output_tensor = batch_norm_layer(input_tensor)

print(output_tensor.shape)