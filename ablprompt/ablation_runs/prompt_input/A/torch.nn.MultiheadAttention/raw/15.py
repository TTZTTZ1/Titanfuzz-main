import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention layer
embed_dim = 512
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Create some random input tensors
batch_size = 32
seq_length = 64
query = torch.randn(batch_size, seq_length, embed_dim)
key = torch.randn(batch_size, seq_length, embed_dim)
value = torch.randn(batch_size, seq_length, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)