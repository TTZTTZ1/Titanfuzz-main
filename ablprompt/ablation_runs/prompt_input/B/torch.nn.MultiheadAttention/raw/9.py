import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 256
num_heads = 8
batch_size = 32
sequence_length = 10

# Create random query, key, and value tensors
query = torch.randn(batch_size, sequence_length, embed_dim)
key = torch.randn(batch_size, sequence_length, embed_dim)
value = torch.randn(batch_size, sequence_length, embed_dim)

# Initialize MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)