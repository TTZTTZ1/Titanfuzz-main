import torch

# Example usage of LayerNorm for a simple 3D tensor representing a sequence of embeddings
batch_size = 4
seq_len = 10
embedding_dim = 8

# Create a random input tensor
input_tensor = torch.randn(batch_size, seq_len, embedding_dim)

# Initialize LayerNorm with normalized_shape corresponding to the embedding dimension
layer_norm = torch.nn.LayerNorm(normalized_shape=embedding_dim)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)