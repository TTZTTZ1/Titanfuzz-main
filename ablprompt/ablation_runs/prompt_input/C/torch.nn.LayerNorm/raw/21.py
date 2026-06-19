import torch
import torch.nn as nn

# Example input tensor with shape (batch_size, sequence_length, embedding_dim)
input_tensor = torch.randn(32, 100, 768)

# Define LayerNorm with normalized_shape matching the last dimension of the input tensor
layer_norm = nn.LayerNorm(normalized_shape=768)

# Apply LayerNorm to the input tensor
normalized_output = layer_norm(input_tensor)

print(normalized_output.shape)  # Should print: torch.Size([32, 100, 768])