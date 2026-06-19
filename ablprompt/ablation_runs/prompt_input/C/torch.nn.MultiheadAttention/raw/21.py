import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads)

# Generate some random input tensors
query = torch.randn(10, 32, embed_dim)  # (sequence_length, batch_size, embed_dim)
key = query
value = query

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)