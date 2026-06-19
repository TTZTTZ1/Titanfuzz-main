import torch
from torch.nn import MultiheadAttention

# Define input tensors for the MultiheadAttention layer
batch_size = 2
seq_length = 4
embed_dim = 16
num_heads = 2

query = torch.randn(batch_size, seq_length, embed_dim)
key = query.clone()
value = query.clone()

# Initialize the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Perform the forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Output shape:", attn_output.shape)
print("Attention weights shape:", attn_output_weights.shape)