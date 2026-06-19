import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define BatchNorm2d layer
batch_norm_layer = nn.BatchNorm2d(num_features=3)

# Apply BatchNorm2d to the input tensor
output_tensor = batch_norm_layer(input_tensor)

print(output_tensor.shape)