import torch
from torch.nn import MultiheadAttention

# Define hyperparameters
embed_dim = 512
num_heads = 8
batch_size = 32
seq_len = 64

# Create random query, key, and value tensors
query = torch.randn(seq_len, batch_size, embed_dim)
key = torch.randn(seq_len, batch_size, embed_dim)
value = torch.randn(seq_len, batch_size, embed_dim)

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads, batch_first=True)

# Forward pass through the multihead attention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)