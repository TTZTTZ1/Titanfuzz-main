import torch
import torch.nn as nn

# Example input tensor with shape (batch_size, sequence_length, embedding_dim)
input_tensor = torch.randn(32, 10, 64)

# Define LayerNorm with normalized_shape set to the embedding dimension
layer_norm = nn.LayerNorm(normalized_shape=[64])

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([32, 10, 64])