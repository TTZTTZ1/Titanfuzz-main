import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Generate random query, key, and value tensors
query = torch.randn(32, 10, embed_dim)  # Batch size 32, sequence length 10, embedding dim 512
key = torch.randn(32, 10, embed_dim)
value = torch.randn(32, 10, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should be [32, 10, 512]
print(attn_output_weights.shape)  # Should be [32, 8, 10, 10]