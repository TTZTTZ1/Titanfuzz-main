import torch
import torch.nn as nn

# Example usage of LayerNorm for an NLP task
embedding_dim = 768
batch_size = 32
sequence_length = 128

# Create a random input tensor of shape (batch_size, sequence_length, embedding_dim)
input_tensor = torch.randn(batch_size, sequence_length, embedding_dim)

# Initialize LayerNorm with the same embedding dimension
layer_norm = nn.LayerNorm(embedding_dim)

# Apply LayerNorm to the input tensor
normalized_tensor = layer_norm(input_tensor)

print(normalized_tensor.shape)  # Output should be (batch_size, sequence_length, embedding_dim)