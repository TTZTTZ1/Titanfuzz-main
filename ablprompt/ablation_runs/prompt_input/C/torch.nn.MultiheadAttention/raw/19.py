import torch
from torch.nn import MultiheadAttention

# Define the dimensions
embed_dim = 512
num_heads = 8

# Create the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Prepare some random input tensors
query = torch.randn(10, 32, embed_dim)  # (sequence_length, batch_size, embed_dim)
key = torch.randn(10, 32, embed_dim)    # (sequence_length, batch_size, embed_dim)
value = torch.randn(10, 32, embed_dim)  # (sequence_length, batch_size, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)