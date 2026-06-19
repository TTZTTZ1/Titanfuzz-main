import torch
from torch.nn import MultiheadAttention

# Define the dimensions and number of heads
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(embed_dim, num_heads, batch_first=True)

# Generate random query, key, and value tensors
batch_size = 32
sequence_length = 10
query = torch.randn(batch_size, sequence_length, embed_dim)
key = torch.randn(batch_size, sequence_length, embed_dim)
value = torch.randn(batch_size, sequence_length, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Attention Output:", attn_output.shape)
print("Attention Weights:", attn_output_weights.shape)