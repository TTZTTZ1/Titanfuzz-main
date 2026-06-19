import torch
import torch.nn as nn

# Example usage of LayerNorm on a sequence of embeddings
embedding_dim = 768
batch_size = 32
sequence_length = 128

# Create a random input tensor of shape (batch_size, sequence_length, embedding_dim)
input_tensor = torch.randn(batch_size, sequence_length, embedding_dim)

# Initialize LayerNorm with the specified normalized shape
layer_norm = nn.LayerNorm(normalized_shape=(embedding_dim,), eps=1e-5, elementwise_affine=True, bias=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)