import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention layer
embed_dim = 256
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Create some random input tensors
query = torch.randn(10, 32, embed_dim)  # (seq_len, batch_size, embed_dim)
key = query  # For simplicity, using the same for keys
value = query  # And values

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should be (seq_len, batch_size, embed_dim)
print(attn_output_weights.shape)  # Should be (batch_size, num_heads, seq_len, seq_len)