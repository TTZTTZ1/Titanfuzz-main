import torch
import torch.nn as nn

# Example usage of LayerNorm on a sequence of token embeddings
embedding_dim = 128
batch_size = 32
sequence_length = 50

# Create a random input tensor representing a batch of sequences of token embeddings
input_tensor = torch.randn(batch_size, sequence_length, embedding_dim)

# Initialize LayerNorm with the same number of features as the embedding dimension
layer_norm = nn.LayerNorm(normalized_shape=embedding_dim)

# Apply LayerNorm to the input tensor
normalized_output = layer_norm(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Normalized Output Shape:", normalized_output.shape)