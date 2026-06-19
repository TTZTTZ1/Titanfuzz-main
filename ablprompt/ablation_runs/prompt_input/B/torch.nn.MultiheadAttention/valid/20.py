import torch
from torch.nn import MultiheadAttention

# Define the dimensions and number of heads
embed_dim = 256
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Generate random query, key, and value tensors
query = torch.randn(32, 10, embed_dim)  # Batch size=32, sequence length=10, embedding dim=256
key = query
value = query

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)