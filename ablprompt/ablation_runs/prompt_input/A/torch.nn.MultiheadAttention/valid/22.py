import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention layer
embed_dim = 512
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Create some random input data
batch_size = 32
seq_len = 64
query = torch.randn(seq_len, batch_size, embed_dim)
key = value = query  # For simplicity, using the same for key and value

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)