import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4, 5)

# Define LayerNorm with specific parameters
layer_norm = nn.LayerNorm(normalized_shape=(4, 5), eps=1e-06, elementwise_affine=False, bias=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([3, 4, 5])