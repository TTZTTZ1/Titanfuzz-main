import torch
from torch.nn import MultiheadAttention

# Define the dimensions and number of heads
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads)

# Generate random query, key, and value tensors
query = torch.randn(10, 32, embed_dim)  # Batch size: 10, Sequence length: 32, Embedding dim: 512
key = torch.randn(10, 32, embed_dim)    # Batch size: 10, Sequence length: 32, Embedding dim: 512
value = torch.randn(10, 32, embed_dim)  # Batch size: 10, Sequence length: 32, Embedding dim: 512

# Perform multi-head attention
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)