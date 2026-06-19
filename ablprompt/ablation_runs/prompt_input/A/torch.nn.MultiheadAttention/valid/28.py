import torch
from torch.nn import MultiheadAttention

# Define input dimensions
embed_dim = 256
num_heads = 8
batch_size = 32
seq_len = 10

# Create random input tensors
query = torch.randn(batch_size, seq_len, embed_dim)
key = query.clone()
value = query.clone()

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)