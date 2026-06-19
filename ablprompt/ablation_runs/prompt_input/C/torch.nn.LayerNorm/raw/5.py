import torch
import torch.nn as nn

# Example input tensor with shape (batch_size, sequence_length, hidden_size)
input_tensor = torch.randn(32, 10, 256)

# Create a LayerNorm layer with normalized_shape [sequence_length, hidden_size]
layer_norm = nn.LayerNorm(normalized_shape=[10, 256], eps=1e-05, elementwise_affine=True, bias=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([32, 10, 256])