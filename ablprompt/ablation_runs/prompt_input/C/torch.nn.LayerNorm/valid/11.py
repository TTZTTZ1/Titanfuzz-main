import torch
import torch.nn as nn

# Example input tensor
input_tensor = torch.randn(3, 4, 5)  # Batch size 3, sequence length 4, feature dimension 5

# Create a LayerNorm layer
layer_norm = nn.LayerNorm(normalized_shape=[4, 5], eps=1e-6, elementwise_affine=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be the same shape as input_tensor: [3, 4, 5]