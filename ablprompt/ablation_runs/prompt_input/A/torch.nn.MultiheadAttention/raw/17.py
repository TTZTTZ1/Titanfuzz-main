import torch
from torch.nn import MultiheadAttention

# Define the input tensors for the MultiheadAttention layer
query = torch.randn(10, 32, 64)  # (seq_len, batch_size, embed_dim)
key = query
value = query

# Initialize the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim=64, num_heads=8)

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should be (seq_len, batch_size, embed_dim)
print(attn_output_weights.shape)  # Should be (num_heads, seq_len, seq_len)