import torch
from torch.nn import MultiheadAttention

# Define hyperparameters
embed_dim = 512
num_heads = 8
batch_size = 32
seq_len = 10

# Create query, key, and value tensors
query = torch.randn(batch_size, seq_len, embed_dim)
key = torch.randn(batch_size, seq_len, embed_dim)
value = torch.randn(batch_size, seq_len, embed_dim)

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Compute attention output
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)