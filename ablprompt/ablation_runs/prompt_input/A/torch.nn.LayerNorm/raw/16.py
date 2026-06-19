import torch

# Create an input tensor
input_tensor = torch.randn(10, 20)

# Define LayerNorm layer
layer_norm = torch.nn.LayerNorm(normalized_shape=20)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)