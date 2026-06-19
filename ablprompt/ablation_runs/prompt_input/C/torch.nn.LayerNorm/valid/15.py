import torch
import torch.nn as nn

# Define the input tensor
input_tensor = torch.randn(32, 64, requires_grad=True)

# Create a LayerNorm layer
layer_norm = nn.LayerNorm(normalized_shape=[64], eps=1e-05, elementwise_affine=True, bias=True)

# Apply the LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Output should be [32, 64]