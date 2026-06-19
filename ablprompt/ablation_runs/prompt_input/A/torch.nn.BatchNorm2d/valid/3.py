import torch
from torch import nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define BatchNorm2d layer with default parameters
batch_norm_layer = nn.BatchNorm2d(num_features=3)

# Apply the batch normalization to the input tensor
output_tensor = batch_norm_layer(input_tensor)

print(output_tensor.shape)