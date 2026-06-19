import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention layer
embed_dim = 256
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Create dummy input tensors
batch_size = 32
seq_len = 10
query = torch.randn(seq_len, batch_size, embed_dim)
key = torch.randn(seq_len, batch_size, embed_dim)
value = torch.randn(seq_len, batch_size, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Output shape:", attn_output.shape)
print("Attention weights shape:", attn_output_weights.shape)