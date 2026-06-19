import torch
from torch import nn

# Example input tensor with shape (batch_size, sequence_length, embedding_dim)
input_tensor = torch.randn(32, 100, 768)

# Define LayerNorm with specific parameters
layer_norm = nn.LayerNorm(normalized_shape=[768], eps=1e-05, elementwise_affine=True, bias=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([32, 100, 768])