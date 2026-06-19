import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Define BatchNorm2d layer with default parameters
batch_norm = nn.BatchNorm2d(num_features=3)

# Apply batch normalization to the input tensor
output_tensor = batch_norm(input_tensor)

print(output_tensor)