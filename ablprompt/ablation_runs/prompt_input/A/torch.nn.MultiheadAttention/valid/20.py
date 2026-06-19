import torch
from torch.nn import MultiheadAttention

# Define input dimensions
embed_dim = 256
num_heads = 8
batch_size = 32
seq_len = 10

# Create random input tensors
query = torch.randn(batch_size, seq_len, embed_dim)
key = torch.randn(batch_size, seq_len, embed_dim)
value = torch.randn(batch_size, seq_len, embed_dim)

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Output shape:", attn_output.shape)
print("Attention weights shape:", attn_output_weights.shape)