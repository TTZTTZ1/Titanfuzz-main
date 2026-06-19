import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Generate some random query, key, and value tensors
query = torch.randn(32, 10, embed_dim)
key = torch.randn(32, 10, embed_dim)
value = torch.randn(32, 10, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should be [32, 10, embed_dim]
print(attn_output_weights.shape)  # Should be [32, num_heads, 10, 10]