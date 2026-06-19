import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8
batch_size = 32
seq_len = 10

# Create random query, key, and value tensors
query = torch.randn(batch_size, seq_len, embed_dim)
key = torch.randn(batch_size, seq_len, embed_dim)
value = torch.randn(batch_size, seq_len, embed_dim)

# Initialize the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)