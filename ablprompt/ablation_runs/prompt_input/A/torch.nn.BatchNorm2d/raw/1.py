import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define BatchNorm2d layer
batch_norm = nn.BatchNorm2d(num_features=3)

# Apply BatchNorm2d to the input tensor
output_tensor = batch_norm(input_tensor)

print(output_tensor)