import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(10, 20)

# Initialize LayerNorm layer with normalized_shape=20 and eps=1e-5
layer_norm = nn.LayerNorm(normalized_shape=20, eps=1e-5)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)