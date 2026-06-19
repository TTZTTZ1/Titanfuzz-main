import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention module
embed_dim = 256
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Prepare input tensors
batch_size = 32
seq_len = 10
query = torch.randn(seq_len, batch_size, embed_dim)
key = query
value = query

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([10, 32, 256])
print(attn_output_weights.shape)  # Should print: torch.Size([32, 8, 10, 10])