import torch
import torch.nn as nn

# Define the input tensor
input_tensor = torch.randn(3, 10, requires_grad=True)

# Create a LayerNorm layer with normalized shape [10]
layer_norm = nn.LayerNorm(normalized_shape=[10])

# Apply the LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)