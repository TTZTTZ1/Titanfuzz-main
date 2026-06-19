import torch
from torch.nn import MultiheadAttention

# Initialize MultiheadAttention layer
embed_dim = 256
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Dummy input tensors
batch_size = 32
seq_len = 10
query = torch.randn(batch_size, seq_len, embed_dim)
key = torch.randn(batch_size, seq_len, embed_dim)
value = torch.randn(batch_size, seq_len, embed_dim)

# Forward pass through MultiheadAttention
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)