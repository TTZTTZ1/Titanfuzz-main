import torch
from torch.nn import MultiheadAttention

# Define input tensors
embed_dim = 256
num_heads = 8
batch_size = 32
seq_len = 10

query = torch.randn(seq_len, batch_size, embed_dim)
key = query
value = query

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should be (seq_len, batch_size, embed_dim)
print(attn_output_weights.shape)  # Should be (num_heads, seq_len, seq_len)