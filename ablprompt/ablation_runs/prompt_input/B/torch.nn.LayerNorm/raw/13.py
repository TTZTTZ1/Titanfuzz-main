import torch
import torch.nn as nn

# Define the LayerNorm layer with specific parameters
layer_norm = nn.LayerNorm(normalized_shape=(3, 4), eps=1e-06, elementwise_affine=False)

# Create a random input tensor
input_tensor = torch.randn(2, 3, 4)

# Apply the LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)