import torch
import torch.nn as nn

# Create an input tensor
input_tensor = torch.randn(10, 20)

# Initialize LayerNorm layer
layer_norm = nn.LayerNorm(normalized_shape=20)

# Apply LayerNorm to the input tensor
normalized_output = layer_norm(input_tensor)

print("Input Tensor:", input_tensor)
print("Normalized Output:", normalized_output)