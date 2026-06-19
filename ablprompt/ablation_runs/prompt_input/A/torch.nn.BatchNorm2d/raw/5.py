import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Initialize BatchNorm2d layer
batch_norm = nn.BatchNorm2d(num_features=3)

# Apply batch normalization to the input tensor
output_tensor = batch_norm(input_tensor)