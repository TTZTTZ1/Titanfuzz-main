import torch
from torch.nn import MultiheadAttention

# Define hyperparameters
embed_dim = 512
num_heads = 8

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads, batch_first=True)

# Create dummy input tensors
query = torch.randn(10, 32, embed_dim)  # (sequence_length, batch_size, embed_dim)
key = query
value = query

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)