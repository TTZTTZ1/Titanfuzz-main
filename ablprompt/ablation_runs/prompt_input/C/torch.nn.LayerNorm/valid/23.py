import torch
import torch.nn as nn

# Example usage of LayerNorm on a 3D tensor representing a sequence of token embeddings
batch_size = 2
seq_len = 4
embedding_dim = 8

# Create a random input tensor
input_tensor = torch.randn(batch_size, seq_len, embedding_dim)

# Initialize LayerNorm with normalized_shape set to the embedding dimension
layer_norm = nn.LayerNorm(normalized_shape=embedding_dim)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after LayerNorm:", output_tensor)