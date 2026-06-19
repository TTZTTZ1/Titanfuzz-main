import torch
import torch.nn as nn

# Example usage of LayerNorm on a 3D tensor representing a sequence of token embeddings
batch_size, seq_len, embedding_dim = 16, 100, 768
input_tensor = torch.randn(batch_size, seq_len, embedding_dim)

# Define LayerNorm with specific parameters
layer_norm = nn.LayerNorm(normalized_shape=[embedding_dim], eps=1e-05, elementwise_affine=True, bias=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be [16, 100, 768]