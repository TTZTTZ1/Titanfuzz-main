import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define the AdaptiveMaxPool2d layer
pool = nn.AdaptiveMaxPool2d((1, 1))

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)