import torch
import torch.nn as nn

# Define the input tensor
input_tensor = torch.randn(32, 10, 24, requires_grad=True)

# Create a LayerNorm layer with specific parameters
layer_norm = nn.LayerNorm(normalized_shape=(10, 24), eps=1e-6, elementwise_affine=True, bias=False)

# Apply the LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be [32, 10, 24]