import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 20)

# Define LayerNorm
layer_norm = nn.LayerNorm(normalized_shape=20)

# Apply LayerNorm to the input tensor
normalized_tensor = layer_norm(input_tensor)

print(normalized_tensor)