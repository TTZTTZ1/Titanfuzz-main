import torch
from torch.nn import MultiheadAttention

# Define the dimensions and number of heads
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads)

# Generate random query, key, and value tensors
query = torch.randn(32, 10, embed_dim)
key = torch.randn(32, 10, embed_dim)
value = torch.randn(32, 10, embed_dim)

# Perform the forward pass through the multihead attention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)