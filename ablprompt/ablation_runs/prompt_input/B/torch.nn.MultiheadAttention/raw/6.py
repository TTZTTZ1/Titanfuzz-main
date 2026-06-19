import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8

# Create the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Generate random query, key, and value tensors
query = torch.randn(32, 10, embed_dim)
key = torch.randn(32, 10, embed_dim)
value = torch.randn(32, 10, embed_dim)

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)