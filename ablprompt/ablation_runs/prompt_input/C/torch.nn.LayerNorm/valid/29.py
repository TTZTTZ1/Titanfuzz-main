import torch
import torch.nn as nn

# Example usage of LayerNorm on a sequence of embeddings
embedding_dim = 128
batch_size = 32
sequence_length = 10

# Create a random input tensor
input_tensor = torch.randn(batch_size, sequence_length, embedding_dim)

# Initialize LayerNorm
layer_norm = nn.LayerNorm(normalized_shape=(embedding_dim,), eps=1e-6, elementwise_affine=True, bias=True)

# Apply LayerNorm
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be (batch_size, sequence_length, embedding_dim)