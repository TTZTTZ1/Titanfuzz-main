import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Initialize BatchNorm2d layer
batch_norm = nn.BatchNorm2d(num_features=3)

# Apply BatchNorm2d to the input tensor
output_tensor = batch_norm(input_tensor)

print(output_tensor)