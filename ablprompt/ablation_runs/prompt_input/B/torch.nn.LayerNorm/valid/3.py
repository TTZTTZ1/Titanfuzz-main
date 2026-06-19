import torch
import torch.nn as nn

# Example input tensor
input_tensor = torch.randn(32, 128, requires_grad=True)

# Define LayerNorm
layer_norm = nn.LayerNorm(normalized_shape=(128,), eps=1e-6, elementwise_affine=True, bias=True)

# Apply LayerNorm
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be [32, 128]