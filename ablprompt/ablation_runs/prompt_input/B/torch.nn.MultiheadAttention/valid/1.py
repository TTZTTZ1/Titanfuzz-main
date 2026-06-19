import torch
from torch.nn import MultiheadAttention

# Define the dimensions and number of heads
embed_dim = 512
num_heads = 8

# Initialize the MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Create dummy input tensors
query = torch.randn(32, 64, embed_dim)
key = torch.randn(32, 64, embed_dim)
value = torch.randn(32, 64, embed_dim)

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)