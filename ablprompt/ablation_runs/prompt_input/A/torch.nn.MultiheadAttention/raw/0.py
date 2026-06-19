import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention module
embed_dim = 256
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Create some random input tensors
query = torch.randn(10, 32, embed_dim)
key = torch.randn(10, 32, embed_dim)
value = torch.randn(10, 32, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([10, 32, 256])
print(attn_output_weights.shape)  # Should print: torch.Size([10, 32, 32])