import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define a BatchNorm2d layer
bn_layer = nn.BatchNorm2d(num_features=3)

# Apply the BatchNorm2d layer to the input tensor
output_tensor = bn_layer(input_tensor)