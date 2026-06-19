import torch
import torch.nn as nn

# Define the dimensions and number of heads
embed_dim = 512
num_heads = 8

# Create an instance of MultiheadAttention
multihead_attn = nn.MultiheadAttention(embed_dim, num_heads)

# Generate random query, key, and value tensors
query = torch.randn(32, 10, embed_dim)
key = torch.randn(32, 10, embed_dim)
value = torch.randn(32, 10, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

# Print the shapes of the output tensors
print("Attention Output Shape:", attn_output.shape)
print("Attention Weights Shape:", attn_output_weights.shape)