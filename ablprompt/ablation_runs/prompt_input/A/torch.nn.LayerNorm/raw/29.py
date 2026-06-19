import torch
import torch.nn as nn

# Create an instance of LayerNorm
layer_norm = nn.LayerNorm(normalized_shape=3, eps=1e-5)

# Example input tensor
input_tensor = torch.randn(2, 3)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)