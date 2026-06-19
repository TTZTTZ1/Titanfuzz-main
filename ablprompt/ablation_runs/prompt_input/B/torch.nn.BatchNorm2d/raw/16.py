import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(32, 3, 64, 64)

# Define BatchNorm2d layer with specific parameters
batch_norm = nn.BatchNorm2d(num_features=3, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

# Apply batch normalization to the input tensor
output_tensor = batch_norm(input_tensor)

print(output_tensor.shape)