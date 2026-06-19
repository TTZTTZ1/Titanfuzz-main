import torch
from torch.nn import MultiheadAttention

# Define input tensors for query, key, and value
query = torch.randn(10, 32, 64)  # (seq_len, batch_size, embed_dim)
key = torch.randn(10, 32, 64)    # (seq_len, batch_size, embed_dim)
value = torch.randn(10, 32, 64)  # (seq_len, batch_size, embed_dim)

# Initialize the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim=64, num_heads=8)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)