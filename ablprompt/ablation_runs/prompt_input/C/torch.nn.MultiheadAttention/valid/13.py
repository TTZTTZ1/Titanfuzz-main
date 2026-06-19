import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads)

# Prepare some random data
query = torch.randn(32, 10, embed_dim)  # Batch size 32, sequence length 10, embedding dim 512
key = query
value = query

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)